import tkinter as tk
import random
from food import Food

class Snake:

    def __init__(self, window, canvas, score_label, direction):
        print("Hi, I am the snake!")
        self.window = window
        self.canvas = canvas
        self.score_label = score_label
        self.direction = direction
        self.len = 1
        x_init = 0
        y_init = 0
        self.shape = []
        for i in range(self.len):
            self.shape.append(self.canvas.create_rectangle(x_init+(20*i), y_init, x_init+(20*i)+20, y_init+20, fill="green"))
        self.head_coords = canvas.coords(self.shape[-1])
        self.tail_coords = canvas.coords(self.shape[0])
    

    def update_head_and_tail_coords(self):
        """Updates head and tail coordinates after a move."""
        self.head_coords = self.canvas.coords(self.shape[-1])
        self.tail_coords = self.canvas.coords(self.shape[0])

    def append_head(self):
        if self.direction == "Right":
            self.shape.append(self.canvas.create_rectangle(self.head_coords[0]+20, self.head_coords[1], self.head_coords[2]+20, self.head_coords[3], fill="green"))
        elif self.direction == "Left":
            self.shape.append(self.canvas.create_rectangle(self.head_coords[0]-20, self.head_coords[1], self.head_coords[2]-20, self.head_coords[3], fill="green"))
        elif self.direction == "Up":
            self.shape.append(self.canvas.create_rectangle(self.head_coords[0], self.head_coords[1]-20, self.head_coords[2], self.head_coords[3]-20, fill="green"))
        elif self.direction == "Down":
            self.shape.append(self.canvas.create_rectangle(self.head_coords[0], self.head_coords[1]+20, self.head_coords[2], self.head_coords[3]+20, fill="green"))     

    def move(self):
        print(self.shape)
        if self.check_collision():
           return False
        if not self.eat():
            tail = self.shape.pop(0)  # Remove the tail from the shape list
            self.canvas.delete(tail)  # Delete the tail rectangle from the canvas
        self.append_head()
        self.update_head_and_tail_coords()
        return True
        '''
        if self.speed == 1:
            self.window.after(200, self.move)
        elif self.speed == 2:
            self.window.after(100, self.move)
        elif self.speed == 3:
            self.window.after(50, self.move)
        '''
    
    def change_direction(self, event):
        print("event: %s" % event)
        if event.keysym == "Up" and self.direction != "Down":
            self.direction = "Up"
        if event.keysym == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif event.keysym == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif event.keysym == "Right" and self.direction != "Left":
            self.direction = "Right"

    def eat(self):
        x1, y1, x2, y2 = self.head_coords
        overlaps = self.canvas.find_overlapping(x1, y1, x2, y2)
        list_overlaps = list(overlaps)
        for item in list_overlaps:
            x3, y3, x4, y4 = self.canvas.coords(item)
            if self.canvas.type(item) == "oval" and not(x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1):
                print("Eating food")
                self.canvas.delete(item)
                self.len +=1
                self.score_label.config(text="Score: {}".format(self.len))
                Food(self.window, self.canvas)
                return True
        return False
    

    def check_collision(self):
        canvas_width = self.canvas.winfo_reqwidth()
        canvas_height = self.canvas.winfo_reqheight()
        x1, y1, x2, y2 = self.head_coords
        # Check collision with the body (excluding the head)
        for segment in self.shape[:-1]:  # Exclude the current head
            x3, y3, x4, y4 = self.canvas.coords(segment)
            if not (x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1):  # Overlap condition
                print("Game over! Hit itself" +". Segment: " +str(segment))
                self.score_label.config(text="Game over!")
                return True
        if x1 < 0 or x2 > canvas_width or y1 < 0 or y2 > canvas_height:
            print("Game over. Hit the wall!")
            self.score_label.config(text="Game over!")
            return True
        return False   
