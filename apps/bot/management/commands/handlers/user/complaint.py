from telebot import TeleBot
from telebot.types import CallbackQuery, Message
from ...bot import bot
from ...keyboards import button, markup, back



@bot.message_handler(func=lambda msg: msg.text == "Taklif va shikoyatlar📝")
def back_handler(msg:Message):
    user_id = msg.chat.id
    bot.send_message(user_id, "Fikringizni qoldiring",reply_markup=button)

@bot.message_handler(func=lambda msg: msg.text == "Taklif bildirish🖌")
def back_handler(msg:Message):
    user_id = msg.chat.id
    bot.send_message(user_id, "xabarni yuboring", reply_markup=back)


@bot.message_handler(func=lambda msg: msg.text == "Shikoyat qilish🖍")
def back_handler(msg:Message):
    user_id = msg.chat.id
    bot.send_message(user_id, "xabarni yuboring", reply_markup=back)