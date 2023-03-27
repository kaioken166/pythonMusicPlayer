from tkinter import filedialog

class playlistController:
    def __init__(self):
        self.__song_arr = []
        self.__index_current = 0
        
    
    
    def add_song(self):
        songs = filedialog.askopenfilename(title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
        for song in songs :
            self.song_arr.append(song)
        
    def get_song_arr(self):
        return self.__song_arr
    
    def next_song(self):
        if self.__index_current ==  ( len(self.__song_arr) - 1) :
            self.__index_current = 0
        else :
            self.__index_current+=1
        
        return self.__index_current
    
    def previous_song(self):
        if self.__index_current ==  0 :
            self.__index_current = len(self.__song_arr) - 1
        else :
            self.__index_current-=1
        
        return self.__index_current 
          

        