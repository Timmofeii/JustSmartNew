import random
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from bot_token import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message, "I can help you with..")


# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Створення клавіатури
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button3 = KeyboardButton("Отримати матиматичну задачу")
    button4 = KeyboardButton("Що ти можеш?")
    keyboard.add(button3, button4)

    # Надсилання повідомлення з кнопками
    bot.send_message(message.chat.id, "Привіт! Обери опцію:", reply_markup=keyboard)

@bot.message_handler(func=lambda message:message.text=="Привіт")
def hello(message):
    bot.send_message(message.chat.id,"Привіт, чим можу допомогти!")

@bot.message_handler(func=lambda message: True)
def handle_button(message):
    if message.text == "Отримати матиматичну задачу":
        bot.send_message(message.chat.id, f"{random.randint(0, 10)} + {random.randint(0, 10)}")
    elif message.text == "Що ти можеш?":
        bot.send_message(message.chat.id, "Давай почнемо! Що тебе цікавить?")
    else:
        bot.send_message(message.chat.id, "Невідома команда, спробуй настиснути кнопку /help")


# Запуск бота
bot.polling()
