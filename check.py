import tkinter as tk


def on_enter(e):
    myButton['background'] = 'green'


def on_leave(e):
    myButton['background'] = 'SystemButtonFace'


root = tk.Tk()
myButton = tk.Button(root, text="Click Me")
myButton.bind("<Enter>", on_enter)
myButton.bind("<Leave>", on_leave)
myButton.pack()

root.mainloop()
