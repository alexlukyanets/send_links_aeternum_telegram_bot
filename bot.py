import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

from message_text import MessageText as message_text
from song_controller import SongController

load_dotenv()

TOKEN = os.getenv('TOKEN', '')
PORT = int(os.environ.get('PORT', 5000))

updater = Updater(TOKEN, use_context=True)
song_controller = SongController()


def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text=message_text.welcome())


def on_help(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=message_text.help())


def on_message(update, context):
    chat_id = update.effective_chat.id
    rawtext = update.message.text
    print(rawtext)
    url = song_controller.find_song(rawtext)

    if url:
        context.bot.send_message(chat_id, url)
    else:
        context.bot.send_message(chat_id=chat_id, text=message_text.error())


if __name__ == '__main__':
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", on_start))
    dispatcher.add_handler(CommandHandler("help", on_help))
    dispatcher.add_handler(MessageHandler(Filters.all, on_message))

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://aeternum-notes-bot.herokuapp.com/' + TOKEN)
    updater.idle()
