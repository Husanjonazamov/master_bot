from telebot import TeleBot
from utils.env import env

state ={}
data_state = {}

bot = TeleBot(env.str("BOT_TOKEN"))
