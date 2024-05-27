from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.inputmedia import InputMediaPhoto

def send_photo(update, context):
    chat_id = update.message.chat_id
    input_media_photo = InputMediaPhoto(open('path_to_your_image.jpg', 'rb'))
    context.bot.send_photo(chat_id=chat_id, photo=input_media_photo)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello!")

def main():
    updater = Updater(token='6359816178:AAHFntqBNSi2pNJ3_peGbAr3tFhbji5bCLo', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text, send_photo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()