from telegram import Update,ParseMode
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton,KeyboardButton,ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler,CallbackContext)

CHOOSING = range(1)

CALLBACK_BUTTON1_CAFE = "cafe"
CALLBACK_BUTTON2_BAR = "bar"
CALLBACK_BUTTON3_RESTAURANT = "restaurant"

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
    query = update.callback_query
    chat_id = update.effective_message.chat_id
    query.edit_message_text(
        text="Send U location",
    )


def do_done(update : Update, context):
    print(update.message.location)

def hedler_for_main():
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('eat', do_eat)],

        states={
            CHOOSING: [CallbackQueryHandler(button)]
        },

        fallbacks=[MessageHandler(Filters.location, do_done)]
    )
    return conv_handler
