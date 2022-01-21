import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

print("Бот запущен. Нажмите Ctrl+C для завершения")

load_dotenv()

TOKEN = os.getenv('TOKEN', '')

updater = Updater(TOKEN, use_context=True)


def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text="Бот для поиска нот по словам. Для поиска напишите название или начало песни. Длина сообщения от одного до трех слов")


def on_help(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='С вопросами и предложениями обращайтесь к @white_kar')


notesnames = {
    'без любви': 'Без любви все теряет смысл',
    'без любви все': 'Без любви все теряет смысл',

    'хорал': 'Рождественский хорал',
    'рождественский': 'Рождественский',
    'рождественский хорал': 'Рождественский хорал',
    'звездная': 'Рождественский хорал',
    'звездная ночь': 'Рождественский хорал',
    'звёздная': 'Рождественский хорал',
    'звёздная ночь': 'Рождественский хорал',

    'новая земля': 'Новая земля',
    'земля': 'Новая земля',
    'господом прекрасная': 'Новая земля',
    'господом': 'Новая земля',

}


def on_message(update, context):
    chat = update.effective_chat
    rawtext = update.message.text
    try:
        text = notesnames[rawtext.casefold()]

        if (text == "Без любви все теряет смысл"):
            context.bot.send_message(chat_id=chat.id,
                                     text="https://drive.google.com/file/d/1fRv36pzV8ofUuJJyVorJn72193sG7PET")
        elif text == 'Рождественский':
            context.bot.send_message(chat_id=chat.id,
                                     text='https://drive.google.com/file/d/1klxCwiRwEJmQPwp0uatS5Zb_Gtq1yqs-')
            context.bot.send_message(chat_id=chat.id,
                                     text='https://drive.google.com/file/d/16QVEuQpzsR4kH3YZDA4YyUQG8eaL3uom')
        elif text == 'Рождественский хорал':
            context.bot.send_message(chat_id=chat.id,
                                     text='https://drive.google.com/file/d/1klxCwiRwEJmQPwp0uatS5Zb_Gtq1yqs-')
        elif text == 'Новая земля':
            context.bot.send_message(chat_id=chat.id,
                                     text='https://drive.google.com/file/d/1oC6Jgz4o7PBD8tmeNYfkvfL6_E1GYI4t')
        else:
            context.bot.send_message(chat_id=chat.id, text="Где-то есть, но куда-то затерялись")
    except:
        context.bot.send_message(chat_id=chat.id, text="Не получилось, не фортануло. Воспльзуйтесь /start или /help")
        print('Неудачник', chat.id, 'c сообщением:', rawtext)


if __name__ == '__main__':
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", on_start))
    dispatcher.add_handler(CommandHandler("help", on_help))
    dispatcher.add_handler(MessageHandler(Filters.all, on_message))

    updater.start_polling()
    updater.idle()
