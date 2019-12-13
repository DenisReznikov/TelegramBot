from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler
from scr.handlers.handler_eat import eat_handler
from scr.handlers.handler_weather import weather_handler
from scr.handlers.avito_handler import avito_handler
import os
from scr.other.logger import debug_requests

@debug_requests
def do_start(update: Update, context):
    # TODO: перенести клавву в другой класс
    location_keyboard = [[KeyboardButton("Send location", request_location=True), ], ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=location_keyboard,
        resize_keyboard=True,
    )

    answer = "Привет, *" + update.message.from_user.first_name + "* " + \
             "\n Я твой помощник." \
             "Если ты хочешь *пить* или есть нажми -> /eat \n" \
             " \n"\
             "Что-бы - /weather" \
             "or if you want I can find something on the avito  tap on - /avito" \

    update.message.reply_text(text=answer, reply_markup=keyboard)



def main():
    TOKEN =  ['TELEGRAM_TOKEN']
    updater = Updater("790323839:AAGCpqOp4LXWd3O0DNYem32FyzF-32kRyGk", use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", do_start))
    updater.dispatcher.add_handler(eat_handler())
    updater.dispatcher.add_handler(weather_handler())
    updater.dispatcher.add_handler(avito_handler())
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
