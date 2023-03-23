# Import tkinter and ttk libraries
from tkinter import *
from tkinter import ttk
# from tkinter import Button
from tkinter.ttk import *
from PIL import Image, ImageTk
# import time
import pygame
import tkinter as tk

# Create a window object
window = tk.Tk()

# Set the window title
window.title("Music Player")

# Set the minimum size of the window
window.minsize(400, 135)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Create a menu bar
menubar = tk.Menu(window)

# Create a file menu and add some commands
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

# Add the file menu to the menu bar with a label "File"
menubar.add_cascade(label="File", menu=filemenu)

# Create an edit menu and add some commands
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")

# Add the edit menu to the menu bar with a label "Edit"
menubar.add_cascade(label="Edit", menu=editmenu)

# Tạo biến trạng thái cho đoạn văn bản
pl_state = False


# Define a function to open a new window with a listbox of songs
def open_playlist():
    global pl_state
    if pl_state:
        listbox_frame.grid_remove()
        pl_state = False
    else:
        listbox_frame.grid(row=4, column=0, pady=10, columnspan=3, sticky='ew')
        pl_state = True


# Create a view menu and add a submenu with label "Playlist"
viewmenu = tk.Menu(menubar, tearoff=0)
viewmenu.add_cascade(label="Playlist", command=open_playlist)

# Add the view menu to the menu bar with a label "View"
menubar.add_cascade(label="View", menu=viewmenu)

# Configure the window to use the menu bar
window.config(menu=menubar)

# Set the window size
# window.geometry("400x300")

# Create a label to display the album image
album_image = Label(window)

# Load an image file using Image.open()
ab_image = Image.open("album.jpg")

# Resize the image to fit the label
ab_image = ab_image.resize((400, 400))

# Convert the image to PhotoImage format
photo = ImageTk.PhotoImage(ab_image)

# Set the image attribute of the label to the photo
album_image.image = photo

# Configure the label to display the photo
album_image.config(image=photo)

# Pack or place the label on the window
album_image.grid(row=0, column=0, columnspan=2)

# Create progress bar
style = ttk.Style()
style.configure("red.Horizontal.TProgressbar", background="red", troughcolor="white", borderwidth=2)
progress = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode="determinate",
                           style="red.Horizontal.TProgressbar")
progress.grid(row=1, column=0, columnspan=2, sticky="ew")


def on_motion(event):
    x = event.x
    max_value = progress['maximum']
    width = progress.winfo_width()
    value = x * max_value / width
    progress['value'] = value
    pygame.mixer.music.set_pos(value / 100)  # assuming 100 seconds is the maximum duration


progress.bind('<B1-Motion>', on_motion)

# Create a frame for Listbox
listbox_frame = Frame(window)

# Create a listbox to display songs
song_list = Listbox(listbox_frame)
song_list.pack(side=LEFT, fill=BOTH, padx=10, pady=10, expand=True)

# Add some sample songs to the listbox
song_list.insert(END, "Song 1")
song_list.insert(END, "Song 2")
song_list.insert(END, "Song 3")
song_list.insert(END, "Song 4")
song_list.insert(END, "Song 5")
song_list.insert(END, "Song 6")
song_list.insert(END, "Song 7")
song_list.insert(END, "Song 8")
song_list.insert(END, "Song 9")
song_list.insert(END, "Song 10")
song_list.insert(END, "Song 11")
song_list.insert(END, "Song 12")
song_list.insert(END, "Song 13")

# Create a scrollbar to scroll through the songs
scrollbar = Scrollbar(listbox_frame)
scrollbar.pack(side=RIGHT, fill='y')

# Attach the scrollbar to the listbox
song_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=song_list.yview)

# Create a label to show the current song
current_song = Label(window, text="No song selected", font=("Arial", 16))
current_song.grid(row=2, column=0, sticky='', columnspan=3, pady=10)


# Define a function to play the selected song
def play_song():
    # Get the index of the selected song
    index = song_list.curselection()

    # Check if the song list is empty or not
    if index:
        # Get the first element of the index tuple
        index = index[0]
    else:
        # Set the index to 0 to select the first song
        index = 0

    # Get the name of the selected song
    name = song_list.get(index)

    # Update the label with the name of the selected song
    current_song.config(text=f"Playing {name}")


def next_song():
    # Get the current selection index
    current_index = song_list.curselection()

    # Check if it is empty
    if len(current_index) == 0:
        # No item is selected, use a default index
        current_index = 0
    else:
        # Convert it to an integer
        current_index = current_index[0]

    # Increment it by one
    next_index = (current_index + 1) % song_list.size()

    # Select the next item in the listbox
    song_list.selection_clear(0, END)
    song_list.selection_set(next_index)

    # Play the new song
    play_song()


def previous_song():
    # Get the current selection index
    current_index = song_list.curselection()

    # Check if it is empty
    if len(current_index) == 0:
        # No item is selected, use a default index
        current_index = 0
    else:
        # Convert it to an integer
        current_index = current_index[0]

    # Decrement it by one
    previous_index = (current_index - 1) % song_list.size()

    # Select the previous item in the listbox
    song_list.selection_clear(0, END)
    song_list.selection_set(previous_index)

    # Play the new song
    play_song()


# Create a frame for the buttons
button_frame = Frame(window)

# Pack the frame below the listbox
button_frame.grid(row=3, column=0, pady=10)

# Create Photo for button below
pl_image = Image.open("image/play-button.png")
pl_image = pl_image.resize((30, 30))
photo_play = ImageTk.PhotoImage(pl_image)

pl_image2 = Image.open("image/pause-button.png")
pl_image2 = pl_image2.resize((30, 30))
photo_play2 = ImageTk.PhotoImage(pl_image2)

pr_image = Image.open("image/back-button.png")
pr_image = pr_image.resize((30, 30))
photo_previous = ImageTk.PhotoImage(pr_image)

next_image = Image.open("image/next-button.png")
next_image = next_image.resize((30, 30))
photo_next = ImageTk.PhotoImage(next_image)

is_playing = False


# Create animation switch play and pause button
def change_image_play():
    # Access the global variable is_playing
    global is_playing
    # Check the current state of the button
    if is_playing:
        # Change it to photo1 and set is_playing to False
        play_button.config(image=photo_play)
        is_playing = False
    else:
        # Change it to photo2 and set is_playing to True
        play_button.config(image=photo_play2)
        is_playing = True


# Create Play button
play_button = Button(button_frame, image=photo_play, command=lambda: [play_song(), change_image_play()])

# Create Next, Previous button
next_button = Button(button_frame, image=photo_next, command=next_song)
previous_button = Button(button_frame, image=photo_previous, command=previous_song)

# Pack all the button in order
previous_button.grid(row=0, column=2, padx=5, pady=5)
play_button.grid(row=0, column=3, padx=5, pady=5)
next_button.grid(row=0, column=4, padx=5, pady=5)

# Initialize pygame mixer
pygame.mixer.init()


# Define a function that can change the volume
def change_volume(value):
    # Convert the value from string to float
    volume = float(value) / 100
    # Set the volume of the mixer
    pygame.mixer.music.set_volume(volume)


# Create a scale widget with horizontal orientation and range from 0 to 100
volume_slider = Scale(button_frame, from_=100, to=0, orient=HORIZONTAL, command=change_volume)

# Pack the scale widget below the button frame
volume_slider.grid(row=0, column=7, sticky='e', padx=5, pady=10)

# Create a separator widget with vertical orientation
separator = Separator(button_frame, orient=VERTICAL)
separator1 = Separator(button_frame, orient=VERTICAL)

# Grid the separator between the frames with sticky option
separator.grid(row=0, column=5, sticky="ns")
separator1.grid(row=0, column=1, sticky="ns")

# Create image for mute button
mt_image = Image.open("image/volume-up.png")
mt_image = mt_image.resize((30, 30))
photo_mute = ImageTk.PhotoImage(mt_image)

# Create mute button
mt_button = Button(button_frame, image=photo_mute)

# Place button
mt_button.grid(row=0, column=6, padx=5, pady=5)

# Create a Label to display the current time
time_label = Label(button_frame, text="00:00", font="Arial 16")
time_label.grid(row=0, column=0, pady=5, padx=10)

# Start the main loop of the window
window.mainloop()
