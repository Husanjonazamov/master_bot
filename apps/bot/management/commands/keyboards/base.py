from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

vhome = ReplyKeyboardMarkup(resize_keyboard=True)
vhome.add(KeyboardButton("Qo'shish ➕"))
vhome.add(KeyboardButton("Statistics 📊"))
vhome.add(KeyboardButton("Accountdan chiqish 🚫"))
vhome.add(KeyboardButton("🔙Ortga"))

bhome = ReplyKeyboardMarkup(resize_keyboard=True)
bhome.add(KeyboardButton("Bekor qilish ❌"))

send_location = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
send_location.add(KeyboardButton("Joylashuvni yuborish", request_location=True))
send_location.add(KeyboardButton("Bekor qilish ❌"))

back = ReplyKeyboardMarkup(resize_keyboard=True)
back.add(KeyboardButton("🔙Ortga"))

markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
markup.add(KeyboardButton("Buyurtma berish🛒"))
markup.add(KeyboardButton("Yetkazib beruvchi🚚"))
markup.add(KeyboardButton("Veterenariya🚑"))

button_phone = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
button_phone.add(KeyboardButton("Telefon raqamni yuborish", request_contact=True))

btn1 = KeyboardButton("Taklif va shikoyatlar📝")
markup.row(btn1)

button = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
button1 = KeyboardButton("Taklif bildirish🖌")
button2 = KeyboardButton("Shikoyat qilish🖍")
button.row(button1,button2)

send_delivered = ReplyKeyboardMarkup(resize_keyboard=True)
send_delivered.add(KeyboardButton("Ro`yxatdan o`tish📝"))

