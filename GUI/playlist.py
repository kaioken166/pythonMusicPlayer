from tkinter import *
from controller.playlistController import playlistController
from controller.songController import SongController

class Playlist:
    def __init__(self, list_frame):
        self.playlist = playlistController()
        self.song = SongController()
        self.song_list = Listbox(list_frame)
        self.song_list.pack(side=LEFT, fill=BOTH, padx=10, pady=10, expand=True)
        self.list_frame = list_frame
        self.pl_state = False

        # Create a scrollbar to scroll through the songs
        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side=RIGHT, fill='y')

        # Attach the scrollbar to the listbox
        self.song_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.song_list.yview)

    def open_playlist(self):
        if self.pl_state:
            self.list_frame.grid_remove()
            self.pl_state = False
        else:
            self.list_frame.grid(row=4, column=0, pady=10, columnspan=3, sticky='ew')
            self.pl_state = True

    def add_song(self, song):
        self.song_list.insert(END, song)

    def add_to_playlist(self, songArr):
        for pathSong in songArr:
            info = self.song.get_info(path=pathSong)
            self.add_song(info.get('title'))
            print(str(info))
        print(str(self.song_list))