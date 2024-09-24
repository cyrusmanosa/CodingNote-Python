import tkinter as tk
import random
from PIL import Image, ImageTk
import os 

def disPhoto(path,num):
    newImage = Image.open(path).resize([200,200])
    imageDate = ImageTk.PhotoImage(newImage)
    if num == 0:
        imageLabel1.configure(image=imageDate)
        imageLabel1.image = imageDate
    elif num == 1:
        imageLabel2.configure(image=imageDate)
        imageLabel2.image = imageDate
    elif num == 2:
        imageLabel3.configure(image=imageDate)
        imageLabel3.image = imageDate

def dice():
    kujiFileName = ["dice01.png", "dice02.png", "dice03.png", "dice04.png","dice05.png","dice06.png"]
    for i in range(3):
        firename = random.choice(kujiFileName)
        fpath = os.path.join(os.path.dirname(__file__), "image", firename) 
        disPhoto(fpath,num=i)

root = tk.Tk()
root.geometry("800x600")
frame = tk.Frame(root)


btn = tk.Button(text="サイコロを振る", command=dice)
imageLabel1 = tk.Label(frame)
imageLabel2 = tk.Label(frame)
imageLabel3 = tk.Label(frame)

btn.pack()
frame.pack()
imageLabel1.pack(side=tk.LEFT)
imageLabel2.pack(side=tk.LEFT)
imageLabel3.pack(side=tk.LEFT)

root.mainloop()
