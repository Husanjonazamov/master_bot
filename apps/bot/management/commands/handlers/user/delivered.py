from pprint import pprint

from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    CallbackQuery, ReplyKeyboardRemove

from ...bot import bot, state
from ...filters import Filter
from ...keyboards import send_location, send_delivered, vhome, bhome
from ...utils.state import State
from ...utils.user import User as BUser
from apps.bot.models import User
from django.contrib.auth import authenticate


@bot.message_handler(func=lambda msg: msg.text == "Yetkazib beruvchi🚚")
def back_handler(msg: Message):
    user_id = msg.chat.id
    keyboard = ReplyKeyboardRemove()
    user = BUser.get_user(user_id)
    check = User.objects.filter(user_id=user_id)
    State.set_state(user_id, "home")
    if not check.exists() or check.first().is_login == False:

        if not check.exists():
            User.objects.create(user_id=user_id)

        State.set_state(user_id, "login")
        bot.send_message(user_id,
                         "Siz yetkazib beruvchi sifatida ro'yhatdan o`tmagansiz",
                         reply_markup=send_delivered)
    else:
        user_id = msg.chat.id
        user = BUser.get_user(user_id)

        bot.send_message(user_id, "Mijozning ismini kiriting", reply_markup=bhome)
        State.set_state(user_id, "sendf2")

@bot.message_handler(func=Filter(state="sendf2"))
def handler(msg: Message):
    user_id = msg.chat.id
    State.set_data(user_id, "sendf2", msg.text)
    State.set_state(user_id, "sendp2")
    bot.send_message(user_id, "Mijozning telefon raqamini kiriting\n\nMisol: 943990509")


@bot.message_handler(func=Filter(state="sendp2"))
def handler(msg: Message):
    user_id = msg.chat.id
    text = msg.text

    if len(text) != 9 or not text.isdigit():
        return bot.send_message(user_id, "Telefon nomer xato kiritildi\n\nMisol: 943990509")

    State.set_data(user_id, "sendp2", msg.text)
    State.set_state(user_id, "sendl2")
    bot.send_message(user_id, "Manzilni yuboring\npastdagi *Joylashuvni yuborish* tugmasini bosing",
                     reply_markup=send_location, parse_mode="markdown")


@bot.message_handler(content_types=['location'])
def location(msg: Message):
    user_id = msg.chat.id
    state = State.get_state(user_id)

    if state != "sendl2":
        return

    State.set_data(user_id, "sendl2", msg.location)
    State.set_state(user_id, "sendc2")
    bot.send_message(user_id, "location")

@bot.message_handler(func=Filter(state="sendc2"))
def handler(msg: Message):
    user_id = msg.chat.id
    text = msg.text
    if not text.isdigit():
        return bot.send_message(user_id, "Jo'ja soni xato kiritildi\n\nMisol: 10,20,30")


    State.set_data(user_id, "sendc2", text)
    State.set_state(user_id, "sendqx2")
    bot.send_message(user_id, "Olib borgan jo`jalaringiz xolatini rasmga olib tashlang")

@bot.message_handler(func=Filter(state="sendqx2"))
def handler(msg: Message):
    user_id = msg.chat.id
    text = msg.text

    if state != "sendqx2":
        return

    State.set_data(user_id, "sendqx2", text)
    State.set_state(user_id, "sendqx2")
    bot.send_message(user_id, "Jo`ja olib borgan (jo`jaxona\nxolati qanday izoh qoldiring va\nrasmga olib tashlang) 20 mb dan oshmasin")



