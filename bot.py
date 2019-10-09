from glob import glob
import logging
import ssl

from random import choice
from utils import get_keyboard, get_user_emo

from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler, Filters
from handlers import *
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
ssl._create_default_https_context = ssl._create_unverified_context

def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text('Готово: {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())

def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text('Готово: {}'.format(get_user_emo(user_data)), reply_markup=get_keyboard())

def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id = update.message.chat_id, photo = open(cat_pic, 'rb'), reply_markup=get_keyboard())

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Бот запускается.')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('cat', send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Прислать котика)$', send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Сменить аватарку)$', change_avatar, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.photo, check_user_photo, pass_user_data=True))

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()