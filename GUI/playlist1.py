from tkinter import *

from controller.playlistController import playlistController
from controller.songController import SongController


class Playlist:
    def __init__(self, list_frame):
        self.play_list_controller = playlistController()
        self.song_controller = SongController()
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
            self.pl_state = True
            self.list_frame.grid(row=4, column=0, pady=10, columnspan=3, sticky='ew')

    def add_songs(self, songArr):
        for pathSong in songArr:
            info = self.song_controller.get_info(path=pathSong)
            self.song_list.insert(END, info.get('name'))

    def open_files(self):
        self.play_list_controller.add_song()
        self.add_songs(self.play_list_controller.get_song_arr())

    def play_song_GUI(self, current_song):  # current_song is a label
        # Get the index of the selected song
        index = self.song_list.curselection()

        # Check if the song list is empty or not
        if index:
            # Get the first element of the index tuple
            if self.play_list_controller.get_index_current() == index[0]:
                if self.song_controller.check_pause():
                    self.song_controller.pause_music()
                return
            self.play_list_controller.set_index_current(index=index[0])

        index = self.play_list_controller.get_index_current()

        # Get the name of the selected song
        name = self.song_list.get(index)

        # Update the label with the name of the selected song
        current_song.config(text=f"Playing {name}")
        path = self.play_list_controller.get_song(index=index)
        self.song_controller.play_song(path=path)
        self.song_list.selection_clear(0, END)
        self.song_list.selection_set(index)

    def next_song_GUI(self, current_song):
        # Get the current selection index
        index = self.play_list_controller.next_song()
        print(index)

        # Play the new song
        path = self.play_list_controller.get_song(index=index)
        self.song_controller.play_song(path=path)

        # Increment it by one
        next_index = index % self.song_list.size()

        # Select the next item in the listbox
        self.song_list.selection_clear(0, END)
        self.song_list.selection_set(next_index)

        # Get the name of the selected song
        name = self.song_list.get(index)

        # Update the label with the name of the selected song
        current_song.config(text=f"Playing {name}")

    def previous_song_GUI(self, current_song):
        # Get the current selection index
        index = self.play_list_controller.previous_song()
        print(index)

        # Play the new song
        path = self.play_list_controller.get_song(index=index)
        self.song_controller.play_song(path=path)

        # Decrement it by one
        previous_index = index % self.song_list.size()

        # Select the next item in the listbox
        self.song_list.selection_clear(0, END)
        self.song_list.selection_set(previous_index)

        # Get the name of the selected song
        name = self.song_list.get(index)

        # Update the label with the name of the selected song
        current_song.config(text=f"Playing {name}")

    def mute_song(self, mute_button):
        if self.song.mute_music():
            mute_button.change_image(image_path='image/volume-up.png')
        else:
            mute_button.change_image(image_path='image/mute.png')

    def pause_song(self):
        self.song_controller.pause_music()

    def stop_song(self):
        self.song_controller.stop_music()
        self.song_list.selection_clear(0, END)
