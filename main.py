from telegram import Update


def do_start(update: Update, context):
    update.message.reply_text("HI")

    
def main():
    updater = Updater(TOKKEN_FOR_BOT, use_context=True)

    start_handler = CommandHandler("start", do_start)
    message_handler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    mypath = str(Path().absolute())
    print(mypath)
    parser = argparse.ArgumentParser(description='Loading model for prediction')
    parser.add_argument("-m", "--model", type=str,
                        help="the path to keras model",
                        default='AI/modelForChatBot.h5')
    parser.add_argument("-t", "--tokenizer", type=str,
                        help="the path to the tokenizer",
                        default='AI/encode/tokenizer.pickle')
    parser.add_argument("-e", "--encoder", type=str,
                        help="the path to encoder",
                        default='AI/encode/classes.npy')
    args = vars(parser.parse_args())
    model_path = args['model']
    tokenizer_path = args['tokenizer']
    encoder_path = args['encoder']
    # create model classifier obj and test prediction
    model = IntentClassifier(model_path, tokenizer_path, encoder_path)
    main()
