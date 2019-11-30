from telegram import Update
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

def do_start(update: Update, context):
    update.message.reply_text("HI")


def main():
    updater = Updater(TOKKEN_FOR_BOT, use_context=True)
    start_handler = CommandHandler("start", do_start)
    updater.dispatcher.add_handler(start_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
