import tkinter as tk

from PIL import Image, ImageTk


def on_enter(e):
    e.widget['background'] = '#C8C8C8'


def on_leave(e):
    e.widget['background'] = '#f0f0f0'


class MyButton(tk.Button):
    def __init__(self, master=None, image_path=None, command=None, img_size=(30, 30), **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.img = Image.open(image_path)
        self.img = self.img.resize(img_size)
        self.photo = ImageTk.PhotoImage(self.img)
        self.config(image=self.photo, command=command, bd=0, highlightthickness=0)
        self.bind("<Enter>", on_enter)
        self.bind("<Leave>", on_leave)

    def change_image(self, image_path):
        self.img = Image.open(image_path)
        self.img = self.img.resize((30, 30))
        self.photo = ImageTk.PhotoImage(self.img)
        self.config(image=self.photo)

