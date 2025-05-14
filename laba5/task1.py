import telebot
from telebot import types

bot = telebot.TeleBot('7381460574:AAFt3BAec1uWBO4bo-inexAzrLDYHC1TK4Y')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('➕ Сложение')
    btn2 = types.KeyboardButton('➖ Вычитание')
    btn3 = types.KeyboardButton('✖️ Умножение')
    btn4 = types.KeyboardButton('➗ Деление')
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, "Привет! Я бот-калькулятор. Выбери операцию:", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        if message.text in ['➕ Сложение', '➖ Вычитание', '✖️ Умножение', '➗ Деление']:
            msg = bot.send_message(message.chat.id, "Введи два числа через пробел (например: 5 3):")
            bot.register_next_step_handler(msg, process_numbers, message.text)
        else:
            result = eval(message.text)
            bot.send_message(message.chat.id, f"Результат: {result}")
    except:
        bot.send_message(message.chat.id, "Что-то пошло не так. Попробуй еще раз или выбери операцию из меню.")


def process_numbers(message, operation):
    try:
        a, b = map(float, message.text.split())

        if operation == '➕ Сложение':
            result = a + b
        elif operation == '➖ Вычитание':
            result = a - b
        elif operation == '✖️ Умножение':
            result = a * b
        elif operation == '➗ Деление':
            if b == 0:
                raise ZeroDivisionError
            result = a / b

        bot.send_message(message.chat.id, f"Результат: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Нужно ввести два числа через пробел!")
    except ZeroDivisionError:
        bot.send_message(message.chat.id, "На ноль делить нельзя!")
    except:
        bot.send_message(message.chat.id, "Что-то пошло не так. Попробуй еще раз.")

bot.polling(none_stop=True)