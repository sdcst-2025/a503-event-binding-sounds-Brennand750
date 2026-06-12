import tkinter as tk
from tkinter import *
import playsound as p

def playsound(event):
    print(event)
    p.playsound("animals_dogs_x2_barking_small_001.mp3")
def playsound2 (event2):
    print(event2)
    p.playsound("cow-moo.mp3")
def playsound3 (event3):
    print(event3)
    p.playsound("dragon-studio-chicken-sounds-487676.mp3")
def playsound4 (event4):
    print(event4)
    p.playsound("stu9-sheep-352668.mp3")


win = tk.Tk()
win.title("Sound board")
win.attributes('-topmost', True)
win.geometry("750x500")
imagedog= PhotoImage(file="Dog.png")
imagechicken = PhotoImage(file="Chicken.png")
imagecow=PhotoImage(file="Cow.png")
imagesheep=PhotoImage(file="Sheep.png")

l1 = tk.Label(win,width=125, text="dog", image=imagedog, compound="top" )
l2 = tk.Label(win,width=100, text="chicken", image=imagechicken, compound="top")
l3 = tk.Label(win,width=100, text="cow", image=imagecow, compound="top")
l4 = tk.Label(win,width=120, text="sheep", image=imagesheep, compound="top")


b1 =  tk.Button(win,text="Click to play", width=10, command="playsound")
b1.bind("<Button>",playsound)
b2= tk.Button(win,text="Click to play", width=10, command="playsound")
b2.bind("<Button>", playsound2)
b3 =  tk.Button(win,text="Click to play", width=10, command="playsound")
b3.bind("<Button>", playsound3)
b4 =  tk.Button(win,text="Click to play", width=10, command="playsound")
b4.bind("<Button>", playsound4)

l1.place(x=25,y=150)
b1.place(x=50, y=300)
l2.place(x=400, y=150)
b2.place(x=225,y=300)
l3.place(x=200,y=150)
b3.place(x=425,y=300)
l4.place(x=530, y=50)
b4.place(x=550, y=300)


win.mainloop()
