import time
from tkinter import *

from controller.playlistController import playlistController
from controller.songController import SongController


class Player:
    def __init__(self, list_frame, song_slider, time_label, current_song):
        self.current_song = current_song
        self.current_time = 0
        self.time_skip = 0
        self.play_list_controller = playlistController()
        self.song_controller = SongController()
        self.song_list = Listbox(list_frame)
        self.song_slider = song_slider
        self.time_lable = time_label
        self.song_list.pack(side=LEFT, fill=BOTH, padx=10, pady=10, expand=True)
        self.list_frame = list_frame
        self.pl_state = False

        # Create a scrollbar to scroll through the songs
        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side=RIGHT, fill='y')

        # Attach the scrollbar to the listbox
        self.song_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.song_list.yview)

    def update_play_song(self):
        name = self.song_controller.get_info().get('name')
        self.current_song.config(text=f'Playing {name}')
        self.time_skip = 0

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
        self.upadate_playlist()
        # self.add_songs(self.play_list_controller.get_song_arr())

    def upadate_playlist(self):
        self.song_list.delete(0, self.song_list.size())
        self.add_songs(self.play_list_controller.get_song_arr())

    def shuffle(self):
        self.play_list_controller.suffle()
        self.upadate_playlist()

    def play_song_GUI(self):  # current_song is a label
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

        # Update the label with the name of the selected song
        path = self.play_list_controller.get_song(index=index)
        self.song_controller.play_song(path=path)
        self.song_list.selection_clear(0, END)
        self.song_list.selection_set(index)
        self.update_play_song()
        self.timer()

    def next_song_GUI(self):
        # Get the current selection index
        index = self.play_list_controller.next_song()

        # Play the new song
        path = self.play_list_controller.get_song(index=index)
        self.song_controller.play_song(path=path)

        # Select the next item in the listbox
        self.song_list.selection_clear(0, END)
        self.song_list.selection_set(index)
        self.update_play_song()

    def previous_song_GUI(self):
        # Get the current selection index
        index = self.play_list_controller.previous_song()

        # Play the new song
        path = self.play_list_controller.get_song(index=index)
        self.song_controller.play_song(path=path)
        self.song_list.selection_clear(0, END)
        self.song_list.selection_set(index)

        # Select the next item in the listbox
        self.song_list.selection_clear(0, END)
        self.song_list.selection_set(index)
        self.update_play_song()

    def repeat_song(self):
        index = self.play_list_controller.get_index_current()

        # Play the new song
        path = self.play_list_controller.get_song(index=index)
        self.song_controller.play_song(path=path)
        self.song_list.selection_clear(0, END)
        self.song_list.selection_set(index)

        # Select the next item in the listbox
        self.song_list.selection_clear(0, END)
        self.song_list.selection_set(index)
        self.update_play_song()

    def mute_song(self, mute_button):
        self.mute_button = mute_button
        if self.song_controller.check_mute():
            self.song_controller.mute_music()
            self.song_controller.set_volume(self.volume_value)
            mute_button.change_image(image_path='image/volume-up.png')
            self.__volume_slider.set(self.volume_value)
        else:
            self.volume_value = self.song_controller.get_volume()
            self.song_controller.mute_music()
            mute_button.change_image(image_path='image/mute.png')
            self.__volume_slider.set(0)

    def pause_song(self):
        self.song_controller.pause_music()

    def stop_song(self):
        self.song_controller.stop_music()
        self.song_list.selection_clear(0, END)

    def timer(self):
        if self.song_controller.check_stop():
            return
        if self.current_time == int(self.song_controller.get_time_len()):
            if self.play_list_controller.check_repeat():
                self.repeat_song()
            else:
                self.next_song_GUI()
        elif self.song_slider.get() != self.current_time:
            self.song_controller.play_in_time(time=self.song_slider.get())
            self.time_skip = int(self.song_slider.get())
            # self.current_time = int (self.song_controller.get_current_time()) + self.time_skip

        self.current_time = int(self.song_controller.get_current_time()) + self.time_skip
        # print(f'{self.current_time}/{self.song_controller.get_time_len()}')
        self.song_slider.config(to=self.song_controller.get_time_len() - 1)
        converted_current_time = time.strftime('%M:%S', time.gmtime(self.current_time))
        self.time_lable.config(text=f'{converted_current_time}')
        self.song_slider.set(int(self.current_time))

        self.time_lable.after(1000, self.timer)

    def volume(self, volume_slider, mute_button, value):
        if value == 0:
            mute_button.change_image(image_path='image/mute.png')
        else:
            mute_button.change_image(image_path='image/volume-up.png')
        self.__volume_slider = volume_slider
        self.song_controller.set_volume(value)

    def repeat(self, repeat_button):
        self.play_list_controller.repeat()
        if self.play_list_controller.check_repeat():
            repeat_button.change_image(image_path='image/repeat-on.png')
        else:
            repeat_button.change_image(image_path='image/repeat-off.png')
