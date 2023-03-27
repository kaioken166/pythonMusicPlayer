import pygame
from mutagen.mp3 import MP3
import eyed3
from PIL import ImageTk, Image


class SongController:

    def __init__(self):
        self.__path_current_song = ''
        self.__pause = False
        self.__mixer = pygame.mixer
        self.__mixer.init()


    def play_song(self,path):
        self.pathCurrentSong = path
        self.mixer.music.load(path)
        self.mixer.music.play()

    def play_in_time(self, start,isPercent = True):
        
        if isPercent :
            time = self.get_time() / 100 * start
        else:
            time = start
        
        self.mixer.music.play(start=time)


    def get_time(self,song):
        song = MP3(self.__path_current_song)
        song_length = song.info.length
        return song_length

    def pause_music(self):
        self.pause = True
        self.mixer.music.pause()
        
    def unpause_music(self):
        self.pause = False
        self.mixer.music.unpause()

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
        return not ( self.pause or pygame.mixer.music.get_busy()) # return True if finish
            
    def get_info(self):
        song = eyed3.load(self.__path_current_song)
        return {
            'album': song.tag.album,
            'title': song.tag.album,
            'artist': song.tag.artist
        }

