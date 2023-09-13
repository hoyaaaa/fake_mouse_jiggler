import pyautogui
import tkinter
from PIL import Image, ImageTk
import os
import sys
import tkinter.font as font
import random
from multiprocessing import Process, Queue
import time
from threading import Thread

pyautogui.FAILSAFE = False

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

window = tkinter.Tk()
window.geometry("500x130")
window.resizable(False, False)
window.title("Rock Your Mouse!")
window.iconbitmap(default=resource_path("rock.ico"))
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

status = "stopped" # stopped, running, rocking


class ImageLabel(tkinter.Label):
    def load(self, image_path):
        self.idx = 0
        im = Image.open(image_path)

        self.frames = []
        for i in range(im.n_frames):
            frame = im.copy().resize((100, 100))
            self.frames.append(ImageTk.PhotoImage(frame))
            im.seek(i)
        self.frames = self.frames[2:]
        self.n_frames = len(self.frames)
        self.configure(image=self.frames[0])

    def update(self):
        while True:
            self.idx += 1
            self.idx %= self.n_frames
            frame = self.frames[self.idx]
            self.configure(image=frame)
            if status == "rocking":
                time.sleep(0.03)
            elif status == "running":
                time.sleep(0.15)
            else:
                break                

    def run(self):
        thread = Thread(target=self.update, daemon=True)
        thread.setDaemon(True)
        thread.start()     

class Mouse():
    def __init__(self):
        self.count = 0
        self.pos = pyautogui.position()

    def update(self):
        global status
        while status != "stopped":
            if status == "running":
                cur_pos = pyautogui.position()
                if (abs(self.pos.x - cur_pos.x) <= 1 and abs(self.pos.y - cur_pos.y) <= 1):
                    self.count += 1            
                else:
                    self.count = 0

                self.pos = cur_pos
                if self.count >= 2:
                    status = "rocking"
                    self.count = 0
                else:
                    time.sleep(0.5)
            elif status == "rocking":
                cur_pos = pyautogui.position()
                if (abs(self.pos.x - cur_pos.x) > 5 or abs(self.pos.y - cur_pos.y) > 5):
                    self.pos = cur_pos
                    status = "running"
                else:
                    xe = random.randint(-5, 5)
                    ye = random.randint(-5, 5)
                    pyautogui.moveTo(self.pos.x + xe, self.pos.y + ye)
                    time.sleep(0.01)
            else:
                break

    def run(self):
        thread = Thread(target=self.update, daemon=True)
        thread.setDaemon(True)
        thread.start()

def click_event():
    global status
    if status == "stopped":
        status = "running"
        mouse.run()
        img.run()
        btn["text"] = "Stop!"
    else:
        status = "stopped"
        btn["text"] = "Let's Rock!"

mouse = Mouse()
img = ImageLabel(window)
img.load(resource_path("rock-dog.gif"))

btn = tkinter.Button(window, text="Let's Rock!", command=click_event, font=font.Font(size=20, weight="bold"))

btn.grid(row=0, column=0, sticky="nesw")
img.grid(row=0, column=1, sticky="nesw", padx=(15, 15), pady=(15, 15))

window.mainloop()