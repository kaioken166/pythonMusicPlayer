import datetime
import tkinter as tk

import pygame

from controller.songController import SongController


class TimeLabel(tk.Label):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        self.config(text="0:00:00", font="Arial 16")
        self.song = SongController()

    def update_time(self):
        song_time = pygame.mixer.music.get_pos() / 1000
        song_time = datetime.timedelta(seconds=song_time)
        song_time = str(song_time).split('.')[0]
        self.config(text=f"{song_time}")

        if not pygame.mixer.music.get_busy():
            song_length = self.song.get_time_len()
            song_length = datetime.timedelta(seconds=song_length)
            song_length = str(song_length).split('.')[0]
            self.config(text=f"{song_length}")
        else:
            self.after(1000, self.update_time)
