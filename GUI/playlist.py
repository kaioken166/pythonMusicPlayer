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
            self.pl_state = True
            self.list_frame.grid(row=4, column=0, pady=10, columnspan=3, sticky='ew')

    def add_song(self, song):
        self.song_list.insert(END, song)

    def add_to_playlist(self, songArr):
        for pathSong in songArr:
            info = self.song.get_info(path=pathSong)
            self.add_song(info.get('name'))

    def play_song_GUI(self):  # current_song is a label
        # Get the index of the selected song
        index = self.song_list.curselection()

        # Check if the song list is empty or not
        if index:
            # Get the first element of the index tuple
            index = index[0]
        else:
            # Set the index to 0 to select the first song
            index = 0

        # Get the name of the selected song
        name = self.song_list.get(index)

        # Update the label with the name of the selected song
        current_song_label.config(text=f"Playing {name}")

    def next_song_GUI(self):
        # Get the current selection index
        current_index = self.song_list.curselection()

        # Check if it is empty
        if len(current_index) == 0:
            # No item is selected, use a default index
            current_index = 0
        else:
            # Convert it to an integer
            current_index = current_index[0]

        # Increment it by one
        next_index = (current_index + 1) % self.song_list.size()

        # Select the next item in the listbox
        self.song_list.selection_clear(0, END)
        self.song_list.selection_set(next_index)

        # Play the new song
        self.play_song_GUI()