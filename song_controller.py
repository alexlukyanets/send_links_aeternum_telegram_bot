from sqlalchemy.dialects import mysql
from sqlalchemy.sql import select
from fuzzywuzzy import process
import sqlalchemy as sa

from database.mysql_connection_string import mysql_connection_string
from database.models.song import Song


class SongController:
    def __init__(self):
        self.engine = sa.create_engine(mysql_connection_string())
        self.connection = self.engine.connect()

    def find_song(self, song_name: str):
        clear_song_name = song_name.lower().strip()
        url = self.select_song_by_text(clear_song_name)
        if url:
            return url['url']
        return self.smart_find_song(clear_song_name)

    def select_song_by_text(self, song_name: str) -> str:
        stmt = select(Song.url).where(Song.name == song_name)
        result = self.compile_execute_selection(stmt)
        return result.fetchone()

    def select_all_songs(self) -> dict:
        stmt = select(Song.name, Song.url)
        result = self.compile_execute_selection(stmt)
        return dict(result.fetchall())

    def smart_find_song(self, song_name):
        songs_dict = self.select_all_songs()
        found_name, ratio = process.extractOne(song_name, songs_dict.keys())
        if ratio < self.minimum_valid_rating():
            return
        return songs_dict.get(found_name)

    def compile_execute_selection(self, stmt):
        stmt_compiled = stmt.compile(compile_kwargs={"literal_binds": True}, dialect=mysql.dialect())
        return self.connection.execute(str(stmt_compiled))

    @staticmethod
    def minimum_valid_rating():
        return 70


if __name__ == '__main__':
    song_controller = SongController()
    song_controller.select_song_by_text('арфы золотые')
    song_controller.smart_find_song('арфы золотые')
