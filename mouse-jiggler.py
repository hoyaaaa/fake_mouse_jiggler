import pyautogui
import tkinter
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

window = tkinter.Tk()
window.geometry("300x50")
window.title("Google Chrome")
window.iconbitmap(default=resource_path("chrome.ico"))
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

running = False

class ImageLabel(tkinter.Label):
    def load(self, image_path):
        self.interval = 100
        self.idx = 0
        im = Image.open(image_path)

        self.n_frames = im.n_frames
        self.frames = []
        for i in range(self.n_frames):
            frame = im.copy().resize((50, 50))
            self.frames.append(ImageTk.PhotoImage(frame))
            im.seek(i)
        self.configure(image=self.frames[self.idx])

    def run(self):
        if not running:
            return
        
        self.idx += 1
        self.idx %= self.n_frames
        frame = self.frames[self.idx]
        self.configure(image=frame)
        window.after(self.interval, self.run)

class Mouse():
    def __init__(self):
        self.left = False
        self.interval = 1000

    def run(self):
        if not running:
            return
        
        if self.left:
            pyautogui.moveRel(-1, 1)
        else:
            pyautogui.moveRel(1, -1)
        self.left = not self.left
        window.after(self.interval, self.run)

def click_event():
    global running
    if running:
        running = False
        btn["text"] = "move"
    else:
        running = True
        mouse.run()
        img.run()
        btn["text"] = "stop"

mouse = Mouse()
img = ImageLabel(window)
img.load(resource_path("running.gif"))

btn = tkinter.Button(window, text="move", command=click_event)

btn.grid(row=0, column=0, sticky="nesw")
img.grid(row=0, column=1, sticky="nesw")
window.mainloop()
