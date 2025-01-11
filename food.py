import tkinter as tk
import random

class Food:

    def __init__(self, window, canvas):
        print("Hi, I am a food!")
        canvas_width = canvas.winfo_reqwidth()
        canvas_height = canvas.winfo_reqheight()
        x = random.randrange(0, canvas_width, 20)
        y = random.randrange(0, canvas_height, 20)
        shape = canvas.create_oval(x, y, x+20, y+20, fill="red")
    
