from pprint import pprint

from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    CallbackQuery, ReplyKeyboardRemove

from ...bot import bot
from ...filters import Filter
from ...keyboards import send_location, vhome, send_delivered, bhome
from ...utils.state import State
from ...utils.user import User as BUser
from apps.bot.models import User
from django.contrib.auth import authenticate



@bot.message_handler(func=lambda msg: msg.text == "Veterenariya🚑")
def back_handler(msg: Message):
    user_id = msg.chat.id
    keyboard = ReplyKeyboardRemove()
    check = User.objects.filter(user_id=user_id)
    State.set_state(user_id, "home")
    if not check.exists() or check.first().is_login == False:

        if not check.exists():
            User.objects.create(user_id=user_id)

        State.set_state(user_id, "login")
        bot.send_message(user_id,
                         "Siz Veterenariya sifatida ro'yhatdan o`tmagansiz",
                         reply_markup=send_delivered)
    else:
        user_id = msg.chat.id
        user = BUser.get_user(user_id)
        role = user.profile

        bot.send_message(user_id, "Mijozning ismini kiriting", reply_markup=bhome)
        State.set_state(user_id, "sendf1")


@bot.message_handler(func=Filter(state="sendf1"))
def handler(msg: Message):
    user_id = msg.chat.id
    State.set_data(user_id, "sendf1", msg.text)
    State.set_state(user_id, "sendp1")
    bot.send_message(user_id, "Mijozning telefon raqamini kiriting\nMisol: 940014741")


@bot.message_handler(func=Filter(state="sendp1"))
def handler(msg: Message):
    user_id = msg.chat.id
    text = msg.text

    if len(text) != 9 or not text.isdigit():
        return bot.send_message(user_id, "Telefon nomer xato kiritildi\n\nMisol: 940014741")

    State.set_data(user_id, "sendp1", msg.text)
    State.set_state(user_id, "sendl1")
    bot.send_message(user_id, "Manzilni yuboring\npastdagi *Joylashuvni yuborish* tugmasini bosing",
                     reply_markup=send_location, parse_mode="markdown")



@bot.message_handler(func=Filter(state="sendnk1"))
def handler(msg: Message):
    user_id = msg.chat.id
    text = msg.text
    if not text.isdigit():
        return bot.send_message(user_id, "kun xato kiritildi\n\nMisol: 10,20,30")

    State.set_data(user_id, "sendnk1", text)
    State.set_state(user_id, "sendn1")
    bot.send_message(user_id, "Jo`jaxona namligi")


@bot.message_handler(func=Filter(state="sendn1"))
def handler(msg: Message):
    user_id = msg.chat.id
    text = msg.text
    if not text.isdigit():
        return bot.send_message(user_id, "Namlik xato kiritildi\n\nMisol: 10,20,30")

    State.set_data(user_id, "namlik", text)
    State.set_state(user_id, "sendt1")
    bot.send_message(user_id, "Jo`jaxona temperaturasi")


@bot.message_handler(func=Filter(state="sendt1"))
def handler(msg: Message):
    user_id = msg.chat.id
    text = msg.text
    if not text.isdigit():
        return bot.send_message(user_id, "Temperatura xato kiritildi\n\nMisol: 1,4,50")

    State.set_data(user_id, "sendt1", text)
    State.set_state(user_id, "sendx1")
    bot.send_message(user_id, "Nima kasallik bilan kasallangan ")

@bot.message_handler(func=Filter(state="sendnk1"))
def handler(msg: Message):
    user_id = msg.chat.id
    text = msg.text

    State.set_data(user_id, "sendnk1", text)
    State.set_state(user_id, "sendx1")
    bot.send_message(user_id, "Nima kasallik bilan kasallangan ")

@bot.message_handler(func=Filter(state="sendx1"))
def handler(msg: Message):
    user_id = msg.chat.id

    text = msg.text
    State.set_data(user_id, "sendx1", text)
    State.set_state(user_id, "sendqx1")
    bot.send_message(user_id, "Jo`ja xonani (rasm va videoga) olib yuboring 20 mb dan oshmasin")