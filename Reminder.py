from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame

t = 0
music = False


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
            text = sd.askstring("Напоминание", "Введите текст напоминания.")
            label.config(text=f"В {hour:02}:{minute:02} {text} ")
            check(msgtext=text)
        except Exception as e:
            mb.showerror("Ошибка.", f"Произошла ошибка {e}")


def check(msgtext):
    print("check:")
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0
            mb.showinfo( "Внимание!", f"Необходимо {msgtext}" )
            print( "finish>>>" )
        else:
            print("after>>>")
            window.after(10000, lambda: check(msgtext))


def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("raz.mp3")
    print("playing...")
    pygame.mixer.music.play()



def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text="Установить новое напоминание")

window = Tk()
window.title("Напоминание")
label = Label(text="Установите напоминание",font=("Arial", 16))
label.pack(pady=10)
set_button = Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)

stop_button = Button(text="Остановить музыку", command=stop_music)
stop_button.pack(pady=10)

#play_snd()

window.mainloop()