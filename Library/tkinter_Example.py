import tkinter as tk
import tkinter.filedialog as fd
import random
from PIL import Image, ImageTk
import os 

def displabel():
    kuji = ["大凶", "凶", "末吉", "小吉", "中吉", "大吉"]
    kujitext = random.choice(kuji)
    lb1.configure(text=kujitext)

def dispPhoto(path):
    newImage = Image.open(path).resize([300, 300])
    imageData = ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData 

def openFile1():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(f"ファイルパス: {fpath}")

def openFile2():
    fpath = os.path.join(os.path.dirname(__file__), "image/omikuji.png")
    dispPhoto(fpath)


root = tk.Tk()
root.title("Tkinter")
root.geometry("800x600")

lb1 = tk.Label(text="LABEL")
btn1 = tk.Button(text="PUSH", command=displabel)
btn2 = tk.Button(text="ファイルを開く", command=openFile2)
imageLabel = tk.Label()

lb1.pack()
btn1.pack()
btn2.pack()
imageLabel.pack()

root.mainloop()
