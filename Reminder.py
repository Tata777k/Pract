from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t = 0


def set():
    global t
    rem = sd.askstring("Время напоминания", "Установите напоминание(ЧЧ:ММ) в 24 формате")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute, second=0)
            print(dt)
            t = dt.timestamp()
            print(t)
            check()
        except Exception as e:
            mb.showerror("Ошибка.", f"Произошла ошибка {e}")


def check():
    print( "check:" )
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0
            print( "finish>>>" )
        else:
            print("after>>>")
            window.after(10000, check)


def play_snd():
    pygame.mixer.init()
    pygame.mixer.music.load("raz.mp3")
    print("playing...")
    pygame.mixer.music.play()

window = Tk()
window.title("Напоминание")
label = Label(text="Установите напоминание",font=("Arial", 14))
label.pack(pady=10)
set_button = Button(text="Установить напоминание", command=set)
set_button.pack()

#play_snd()

window.mainloop()