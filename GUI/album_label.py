import tkinter as tk

from PIL import Image, ImageTk


# from tkinter import ttk


class MyLabel(tk.Label):
    def __init__(self, master=None, image_path=None, img_size=(400, 400), **kw):
        tk.Label.__init__(self, master=master, **kw)
        self.img = Image.open(image_path)
        self.img = self.img.resize(img_size)
        self.photo = ImageTk.PhotoImage(self.img)
        self.image = self.photo
        self.config(image=self.photo)

    def change_image(self, new_image_path):
        self.img = Image.open(new_image_path)
        self.img = self.img.resize((400, 400))
        self.photo = ImageTk.PhotoImage(self.img)
        self.image = self.photo
        self.config(image=self.photo)

    def change_image_2(self, img):  # (img=get_img)
        self.image = img
        self.config(image=img)