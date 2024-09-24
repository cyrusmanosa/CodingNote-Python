import tkinter as tk
import random
from PIL import Image, ImageTk
import os 

def disPhoto(path):
    newImage = Image.open(path).resize([200,300])
    imageDate = ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageDate)
    imageLabel.image = imageDate

def omikuji():
    kujiFileName = ["daikiti.png", "tyukiti.png", "syokiti.png", "kyo.png"]
    firename = random.choice(kujiFileName)
    fpath = os.path.join(os.path.dirname(__file__), "image", firename) 
    disPhoto(fpath)

root = tk.Tk()
root.geometry("800x600")

btn = tk.Button(text="おみくじを引く", command=omikuji)
imageLabel = tk.Label()

btn.pack()
imageLabel.pack()

root.mainloop()
