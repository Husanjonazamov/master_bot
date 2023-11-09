import os
from django.db import models
from django.conf import settings
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    CallbackQuery, ReplyKeyboardRemove

from apps.api.models import Veterinarian, Delivered, Location, Placing, Registration
from ...bot import bot
from ...keyboards import vhome, bhome, button, markup, send_delivered, back, button_phone
from ...utils.state import State
from ...utils.user import User as BUser
# from apps.bot.models import User
from apps.accounts.models import User
from ...filters.state import Filter
from django.contrib.auth import authenticate



@bot.message_handler(commands=['start'])
def start_handler(msg: Message):
    user_id = msg.chat.id
    bot.send_message(user_id,
                         "Assalomu alaykum Inter broiler botimizga xush kelibsiz.",
                         reply_markup=markup)



@bot.message_handler(func=Filter(text="🔙Ortga"))
def back_handler(msg: Message):
    user_id = msg.chat.id
    State.set_state(user_id, "home")
    bot.send_message(user_id, "Assalomu alaykum Inter broiler botimizga xush kelibsiz.", reply_markup=markup)


@bot.message_handler(content_types=['location'])
def location(msg: Message):
    user_id = msg.chat.id
    state = State.get_state(user_id)

    if state == "sendl1":
        State.set_data(user_id, "sendl1", msg.location)
        State.set_state(user_id, "sendnk1")
        bot.send_message(user_id, "Jo'ja necha kunlik")
    elif state == "sendl2":
        State.set_data(user_id, "sendl2", msg.location)
        State.set_state(user_id, "sendc2")
        bot.send_message(user_id, "Nechta jo`ja olib bordingiz")

    elif state == "location":
        State.set_data(user_id, "location", msg.location)
        bot.send_message(user_id, "Buyurtmangiz qabul qilndi ✅", reply_markup=markup)
        State.set_state(user_id, "home")

@bot.message_handler(content_types=['contact'])
def Phone(msg: Message):
    user_id = msg.chat.id
    state = State.get_state(user_id)

    if state == "phone":
        State.set_data(user_id, "phone", msg.contact)
        State.set_state(user_id, "day")
        bot.send_message(user_id, "Qaysi kunga jo`ja kerak")
    elif state == "number":
        State.set_data(user_id, "number", msg.contact)
        bot.send_message(user_id, "Siz ro'yhatdan o'tdingiz ✅", reply_markup=markup)
        State.set_state(user_id, "home")


@bot.message_handler(content_types=["photo", "video"])
def handler(msg: Message):
    user_id = msg.chat.id
    user = BUser.get_user(user_id)
    state = State.get_state(user_id)
    content_type = msg.content_type

    ext = "jpg"
    file_id = ""
    if content_type == "video":
        file_id = msg.video.file_id

        ext = "mp3"
    elif content_type == "photo":
        file_id = msg.photo[-1].file_id

        ext = "jpg"

    file_info = bot.get_file(file_id)
    file = bot.download_file(file_info.file_path)
    file_name = "{}_{}.{}".format(user_id, file_id, ext)
    file_path = os.path.join(settings.MEDIA_ROOT, 'additions', file_name)

    with open(file_path, 'wb') as new_file:
        new_file.write(file)

    if state == "sendqx1":
        name = State.get_data(user_id, "sendf1")
        phone = State.get_data(user_id, "sendp1")
        location = State.get_data(user_id, "sendl1")
        nday = State.get_data(user_id, "sendnk1")
        namlik = State.get_data(user_id, "sendn1")
        temprature = State.get_data(user_id, "sendt1")
        Tashxis = State.get_data(user_id, "sendg1")
        xulosa = State.get_data(user_id, "sendx1")

        loc = Location()
        loc.lat = location.latitude
        loc.lon = location.longitude
        loc.save()
        
        user = User.objects.all().first()
        # print(user)
        newVeterinar = Veterinarian.objects.create (
            user = user,
            first_name = name,
            phone = phone,
            location = loc,
            day = nday,
            moisture = namlik,
            temperature = temprature,
            diagnosis = Tashxis,
            conclusion = xulosa,
            addition = "{}{}".format('additions/', file_name)
        )

        newVeterinar.save()
        bot.send_message(user_id, "Muvofaqiyyatli qo'shildi ✅", reply_markup=markup)
        State.set_state(user_id, "home")


    elif state == "sendqx2":
        name = State.get_data(user_id, "sendf2")
        phone = State.get_data(user_id, "sendp2")
        location = State.get_data(user_id, "sendl2")
        count = State.get_data(user_id, "sendc2")


        loc = Location()
        loc.lat = location.latitude
        loc.lon = location.longitude
        loc.save()
        


        user = User.objects.all().first()
        # user = User.objects.create()

        print(user)

        newDelever = Delivered.objects.create (
               user = user,
               first_name = name,
               phone = phone,
               location = loc,
               product_count = count,
               addition = "{}{}".format('additions/', file_name)
        )
        newDelever.save()
        bot.send_message(user_id, "Muvofaqiyyatli qo'shildi ✅", reply_markup=markup)
        State.set_state(user_id, "home")

    elif state == "first_name":
        name = State.get_data(user_id, "first_name")
        phone = State.get_data(user_id, "phone")
        day = State.get_data(user_id, "day")
        product_count = State.get_data(user_id, "count")
        location = State.get_data(user_id, "location")

        loc = Location()
        loc.lat = location.latitude
        loc.lon = location.longitude
        loc.save()

        p = Placing()
        p.user_id = user_id
        p.user = user.profile
        p.name = name
        p.phone = phone
        p.day = day
        p.product_count = product_count
        p.location = location
        p.addition = "{}{}".format('additions/', file_name)
        p.save()

        bot.send_message(user_id, "Buyurtmangiz qabul qilndi ✅", reply_markup=markup)
        State.set_state(user_id, "home")


    elif state == "name":
        name = State.get_data(user_id, "name")
        number = State.get_data(user_id, "number")

        r = Registration()
        r.user_id = user_id
        r.user = user.profile
        r.name = name
        r.phone = number
        r.save()



