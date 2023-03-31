from controller.songController import SongController


class Song:
    def __init__(self):
        self.song = SongController()
        pass

    # def mute_song(self,mute_button):
    #     if self.song.mute_music():
    #         mute_button.change_image(image_path='image/volume-up.png')
    #     else:
    #         mute_button.change_image(image_path='image/mute.png')

    # def pause_song(self):
    #     self.song.pause_music()

    # def stop_song(self):
    #     self.song.stop_music()
