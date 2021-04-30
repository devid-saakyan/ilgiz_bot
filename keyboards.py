from telebot import types

def courses_name():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Python')
    btn2 = types.KeyboardButton('Java')
    btn3 = types.KeyboardButton('SQL')
    btn4 = types.KeyboardButton('C++')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    return markup

def teachers_keyb():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Получить список студентов')
    btn2 = types.KeyboardButton('Прикрепить задание для всех студентов')
    btn3 = types.KeyboardButton('Начать занятие')
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    return markup

def scores_keyb():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('1')
    btn2 = types.KeyboardButton('2')
    btn3 = types.KeyboardButton('3')
    btn4 = types.KeyboardButton('4')
    btn5 = types.KeyboardButton('5')
    btn6 = types.KeyboardButton('6')
    btn7 = types.KeyboardButton('7')
    btn8 = types.KeyboardButton('8')
    btn9 = types.KeyboardButton('9')
    btn10 = types.KeyboardButton('10')
    btn11 = types.KeyboardButton('Отсутствует')
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7, btn8, btn9, btn10, btn11)
    return markup

def yes_no():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Да')
    btn2 = types.KeyboardButton('Нет')
    markup.add(btn1, btn2)
    return markup