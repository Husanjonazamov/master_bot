from pprint import pprint

from telebot.types import Message
from ...utils.user import User as BUser
from ...bot import bot
from ...filters import Filter
from ...keyboards import send_location, vhome, button_phone, bhome, back
from ...utils import State



@bot.message_handler(func=Filter(text="Buyurtma berish🛒"))
def add_handler(msg: Message):
    user_id = msg.chat.id
    user = BUser.get_user(user_id)
    role = user.profile.role

    bot.send_message(user_id, "Ism kiriting", reply_markup=back)



@bot.message_handler(func=Filter(state="first_name"))
def handler(msg: Message):
    user_id = msg.chat.id
    State.set_data(user_id, "first_name", msg.text)
    State.set_state(user_id, "phone")
    bot.send_message(user_id, "Telefon nomerni kiriting\npastdagi Telefon raqamni yuborish tugmasini bosing",
                     reply_markup=button_phone, parse_mode="markdown")



@bot.message_handler(func=Filter(state="phone"))
def handler(msg: Message):
    user_id = msg.chat.id
    text = msg.text
    if len(text) != 9 or not text.isdigit():
        return bot.send_message(user_id, "Telefon nomer xato kiritildi\n\nPastdagi tugmani bosing")

    State.set_data(user_id, "phone", msg.text)
    State.set_state(user_id, "day")
    bot.send_message(user_id, "Qaysi kunga jo`ja kerak")



@bot.message_handler(func=Filter(state="day"))
def handler(msg: Message):
    user_id = msg.chat.id
    text = msg.text

    State.set_data(user_id, "day", text)
    State.set_state(user_id, "product_count")
    bot.send_message(user_id, "Qancha miqdorda jo`ja kerak(son ko`rinishida )")


@bot.message_handler(func=Filter(state="product_count"))
def handler(msg: Message):
    user_id = msg.chat.id
    text = msg.text
    if not text.isdigit():
        return bot.send_message(user_id, "Miqdori xato kiritildi\n\nMisol: 10,20,30")

    State.set_data(user_id, "count", text)
    State.set_state(user_id, "location")
    bot.send_message(user_id, "Manzilni yuboring\n\npastdagi *Joylashuvni yuborish* tugmasini bosing",
                     reply_markup=send_location, parse_mode="markdown")

@bot.message_handler(func=Filter(state="location"))
def handler(msg: Message):
    user_id = msg.chat.id
    text = msg.text
    if not text.isdigit():
        return bot.send_message(user_id, "Location xato kiritildi\n\npastdagi tugmani bosing")




