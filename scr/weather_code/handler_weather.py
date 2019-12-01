from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import (CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler, CallbackContext)
from scr.weather_code.api_for_weather import request_current_weather, request_forecast

LOCATION, CITY = range(2)

CALLBACK_BUTTON1_YES = "Yes"
CALLBACK_BUTTON2_NO = "No"

TITLES = {
    CALLBACK_BUTTON1_YES: "Yes 🆗",
    CALLBACK_BUTTON2_NO: "No  🙅‍♂ "
}


def get_place_keyboard():
    keyboard = \
        [
            [
                InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_YES], callback_data=CALLBACK_BUTTON1_YES),
                InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_NO], callback_data=CALLBACK_BUTTON2_NO),
            ],
        ]
    return InlineKeyboardMarkup(keyboard)


def do_start_weather(update: Update, context):
    update.message.reply_text(
        text="Send name of city or u location"
    )
    return LOCATION


def do_location(update: Update, context):
    print("hi")
    longitude, latitude = update.message.location.longitude, update.message.location.latitude
    print("das")
    context.user_data['city'] = ''
    context.user_data['longitude'] = longitude
    context.user_data['latitude'] = latitude
    print("hi")
    answer = request_current_weather(lon=longitude, lat=latitude)
    update.message.reply_text(text=answer,
                              reply_markup=get_place_keyboard())


def do_city(update: Update, context):
    city = update.message.text
    print("hi")
    context.user_data['city'] = city
    print(context.user_data.get('city'))
    answer = request_current_weather(city_name=city)
    update.message.reply_text(text=answer)
    update.message.reply_text(text="Do you want to know weather in"+ context.user_data.get('city') + " more DETAIL",
                              reply_markup=get_place_keyboard())


def do_done(update: Update, context):
    i = 0
    chat_id = update.effective_message.chat_id
    print("fds")
    if (update.callback_query.data == 'Yes'):
        if context.user_data.get('city') == '' or context.user_data.get('city') is None:
            answer = request_forecast(lon=context.user_data['longitude'],
                             lat=context.user_data['latitude'])
            context.bot.send_message(chat_id=chat_id,text=answer)
        else:
            answer = request_forecast(city_name=context.user_data.get('city'))
            print("ese",type(answer))
            context.bot.send_message(chat_id=chat_id,text=answer)
    else:
        context.bot.send_message(chat_id=chat_id,text="Okay. Bay")
    return ConversationHandler.END


def weather_handler():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('weather', do_start_weather)],
        states={
            LOCATION: [MessageHandler(Filters.location, do_location),
                       MessageHandler(Filters.text, do_city)]
        },
        fallbacks=[CallbackQueryHandler(do_done)]
    )
    return conv_handler
