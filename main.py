import config
import telebot
from telebot import types
import sqlite3
from time import sleep
from database import *
from keyboards import courses_name, teachers_keyb, scores_keyb, yes_no
import datetime

joincourse = False
# подключаемся к боту
bot = telebot.TeleBot(config.TOKEN)
# подключаемся к базе данных
# execute_query(connection, create_csharp_db)
# execute_query(connection, create_cpp_db)
# execute_query(connection, create_python_db)
# execute_query(connection, create_java_db)

# start
@bot.message_handler(commands=['start'])
def command_handler(message):
    keyboard = types.InlineKeyboardMarkup()
    stud_btn = types.InlineKeyboardButton(text="Студент", callback_data='stud')
    teach_btn = types.InlineKeyboardButton(text="Преподаватель", callback_data='teach')
    keyboard.add(stud_btn)
    keyboard.add(teach_btn)
    bot.send_message(message.chat.id, config.start, reply_markup=keyboard)
# help
@bot.message_handler(commands=['help'])
def command_handler(message):
    bot.send_message(message.chat.id, config.help)

@bot.message_handler(commands=['courses'])
def handle_command(message):
    courses = types.InlineKeyboardMarkup()
    cs_btn = types.InlineKeyboardButton(text="CSharp", callback_data='cs')
    cpp_btn = types.InlineKeyboardButton(text="Cpp", callback_data='cpp')
    py_btn = types.InlineKeyboardButton(text="Python", callback_data='py')
    java_btn = types.InlineKeyboardButton(text="Java", callback_data='java')
    courses.add(cs_btn)
    courses.add(cpp_btn)
    courses.add(py_btn)
    courses.add(java_btn)
    bot.send_message(message.chat.id, "Выберите курс", reply_markup=courses)

@bot.message_handler(commands=['mycourses'])
def handle_command(message):
    mycourses = db.select_mycourses(message.chat.id)
    if mycourses:
        message_text = ""
        for course in mycourses:
            message_text = course+"\n"
        bot.send_message(message.chat.id, message_text)
    else:
        bot.send_message(message.chat.id, "Вы не записаны ни на один курс")



@bot.message_handler(commands=['aboutcourse'])
def handle_command(message):
    courses = types.InlineKeyboardMarkup()
    cs_btn = types.InlineKeyboardButton(text="CSharp", callback_data='about_cs')
    cpp_btn = types.InlineKeyboardButton(text="Cpp", callback_data='about_cpp')
    py_btn = types.InlineKeyboardButton(text="Python", callback_data='about_py')
    java_btn = types.InlineKeyboardButton(text="Java", callback_data='about_java')
    courses.add(cs_btn)
    courses.add(cpp_btn)
    courses.add(py_btn)
    courses.add(java_btn)
    bot.send_message(message.chat.id, "Выберите курс, о котором хотите узнать", reply_markup=courses)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    #mycourses
    btns = types.InlineKeyboardMarkup()
    # exit
    ex_c = types.InlineKeyboardButton(text="Покинуть курс", callback_data='exit_c')
    #marks
    CSmarks = types.InlineKeyboardButton(text="Оценки", callback_data='cs_marks')
    CPPmarks = types.InlineKeyboardButton(text="Оценки", callback_data='cpp_marks')
    Pymarks = types.InlineKeyboardButton(text="Оценки", callback_data='py_marks')
    Javamarks = types.InlineKeyboardButton(text="Оценки", callback_data='java_marks')

    # if - else
    if message.text == 'курс - CSharp':
        btns.add(CSmarks)
        btns.add(ex_c)
        bot.send_message(message.chat.id, "курс - CSharp", reply_markup=btns)
    elif message.text == 'курс - CPP':
        btns.add(CPPmarks)
        btns.add(ex_c)
        bot.send_message(message.chat.id, "курс - CPP", reply_markup=btns)
    elif message.text == 'курс - Python':
        btns.add(Pymarks)
        btns.add(ex_c)
        bot.send_message(message.chat.id, "курс - Python", reply_markup=btns)
    elif message.text == 'курс - Java':
        btns.add(Javamarks)
        btns.add(ex_c)
        bot.send_message(message.chat.id, "курс - Java", reply_markup=btns)

@bot.callback_query_handler(func=lambda call: True)
def callback_message(call):
    button = types.InlineKeyboardMarkup()
    joinCS = types.InlineKeyboardButton(text="Записаться", callback_data='c#')
    joinCPP = types.InlineKeyboardButton(text="Записаться", callback_data='c++')
    joinPy = types.InlineKeyboardButton(text="Записаться", callback_data='p')
    joinJava = types.InlineKeyboardButton(text="Записаться", callback_data='j')
    try:
        if call.message:
            if call.data == 'stud':
                bot.send_message(call.message.chat.id, config.for_student)  # get info for students
                sleep(1)
                bot.send_message(call.message.chat.id, 'Введите название курса: ', reply_markup=courses_name())
                bot.register_next_step_handler(call.message, state_for_course_name)
            elif call.data == 'teach':
                bot.send_message(call.message.chat.id, config.for_teachers)  # get info for teachers
                sleep(1)
                bot.send_message(call.message.chat.id, 'Введите ваш логин: ')
                bot.register_next_step_handler(call.message, state_for_teacher)
            elif call.data == 'about_cs':
                bot.send_message(call.message.chat.id, config.csharp)  # get info about courses
            elif call.data == 'about_cpp':
                bot.send_message(call.message.chat.id, config.cpp)
            elif call.data == 'about_py':
                bot.send_message(call.message.chat.id, config.python)
            elif call.data == 'about_java':
                bot.send_message(call.message.chat.id, config.java)
            elif call.data == 'cs':
                button.add(joinCS)
                bot.send_message(call.message.chat.id, config.csharp, reply_markup=button)  # get info about csharp, cpp, python, java
            elif call.data == 'cpp':
                button.add(joinCPP)
                bot.send_message(call.message.chat.id, config.cpp, reply_markup=button)
            elif call.data == 'py':
                button.add(joinPy)
                bot.send_message(call.message.chat.id, config.python, reply_markup=button)
            elif call.data == 'java':
                button.add(joinJava)
                bot.send_message(call.message.chat.id, config.java, reply_markup=button)
            elif call.data == 'c#' or call.data == 'c++' or call.data == 'p' or call.data == 'j':
                db.add_course_name(call.data)
                bot.send_message(call.message.chat.id, "Введите ФИО и группу в формате:\nИванов Иван Иванович 11-111:")   # join courses
            elif call.data in ['exit_cs', 'exit_cpp', 'exit_py', 'exit_java', 'exit_c']:
                bot.send_message(call.message.chat.id, config.exit_course)  # exit courses
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  reply_markup=None, text='priv')

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ALERT!!!")

    except Exception as e:
        print(repr(e))

def state_for_course_name(message):   ## состояние для ввода курса
    global course_name
    course_name = message.text
    a = find_in_students(message.chat.id)
    if a is False:
        bot.send_message(message.chat.id, 'Введите фамилию, имя и отчество в одно сообщение без знаков')
        bot.register_next_step_handler(message, state_for_name)
    else:
        bot.send_message(message.chat.id, get_name(message.chat.id)[0][0] + ' ' +
                         get_name(message.chat.id)[0][1] + ' ' + get_name(message.chat.id)[0][1] + ','+ ' это вы?',  reply_markup=yes_no())
        bot.register_next_step_handler(message, state_for_check)

def state_for_name(message): ## состояние для ввода имени
    name = str(message.text).split(' ')
    chat_id = message.chat.id
    print(name)
    a = find_in_cpp(int(message.chat.id))
    b = find_in_java(int(message.chat.id))
    c = find_in_python(int(message.chat.id))
    d = find_in_sql(int(message.chat.id))

    
    date = datetime.datetime.now() + datetime.timedelta(days=21)
    if course_name == 'Java':

        if b is False:
            add_to_java(chat_id, date)
        else:
            dt = datetime.datetime.fromisoformat(find_in_python(message.chat.id)[0][0]) - datetime.datetime.now()
            bot.send_message(message.chat.id, 'Вы уже записаны на это курс\n'
                                              'Осталось {} дней и {} часов'.format(dt.days, dt.seconds//3600))
            bot.send_message(message.chat.id, 'У вас {} баллов по данному предмету'.format(get_scores_java(chat_id)[0][0]))

    if course_name == 'Python':
        if c is False:
            add_to_python(chat_id, date)
        else:
            dt = datetime.datetime.fromisoformat(find_in_python(message.chat.id)[0][0]) - datetime.datetime.now()
            bot.send_message(message.chat.id, 'Вы уже записаны на это курс\n'
                                              'Осталось {} дней и {} часов'.format(dt.days, dt.seconds // 3600))
            bot.send_message(message.chat.id, 'У вас {} баллов по данному предмету'.format(get_scores_java(chat_id)[0][0]))


    if course_name == 'C++':
        if a is False:
            add_to_cpp(chat_id, date)
        else:
            dt = datetime.datetime.fromisoformat(find_in_python(message.chat.id)[0][0]) - datetime.datetime.now()
            bot.send_message(message.chat.id, 'Вы уже записаны на это курс\n'
                                              'Осталось {} дней и {} часов'.format(dt.days, dt.seconds // 3600))
            bot.send_message(message.chat.id, 'У вас {} баллов по данному предмету'.format(get_scores_cpp(chat_id)[0][0]))


    if course_name == 'SQL':
        if d is False:
            add_to_sql(chat_id, date)
        else:
            dt = datetime.datetime.fromisoformat(find_in_python(message.chat.id)[0][0]) - datetime.datetime.now()
            bot.send_message(message.chat.id, 'Вы уже записаны на это курс\n'
                                              'Осталось {} дней и {} часов'.format(dt.days, dt.seconds // 3600))
            bot.send_message(message.chat.id, 'У вас {} баллов по данному предмету'.format(get_scores_sql(chat_id)[0][0]))

    if a == b == c == d == False:
        add_to_students_table(message.chat.id, name[1], name[0], name[2])
    bot.send_message(message.chat.id, name)

def state_for_check(message):
    a = find_in_cpp(int(message.chat.id))
    b = find_in_java(int(message.chat.id))
    c = find_in_python(int(message.chat.id))
    d = find_in_sql(int(message.chat.id))
    chat_id = message.chat.id
    
    date = datetime.datetime.now() + datetime.timedelta(days=21)
    if course_name == 'Java':
        if b is False:
            add_to_java(chat_id, date)
        else:
            dt = datetime.datetime.fromisoformat(find_in_python(message.chat.id)[0][0]) - datetime.datetime.now()
            bot.send_message(message.chat.id, 'Вы уже записаны на это курс\n'
                                              'Осталось {} дней и {} часов'.format(dt.days, dt.seconds // 3600))
            bot.send_message(message.chat.id, 'У вас {} баллов по данному предмету'.format(get_scores_java(chat_id)[0][0]))


    if course_name == 'Python':
        if c is False:
            add_to_python(chat_id, date)
        else:
            dt = datetime.datetime.fromisoformat(find_in_python(message.chat.id)[0][0]) - datetime.datetime.now()
            bot.send_message(message.chat.id, 'Вы уже записаны на это курс\n'
                                              'Осталось {} дней и {} часов'.format(dt.days, dt.seconds // 3600))
            bot.send_message(message.chat.id, 'У вас {} баллов по данному предмету'.format(get_scores_java(chat_id)[0][0]))


    if course_name == 'C++':
        if a is False:
            add_to_cpp(chat_id, date)
        else:
            dt = datetime.datetime.fromisoformat(find_in_python(message.chat.id)[0][0]) - datetime.datetime.now()
            bot.send_message(message.chat.id, 'Вы уже записаны на это курс\n'
                                              'Осталось {} дней и {} часов'.format(dt.days, dt.seconds // 3600))
            bot.send_message(message.chat.id, 'У вас {} баллов по данному предмету'.format(get_scores_cpp(chat_id)[0][0]))


    if course_name == 'SQL':
        if d is False:
            add_to_sql(chat_id, date)
        else:
            dt = datetime.datetime.fromisoformat(find_in_python(message.chat.id)[0][0]) - datetime.datetime.now()
            bot.send_message(message.chat.id, 'Вы уже записаны на это курс\n'
                                              'Осталось {} дней и {} часов'.format(dt.days, dt.seconds // 3600))
            bot.send_message(message.chat.id, 'У вас {} баллов по данному предмету'.format(get_scores_sql(chat_id)[0][0]))

def state_for_teacher(message):
    global login
    login = message.text
    bot.send_message(message.chat.id, 'Введите пароль: ')
    bot.register_next_step_handler(message, state_for_teacher1)
def state_for_teacher1(message):
    global password
    password = message.text
    if (login, password) in teachers_date.items():
        if login == 'teacher1':
            bot.send_message(message.chat.id, 'Вы преподаватель в курсе Java', reply_markup=teachers_keyb())
            bot.send_message(message.chat.id, 'Выберите действие: ')
            bot.register_next_step_handler(message, state_for_java_teacher,)
        if login == 'teacher2':
            bot.send_message(message.chat.id, 'Вы преподаватель в группе Python', reply_markup=teachers_keyb())
            bot.send_message(message.chat.id, 'Выберите действие: ')
            bot.register_next_step_handler(message, state_for_python_teacher)
        if login == 'teacher3':
            bot.send_message(message.chat.id, 'Вы преподаватель в группе C++', reply_markup=teachers_keyb())
            bot.send_message(message.chat.id, 'Выберите действие: ')
            bot.register_next_step_handler(message, state_for_cpp_teacher)
        if login == 'teacher4':
            bot.send_message(message.chat.id, 'Вы преподаватель в группе SQl', reply_markup=teachers_keyb())
            bot.send_message(message.chat.id, 'Выберите действие: ')
            bot.register_next_step_handler(message, state_for_sql_teacher)
    else:
        bot.send_message(message.chat.id, 'Вы ввели неправильно логин или пароль\n'
                                          'Попробуйте снова')
        bot.send_message(message.chat.id, 'Введите логин')
        bot.register_next_step_handler(message, state_for_teacher)

def state_for_java_teacher(message):
    students_chat_ids = ids_java()
    chat_id = message.chat.id
    if message.text == 'Получить список студентов':
        for i in students_chat_ids:
            bot.send_message(message.chat.id, str(get_name(i[0])[0][0]) + ' ' +
                             str(get_name(i[0])[0][1]) + ' ' + str(get_name(i[0])[0][2]))
    elif message.text == 'Прикрепить задание для всех студентов':
        bot.send_message(chat_id,'Напишите задание или загрузите документ')
        bot.register_next_step_handler(message, state_for_java_document)
    elif message.text == 'Начать занятие':
        bot.send_message(message.chat.id, 'Занятие началось!')
        sleep(1)
        bot.send_message(message.chat.id, 'Ниже будет представлено список студентов\n'
                                          'Оцените их работа на семинаре по 10-и бальной шкале'
                                          'Если студент отсутствует, то так же отметьте это')
        sleep(1)
        global spisok_of_scores
        spisok_of_scores = []
        for i in students_chat_ids:
            bot.send_message(message.chat.id, str(get_name(i[0])[0][0])+' '+
                             str(get_name(i[0])[0][1])+' ' + str(get_name(i[0])[0][2]), reply_markup=scores_keyb())
def state_for_java_document(message):
    try:
        message.document.file_id
        for i in ids_java():
            bot.send_document(i[0], message.document.file_id)
        bot.send_message(message.chat.id, 'ДЗ отправлено всем студентам данной группы')
    except AttributeError:
        for i in ids_java():
            bot.send_message(i[0], message.text)

def state_for_python_teacher(message):
    chat_id = message.chat.id
    students_chat_ids = ids_python()
    if message.text == 'Получить список студентов':
        for i in students_chat_ids:
            bot.send_message(message.chat.id, str(get_name(i[0])[0][0]) + ' ' +
                             str(get_name(i[0])[0][1]) + ' ' + str(get_name(i[0])[0][2]))
    elif message.text == 'Прикрепить задание для всех студентов':
        bot.send_message(chat_id, 'Напишите задание или загрузите документ')
        bot.register_next_step_handler(message, state_for_python_document)
    elif message.text == 'Начать занятие':
        bot.send_message(message.chat.id, 'Занятие началось!')
        sleep(1)
        bot.send_message(message.chat.id, 'Ниже будет представлено список студентов\n'
                                          'Оцените их работа на семинаре по 10-и бальной шкале'
                                          'Если студент отсутствует, то так же отметьте это')
        sleep(1)
        for i in students_chat_ids:
            bot.send_message(message.chat.id, str(get_name(i[0])[0][0]) + ' ' +
                             str(get_name(i[0])[0][1]) + ' ' + str(get_name(i[0])[0][2]), reply_markup=scores_keyb())
def state_for_python_document(message):
    try:
        message.document.file_id
        for i in ids_python():
            bot.send_document(i[0], message.document.file_id)
        bot.send_message(message.chat.id, 'ДЗ отправлено всем студентам данной группы')
    except AttributeError:
        for i in ids_python():
            bot.send_message(i[0], message.text)
def state_for_cpp_teacher(message):
    chat_id = message.chat.id
    students_chat_ids = ids_cpp()
    if message.text == 'Получить список студентов':
        for i in students_chat_ids:
            bot.send_message(message.chat.id, str(get_name(i[0])[0][0]) + ' ' +
                             str(get_name(i[0])[0][1]) + ' ' + str(get_name(i[0])[0][2]))
    elif message.text == 'Прикрепить задание для всех студентов':
        bot.send_message(chat_id, 'Напишите задание или загрузите документ')
        bot.register_next_step_handler(message, state_for_cpp_document)
    elif message.text == 'Начать занятие':
        bot.send_message(message.chat.id, 'Занятие началось!')
        sleep(1)
        bot.send_message(message.chat.id, 'Ниже будет представлено список студентов\n'
                                          'Оцените их работа на семинаре по 10-и бальной шкале'
                                          'Если студент отсутствует, то так же отметьте это')
        sleep(1)
        for i in students_chat_ids:
            bot.send_message(message.chat.id, str(get_name(i[0])[0][0]) + ' ' +
                             str(get_name(i[0])[0][1]) + ' ' + str(get_name(i[0])[0][2]), reply_markup=scores_keyb())
def state_for_cpp_document(message):
    try:
        message.document.file_id
        for i in ids_cpp():
            bot.send_document(i[0], message.document.file_id)
        bot.send_message(message.chat.id, 'ДЗ отправлено всем студентам данной группы')
    except AttributeError:
        for i in ids_cpp():
            bot.send_message(i[0], message.text)
def state_for_sql_teacher(message):
    chat_id = message.chat.id
    students_chat_ids = ids_sql()
    if message.text == 'Получить список студентов':
        for i in students_chat_ids:
            bot.send_message(message.chat.id, str(get_name(i[0])[0][0]) + ' ' +
                             str(get_name(i[0])[0][1]) + ' ' + str(get_name(i[0])[0][2]))
    elif message.text == 'Прикрепить задание для всех студентов':
        bot.send_message(chat_id, 'Напишите задание или загрузите документ')
        bot.register_next_step_handler(message, state_for_sql_document)
    elif message.text == 'Начать занятие':
        bot.send_message(message.chat.id, 'Занятие началось!')
        sleep(1)
        bot.send_message(message.chat.id, 'Ниже будет представлено список студентов\n'
                                          'Оцените их работа на семинаре по 10-и бальной шкале\n'
                                          'Если студент отсутствует, то так же отметьте это')
        sleep(1)
        for i in students_chat_ids:
            bot.send_message(message.chat.id, str(get_name(i[0])[0][0]) + ' ' +
                             str(get_name(i[0])[0][1]) + ' ' + str(get_name(i[0])[0][2]), reply_markup=scores_keyb())
def state_for_sql_document(message):
    try:
        message.document.file_id
        for i in ids_sql():
            bot.send_document(i[0], message.document.file_id)
        bot.send_message(message.chat.id, 'ДЗ отправлено всем студентам данной группы')
    except AttributeError:
        for i in ids_sql():
            bot.send_message(i[0], message.text)


bot.polling()
