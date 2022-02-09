from sqlalchemy.dialects import mysql
from sqlalchemy.sql import select

import sqlalchemy as sa

from database.mysql_connection_string import mysql_connection_string
from database.models.song import Song
from smart_search import SmartSearch


class SongController:
    def __init__(self):
        self.engine = self.create_connection()
        self.smart_search = SmartSearch

    def create_connection(self):
        engine = sa.create_engine(mysql_connection_string())
        return engine.connect()

    def find_song(self, song_name: str):
        clear_song_name = song_name.lower().strip()
        url = self.select_song_by_name(clear_song_name)
        if url:
            return url['url']
        songs_dict = self.select_all_songs()
        return self.smart_search.find_song(clear_song_name, songs_dict)

    def select_song_by_name(self, song_name: str) -> str:
        stmt = select(Song.url).where(Song.name == song_name)
        result = self.compile_execute_selection(stmt)
        return result.fetchone()

    def select_all_songs(self) -> dict:
        stmt = select(Song.name, Song.url)
        result = self.compile_execute_selection(stmt)
        return dict(result.fetchall())

    def compile_execute_selection(self, stmt):
        stmt_compiled = stmt.compile(compile_kwargs={"literal_binds": True}, dialect=mysql.dialect())
        return self.connection.execute(str(stmt_compiled))


if __name__ == '__main__':
    song_controller = SongController()
    song_controller.select_song_by_name('арфы золотые')
    song_controller.smart_find_song('арфы золотые')
