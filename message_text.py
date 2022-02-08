class MessageText:
    @staticmethod
    def welcome():
        return 'Бот для поиска нот по словам. Для поиска напишите название или начало песни. ' \
               'Длина сообщения от одного до трех слов'

    @staticmethod
    def help():
        return 'С вопросами и предложениями обращайтесь к @white_kar'

    @staticmethod
    def error():
        return 'Не получилось, не фортануло. Воспльзуйтесь /start или /help'
