import os
import tkinter as tk
from snake import Snake
from food import Food

# Window Configuration
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 670
MAIN_CANVAS_WIDTH = 800
MAIN_CANVAS_HEIGHT = 600

def game():
    """Starts the game by initializing Food and Snake objects."""
    play_button["state"] = "disabled"  # Uncomment to disable the button during gameplay
    speed_slider["state"] = "disabled"  # Uncomment to disable the speed slider during gameplay
    score_label.config(text="Score: 1")
    score_label.place(relx=0.9, rely=0.5, anchor="e")
    food = Food(window=window, canvas=canvas)
    snake = Snake(window=window, canvas=canvas, score_label=score_label, direction="Right")
    speed = speed_var.get()
    # Bind keyboard events to control the snake's direction
    window.bind("<Up>", snake.change_direction)
    window.bind("<Down>", snake.change_direction)
    window.bind("<Left>", snake.change_direction)
    window.bind("<Right>", snake.change_direction)

    # Start the snake's movement
    while True:
        print("Sono nel loop")
        if snake.move() == False:
            print("HO CHIAMATO LA FUNZIONE GAME OVER")
            game_over()
            break
        else:
            if speed == 1:
                window.after(200)
            elif speed == 2:
                window.after(100)
            elif speed == 3:
                window.after(50)
            window.update()
        

def game_over():
    """Ends the game by deleting all canvas items and resetting the score label."""
    play_button["state"] = "normal"  # Uncomment to enable the button after the game ends
    speed_slider["state"] = "normal"  # Uncomment to enable the speed slider after the game ends
    #score_label.place_forget()
    canvas.delete("all")

    # Unbind all keyboard events
    window.unbind("<Up>")
    window.unbind("<Down>")
    window.unbind("<Left>")
    window.unbind("<Right>")

# Main application setup
if __name__ == "__main__":
    # Initialize main window
    window = tk.Tk()
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window.title("Snake")
    window.resizable(False, False)
    window.configure(background="white")

    # Create the main game canvas
    canvas = tk.Canvas(window, bg="black", width=MAIN_CANVAS_WIDTH, height=MAIN_CANVAS_HEIGHT, bd=0, highlightthickness=0, relief="ridge")
    canvas.pack()

    # Create a frame for the bottom section (score and controls)
    bottom_frame = tk.Frame(window, bg="white", height=WINDOW_HEIGHT - MAIN_CANVAS_HEIGHT)
    bottom_frame.pack(fill=tk.X)

    # Create the score canvas inside the bottom frame
    score_canvas = tk.Canvas(bottom_frame, bg="white", width=MAIN_CANVAS_WIDTH, height=WINDOW_HEIGHT - MAIN_CANVAS_HEIGHT, bd=0, highlightthickness=0, relief="ridge")
    score_canvas.pack()

    # Add a "New Game" button
    play_button = tk.Button(
        score_canvas,
        text="New Game",
        font=("Arial", 16),
        bg="white",
        fg="black",
        command=game  # Pass the function reference without parentheses
    )
    play_button.place(relx=0.1, rely=0.5, anchor="w")

    speed_var = tk.IntVar(value=2)  # Default to Medium
    speed_slider = tk.Scale(
        score_canvas,
        from_=1,
        to=3,
        orient="horizontal",
        variable=speed_var,
        showvalue=False,
        tickinterval=1,
        length=200,
        bg="white",
        fg="black",
        font=("Arial", 10),
        label="Speed",
    )
    speed_slider.place(relx=0.5, rely=0.5, anchor="center")


    # Add a score label to display the current score
    score_label = tk.Label(
        score_canvas,
        text="Score: 1",
        font=("Arial", 16),
        bg="white",
        fg="black"
    )
    score_label.place(relx=0.9, rely=0.5, anchor="e")
    score_label.place_forget()  # Hide the score label initially

    # Run the application
    window.mainloop()
