import datetime
import tkinter as tk

import pygame

from controller.songController import SongController


def update_label():
    # current_time = datetime.datetime.now().strftime('%H:%M:%S')
    song_time = pygame.mixer.music.get_pos() / 1000
    song_time = datetime.timedelta(seconds=song_time)
    song_time = str(song_time).split('.')[0]
    time_label.config(text=f"Song time: {song_time}")
    if not pygame.mixer.music.get_busy():
        # song_length = pygame.mixer.music.get_length() / 1000
        song_length = song1.get_time()
        song_length = datetime.timedelta(seconds=song_length)
        song_length = str(song_length).split('.')[0]
        time_label.config(text=f"Song time: {song_length}")
    else:
        time_label.after(1000, update_label)


root = tk.Tk()
time_label = tk.Label(root, font=('calibri', 40))
time_label.pack()

song1 = SongController()
song1.play_song(path='song/song.mp3')

update_label()
root.mainloop()
