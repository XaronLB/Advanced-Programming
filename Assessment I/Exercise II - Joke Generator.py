from tkinter import *
import random

root = Tk()
root.title("Joke Generator")
root.geometry("500x300")

# Load jokes from file
def load_jokes(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return ["Jokes file not found!"]

# Load jokes from jokes.txt
jokes = load_jokes("jokes.txt")

# Function to display a random joke
def show_joke():
    joke_label.config(text=random.choice(jokes))

# Add joke text label
joke_label = Label(root, text="Click to button for the funnies", wraplength=450, font=("Cascadia Code", 24))
joke_label.pack(pady=20)

# Button to get a joke
joke_button = Button(root, text="Tell me a joke!", command=show_joke, font=("Cascadia Code", 24),
                     fg="white",
                     bg="darkblue")
joke_button.pack()

# Run the UI
root.mainloop()
