import click
from PIL import ImageTk
import tkinter as tk


# Creates the output window presenting the edited image and a button to save the result
# https://www.perplexity.ai/search/f5473391-9100-45d3-89e5-6db22069a25e?s=c
def spawn_output_window(image, image_path):
    # Display the result
    root = tk.Tk()
    root.title(f"Edited {image_path}")

    # Result image
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.pack()

    # Save button
    button = tk.Button(root, text="Save", command=lambda: save_image(image, "output.png"))
    button.pack()

    root.mainloop()


# Prints the result and saves the image
def save_image(image, filename):
    click.echo(f"Saving image as {filename}...")
    image.save(filename)
