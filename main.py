from telegram import Update
from telegram.ext import Updater, CommandHandler


def do_start(update: Update, context):
    answer = " *Hello, " + update.message.from_user.first_name + "*\n I am u helper . " \
             "if U want drink or eat tap - /eat \n" \
             "And I will show nearest the nearest bars or cafe or restaurant"
    update.message.reply_markdown(text=answer)


def main():
    updater = Updater("Token", use_context=True)
    start_handler = CommandHandler("start", do_start)
    updater.dispatcher.add_handler(start_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
