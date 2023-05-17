import random
from tkinter import filedialog


class playlistController:
    def __init__(self):
        self.__repeat = False
        self.__song_arr = []
        self.__index_current = -1

    def add_song(self):
        songs = filedialog.askopenfilenames(
            title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
        for song in songs:
            self.__song_arr.append(song)

    def get_song(self, index):
        return self.__song_arr[index]

    def get_song_arr(self):
        return self.__song_arr

    def next_song(self):
        if self.__index_current == (len(self.__song_arr) - 1):
            self.__index_current = 0
        else:
            self.__index_current += 1

        return self.__index_current

    def previous_song(self):
        if self.__index_current == 0:
            self.__index_current = len(self.__song_arr) - 1
        else:
            self.__index_current -= 1

        return self.__index_current

    def set_index_current(self, index):
        self.__index_current = index

    def get_index_current(self):
        return self.__index_current

    def suffle(self):
        random.shuffle(self.__song_arr)

    def repeat(self):
        self.__repeat = not self.__repeat

    def check_repeat(self):
        return self.__repeat
