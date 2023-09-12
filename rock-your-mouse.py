import pyautogui
import tkinter
from PIL import Image, ImageTk
import os
import sys
import tkinter.font as font

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

running = False


class ImageLabel(tkinter.Label):
    def load(self, image_path):
        self.running_interval = 40
        self.default_interval = 200

        self.idx = 0
        im = Image.open(image_path)

        self.frames = []
        for i in range(im.n_frames):
            frame = im.copy().resize((100, 100))
            self.frames.append(ImageTk.PhotoImage(frame))
            im.seek(i)
        self.frames = self.frames[1:]
        self.n_frames = len(self.frames)
        self.run()

    def run(self):       
        self.idx += 1
        self.idx %= self.n_frames
        frame = self.frames[self.idx]
        self.configure(image=frame)
        if running:
            window.after(self.running_interval, self.run)
        else:
            window.after(self.default_interval, self.run)

class Mouse():
    def __init__(self):
        self.left = False
        self.interval = 700

    def run(self):
        if not running:
            return
        
        if self.left:
            pyautogui.moveRel(1, -1)
        else:
            pyautogui.moveRel(-1, 1)
        self.left = not self.left
        window.after(self.interval, self.run)

def click_event():
    global running
    if running:
        running = False
        btn["text"] = "Let's Rock!"
    else:
        running = True
        mouse.run()
        btn["text"] = "Stop!"

mouse = Mouse()
img = ImageLabel(window)
img.load(resource_path("rock-dog.gif"))

btn = tkinter.Button(window, text="Let's Rock!", command=click_event, font=font.Font(size=20, weight="bold"))

btn.grid(row=0, column=0, sticky="nesw")
img.grid(row=0, column=1, sticky="nesw", padx=(15, 15), pady=(15, 15))
window.mainloop()
