from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler
from scr.eat_code.handler_eat import eat_handler
from scr.weather_code.handler_weather import weather_handler


def do_start(update: Update, context):
    # TODO: перенести клавву в другой класс
    location_keyboard = [[KeyboardButton("Send location", request_location=True), ], ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=location_keyboard,
        resize_keyboard=True,
    )
    answer = " Hello, " + update.message.from_user.first_name + \
             "\n I am u helper." \
             " If U want drink or eat, tap on - /eat \n" \
             "And I will show nearest the nearest bars or cafe or " \
             "restaurant "
    update.message.reply_text(text=answer, reply_markup=keyboard)


def main():
    updater = Updater("790323839:AAGCpqOp4LXWd3O0DNYem32FyzF-32kRyGk", use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", do_start))
    updater.dispatcher.add_handler(eat_handler())
    updater.dispatcher.add_handler(weather_handler())
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
