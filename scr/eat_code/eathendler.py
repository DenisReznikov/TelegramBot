from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import (CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler,CallbackContext)
from scr.eat_code.apiforeat import search
CHOOSING = range(1)

CALLBACK_BUTTON1_CAFE = "Кафе"
CALLBACK_BUTTON2_BAR = "Бар"
CALLBACK_BUTTON3_RESTAURANT = "Ресторан"

TITLES = {
    CALLBACK_BUTTON1_CAFE: "Cafe ☕ ",
    CALLBACK_BUTTON2_BAR: "Bar 🍺️ ",
    CALLBACK_BUTTON3_RESTAURANT: "Restaurant 🍽️",
}


def get_place_keyboard():
    keyboard = \
        [
            [
                InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_CAFE], callback_data=CALLBACK_BUTTON1_CAFE),
                InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_BAR], callback_data=CALLBACK_BUTTON2_BAR),
            ],
            [
                InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_RESTAURANT], callback_data=CALLBACK_BUTTON3_RESTAURANT),
            ]
        ]
    return InlineKeyboardMarkup(keyboard)


def do_eat(update: Update, context):
    update.message.reply_text(
        text="Select a category to search.",
        reply_markup=get_place_keyboard()
    )
    return CHOOSING


def button(update : Update, context: CallbackContext):
    print("hi")
    context.user_data['choise'] = update.callback_query.data
    update.callback_query
    update.callback_query.edit_message_text(
        text="Send U location",
    )


def do_done(update : Update, context):
    i=0
    type_of_place = context.user_data['choise']
    print(type_of_place)
    longitude,latitude =update.message.location.longitude, update.message.location.latitude
    result=search(type_of_place,longitude,latitude)
    while i < 3:
        answer = result[str(i)+'answer']
        longitude = result[str(i)+'longitude']
        latitude = result[str(i)+'latitude']
        update.message.reply_text(text=answer)
        update.message.reply_location(longitude=longitude, latitude=latitude)
        i += 1
    context.user_data.clear()
    return ConversationHandler.END


def hedler_for_main():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('eat', do_eat)],

        states={
            CHOOSING: [CallbackQueryHandler(button)]
        },

        fallbacks=[MessageHandler(Filters.location, do_done)]
    )
    return conv_handler
