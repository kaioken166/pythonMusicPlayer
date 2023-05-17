import eyed3
import pygame
from PIL import ImageTk, Image
from mutagen.mp3 import MP3


class SongController:

    def __init__(self):
        self.__stop = True
        self.__path_current_song = ''
        self.__pause = False
        self.__mute = False
        self.__mixer = pygame.mixer
        self.__mixer.init()

    def play_song(self, path):
        self.__path_current_song = path
        self.__mixer.music.load(path)
        self.__mixer.music.play()
        self.__stop = False

    def play_in_time(self, time):
        self.__mixer.music.play(start=time)

    def get_time_len(self, song=False):
        if not song:
            song = self.__path_current_song
        song = MP3(self.__path_current_song)
        song_length = song.info.length
        return song_length

    def get_current_time(self):
        return self.__mixer.music.get_pos() / 1000

    def check_pause(self):
        return self.__pause

    def pause_music(self):
        if self.__pause:
            self.__pause = False
            self.__mixer.music.unpause()
        else:
            self.__pause = True
            self.__mixer.music.pause()
        return self.__pause

    def get_img(self):
        audio_file = eyed3.load(self.__path_current_song)
        myit = iter(audio_file.tag.images)
        image = next(myit)
        image_file = open("tmp.jpg", "wb")
        image_file.write(image.image_data)
        image_file.close()
        img = Image.open("tmp.jpg")
        img = ImageTk.PhotoImage(img)
        return img

    def check_if_finished(self):
        # return True if finish
        return not (self.__pause or self.__mixer.music.get_busy())

    def get_info(self, path=1):
        if path == 1:
            path = self.__path_current_song
        song = eyed3.load(path)
        return {
            'album': song.tag.album,
            'title': song.tag.album,
            'artist': song.tag.artist,
            'name': path.split('/')[-1][:-4]
        }

    def mute_music(self):
        if self.__mute:
            self.__mute = False
            self.__mixer.music.set_volume(1)
        else:
            self.__mute = True
            self.__mixer.music.set_volume(0)

    def check_mute(self):
        return self.__mute

    def stop_music(self):
        self.__mixer.music.stop()

    def check_stop(self):
        return self.__stop

    def set_volume(self, value):
        self.__mixer.music.set_volume(value)

    def get_volume(self):
        return self.__mixer.music.get_volume()
