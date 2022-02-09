from fuzzywuzzy import process
from fuzzywuzzy import fuzz


class SmartSearch:
    @classmethod
    def find_song(cls, song_name: str, songs_dict: dict):
        found_name, ratio = process.extractOne(song_name, songs_dict.keys(), scorer=fuzz.token_sort_ratio)
        print(ratio)
        if ratio < cls.minimum_valid_ratio():
            return
        return songs_dict.get(found_name)

    @staticmethod
    def minimum_valid_ratio():
        return 40
