import pygame
from mutagen.mp3 import MP3
import eyed3
from PIL import ImageTk, Image


class SongController:

    def __init__(self):
        self.pathCurrentSong = ''
        self.mixer = pygame.mixer
        self.mixer.init()


    def play_song(self,path):
        self.pathCurrentSong = path
        self.mixer.music.load(path)
        self.mixer.music.play()

    def play_in_time(self, start,isPercent = True):
        
        if isPercent :
            time = SongController.get_time() / 100 * start
        else:
            time = start
        
        self.mixer.music.play(start=time)


    def get_time(self,song):
        song = MP3(self.pathCurrentSong)
        song_length = song.info.length
        return song_length

    def pause_music(self):
        self.mixer.music.stop()

    def get_img(self):
        audio_file = eyed3.load(self.pathCurrentSong)
        myit = iter(audio_file.tag.images)
        image = next(myit)
        image_file = open("tmp.jpg", "wb")
        image_file.write(image.image_data)
        image_file.close()
        img = Image.open("tmp.jpg")
        img = ImageTk.PhotoImage(img)
        return img

    


        