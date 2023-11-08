from telebot import TeleBot
from telebot.types import Message

bot = TeleBot("6418058572:AAFYnF5cb9tZyqSUE3USsKHLO7TiybwUGCM")


@bot.message_handler(commands=['start'])
def handler(msg: Message):
    print(msg)


@bot.message_handler(content_types=['photo', 'voice'])
def handle_docs_audio(message):
    print(message)


bot.polling()
