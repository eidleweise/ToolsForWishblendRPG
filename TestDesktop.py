import tkinter as tk


def create_window(title, message):
    window = tk.Tk()
    window.title(title)
    window.geometry("600x400")
    newlabel = tk.Label(text = message)
    newlabel.grid(column=0, row=0)
    window.mainloop()


create_window("Desktop App", "We can make a window 2")
