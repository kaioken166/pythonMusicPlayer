import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Separator

# import pygame

from GUI.album_label import MyLabel
from GUI.button_function import MyButton
from GUI.playlist import Playlist
from GUI.song import Song
from GUI.timeLabel import TimeLabel

# Create a root object
root = tk.Tk()

# Set the root title
root.title("Music Player")

# Set the minimum size of the root
root.minsize(515, 140)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a menu bar
menubar = tk.Menu(root)

# Create Playlist frame
list_frame = Frame(root)

# Create a listbox to display songs
my_playlist = Playlist(list_frame)
my_song = Song()

# def add_song_and_playlist():
#     playlist.add_song()
#     my_playlist.add_song(playlist.get_song_arr())


# Create a file menu and add some commands
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=lambda: my_playlist.open_files())
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Add the file menu to the menu bar with a label "File"
menubar.add_cascade(label="File", menu=filemenu)

# Add the view menu to the menu bar with a label "View"
menubar.add_command(label="Playlist", command=lambda: my_playlist.open_playlist())

# Configure the root to use the menu bar
root.config(menu=menubar)

# song = SongController()
# playlist = playlistController()

# Start
label_frame = tk.Frame(root)
label_frame.grid(row=0, column=0, columnspan=2, sticky='ew')

album_image = MyLabel(label_frame, image_path='image/Music_Isometric.png', img_size=(620, 515))
album_image.pack(fill='x')  # inside label_frame

# Create progress bar
song_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
song_slider.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10, padx=20)

# Create a label to show the current song
current_song = Label(root, text="No song selected", font=("Arial", 16))
current_song.grid(row=2, column=0, sticky='', columnspan=3, pady=10)

# Create a frame for the buttons
button_frame = Frame(root)
# button_frame.config(background='#353839')
button_frame.grid(row=3, column=0, pady=10, sticky='w')

# Create content inside button frame

# Create a Label to display the current time
# time_label = Label(button_frame, text="00:00", font="Arial 16")
time_label = TimeLabel(button_frame)
time_label.grid(row=0, column=0, pady=5, padx=10)

# Add seperator
separator = Separator(button_frame, orient=VERTICAL)
separator.grid(row=0, column=1, sticky="ns")

play_button = MyButton(button_frame, image_path='image/play-button.png', img_size=(30, 30),
                       command=lambda: [my_playlist.play_song_GUI(current_song), time_label.update_time()])
play_button.grid(row=0, column=2, pady=5, padx=5)

pause_button = MyButton(button_frame, image_path='image/pause-button.png', command=lambda: my_playlist.pause_song())
pause_button.grid(row=0, column=3, pady=5, padx=5)

stop_button = MyButton(button_frame, image_path='image/stop-button.png', command=lambda: my_playlist.stop_song())
stop_button.grid(row=0, column=4, padx=5, pady=5)

separator2 = Separator(button_frame, orient=VERTICAL)
separator2.grid(row=0, column=5, sticky='ns')

previous_button = MyButton(button_frame, image_path='image/back-button.png',
                           command=lambda: my_playlist.previous_song_GUI(current_song))
previous_button.grid(row=0, column=6, padx=5, pady=5)

next_button = MyButton(button_frame, image_path='image/next-button.png', command=lambda: my_playlist.next_song_GUI(current_song))
next_button.grid(row=0, column=7, padx=5, pady=5)

shuffle_button = MyButton(button_frame, image_path='image/shuffle-off.png')
shuffle_button.grid(row=0, column=8, padx=5, pady=5)

repeat_button = MyButton(button_frame, image_path='image/repeat-off.png')
repeat_button.grid(row=0, column=9, padx=5, pady=5)

separator3 = Separator(button_frame, orient=VERTICAL)
separator3.grid(row=0, column=10, sticky="ns")

# Volume Frame
vol_frame = Frame(root)
vol_frame.grid(row=3, column=1, pady=10, sticky='e')

# Mute button

# muted = False


# def mute_button_callback():
#     global muted
#     if muted:
#         mute_button.change_image(image_path='image/volume-up.png')
#         muted = False
#         vol_frame.update()
#     else:
#         mute_button.change_image(image_path='image/mute.png')
#         muted = True
#         vol_frame.update()


mute_button = MyButton(vol_frame, image_path='image/volume-up.png',
                       command=lambda: my_playlist.mute_song(mute_button=mute_button))

mute_button.grid(row=0, column=0, pady=5, padx=5)

# Create a scale widget with horizontal orientation and range from 0 to 100
volume_slider = ttk.Scale(vol_frame, from_=0, to=100, orient=HORIZONTAL)  # ttk for better UI
volume_slider.set(100)

# Pack the scale widget below the button frame
volume_slider.grid(row=0, column=1, padx=5, pady=10)

# End

# Start the main loop of the root
root.mainloop()
