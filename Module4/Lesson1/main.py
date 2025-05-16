import random
import telebot
from bot_token import Bot_TOKEN
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot(Bot_TOKEN)
jokes = [1,2,3,4,5]


bot = telebot.TeleBot(TOKEN)

string_tell_a_joke = "tell a joke"
# Команда /start: відправляє привітання, коли користувач пише /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я твій новий бот 😃")
    keyboard = ReplyKeyboardMarkup(resize_keyboard = True)
    button1 = KeyboardButton(string_tell_a_joke)
    button2 = KeyboardButton("hello")
    keyboard.add(button1, button2)
    bot.send_message(
message.chat.id
, "tell me a joke hello:",reply_markup= keyboard)
# Команда /help: відправляє повідомлення з підказками
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я можу допомогти тобі з основними командами: /start, /help,/joke")
# Запуск бота
@bot.message_handler(func= lambda message: True)
def send_joke(message):
    bot.reply_to(message, choice(jokes))
def handle_button(message):
    if message.text == string_tell_a_joke:
        bot.send_message(message.chat.id, choice([1,2,3,4]))
    elif message.text == "help":
        bot.send_message(message.chat.id, "Я можу допомогти тобі з основними командами")
bot.polling()








# # Команда /start
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# # Створення клавіатури
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = KeyboardButton("Привіт")
#     button2 = KeyboardButton("Почати")
#     keyboard.add(button1, button2)
#
#     # Надсилання повідомлення з кнопками
#     bot.send_message(message.chat.id, "Привіт! Обери опцію:", reply_markup=keyboard)
#
# # Обробка текстових повідомлень (реакція на кнопки)
# @bot.message_handler(func=lambda message: True)
# def handle_buttons(message):
#     if message.text == "Привіт":
#         bot.send_message(message.chat.id, "Привіт! Як у тебе справи?")
#     elif message.text == "Почати":
#         bot.send_message(message.chat.id, "Давай почнемо! Що саме тебе цікавить?")
#     else:
#         bot.send_message(message.chat.id, "Я не знаю такої команди, спробуй натиснути на кнопку 😊")
#



bot.polling()

# Запуск бота


# @bot.message_handler(commands=["start"])
# def send_welcome(message):
#     bot.reply_to(message,'Hi, i`m bot')
#
# @bot.message_handler(commands=["help"])
# def send_help(message):
#     bot.reply_to(message,"I can help you with..")
#
#
# @bot.message_handler(commands=["random"])
# def get_random(message):
#     bot.reply_to(message,random.randint(0,10))
#
# @bot.message_handler(commands=["math"])
# def get_math(message):
#     bot.reply_to(message, f"{random.randint(0, 10)} + {random.randint(0, 10)}")
# bot.polling()

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = 'ТВІЙ ТОКЕН'
bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
# Створення клавіатури
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton("Привіт")
button2 = KeyboardButton("Почати")
keyboard.add(button1, button2)

# Надсилання повідомлення з кнопками
bot.send_message(message.chat.id, "Привіт! Обери опцію:", reply_markup=keyboard)

# Обробка текстових повідомлень (реакція на кнопки)
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
if message.text == "Привіт":
bot.send_message(message.chat.id, "Привіт! Як у тебе справи?")
elif message.text == "Почати":
bot.send_message(message.chat.id, "Давай почнемо! Що саме тебе цікавить?")
else:
bot.send_message(message.chat.id, "Я не знаю такої команди, спробуй натиснути на кнопку 😊")

# Запуск бота
bot.polling()
