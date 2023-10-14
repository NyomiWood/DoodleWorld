import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import random

def create_tooltip(widget, text):
    def show_tooltip(event):
        tooltip.config(text=text)
        tooltip.place(x=widget.winfo_x() + widget.winfo_width(), y=widget.winfo_y())

    def hide_tooltip(event):
        tooltip.place_forget()

    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)

    tooltip = tk.Label(root, text="", background="lightyellow", relief="solid")
    return tooltip

def exit_application():
    root.destroy()

def open_window_one():
    window_one = tk.Toplevel(root)
    window_one.geometry("700x900")
    window_one.title("Doodle Prompts")

    # Create a Text widget for displaying drawing prompts
    prompts = [
        "Draw a smiling sun.",
        "Sketch your favorite animal.",
        "Create a simple landscape.",
        "Draw a cup of coffee.",
        "Sketch a happy face.",
        "Illustrate a flying bird.",
        "Draw your favorite fruit.",
        "Sketch a cozy house.",
        "Create a beautiful flower.",
        "Illustrate a friendly monster."
    ]

    prompt_text = "\n".join(prompts)  # Combine prompts into one string with line breaks

    prompt_box = tk.Text(window_one, wrap=tk.WORD, width=40, height=10)
    prompt_box.insert(tk.END, prompt_text)
    prompt_box.pack()

    back_to_original_btn = tk.Button(window_one, text="Back to Original Window", command=root.deiconify)
    back_to_original_btn.pack()

    label = tk.Label(window_one, text="Pick one of these ten drawing prompts!")
    label.pack()

def open_window_two():
    window_two = tk.Toplevel(root)
    window_two.geometry("700x900")
    window_two.title("Color Generator")

    # Create a label for displaying the random color
    color_label = tk.Label(window_two, text="", width=20, height=5)
    color_label.pack()

    def generate_random_color():
        # Generate random RGB values
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        # Create a hexadecimal color string
        color = f'#{red:02X}{green:02X}{blue:02X}'

        # Set the background color of the label
        color_label.configure(bg=color)
        color_label.config(text=f'Color: {color}')

    # Create a "Generate" button
    generate_button = tk.Button(window_two, text="Generate", command=generate_random_color)
    generate_button.pack()

    back_to_original_btn = tk.Button(window_two, text="Back to Original Window", command=root.deiconify)
    back_to_original_btn.pack()

    label = tk.Label(window_two, text="Here, you will be able to generate any color!")
    label.pack()

def open_contact_us():
    contact_us_window = tk.Toplevel(root)
    contact_us_window.geometry("700x900")
    contact_us_window.title("Contact Us")

    back_to_original_btn = tk.Button(contact_us_window, text="Back to Original Window", command=root.deiconify)
    back_to_original_btn.pack()

    # Add content to the "Contact Us" window
    contact_us_label = tk.Label(contact_us_window, text="You can contact us at doodleword@finalproject.com", font="Railway")
    contact_us_label.pack()

    exit_btn = tk.Button(contact_us_window, text="Exit", command=exit_application, font="Railway", bg="#FF5733", fg="white", height=2, width=15)
    exit_btn.pack()

root = tk.Tk()
root.geometry("700x900")  # Adjust the window size to better accommodate the buttons

canvas = tk.Canvas(root, width=700, height=300)
canvas.grid(columnspan=4)  # Set columnspan to 4 for the canvas

# Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0, columnspan=2)  # Center the logo by using columnspan 2

# Create a tooltip for the logo
create_tooltip(logo_label, "DoodleWorld Logo")

# Instructions
instructions = tk.Label(root, text="Select a window to look into our services.", font="Railway")
instructions.grid(columnspan=4, column=0, row=1)  # Set columnspan to 4

# New Window Buttons
open_window_one_btn = tk.Button(root, text="Window One", command=open_window_one, font="Railway", bg="#20bebe", fg="white", height=2, width=15)
open_window_one_btn.grid(column=1, row=4, padx=20, pady=10)  # Add spacing under the button using padx and pady

open_window_two_btn = tk.Button(root, text="Window Two", command=open_window_two, font="Railway", bg="#20bebe", fg="white", height=2, width=15)
open_window_two_btn.grid(column=2, row=4, padx=20, pady=10)  # Place the second button in column 2 and add spacing

canvas = tk.Canvas(root, width=700, height=200)
canvas.grid(columnspan=4)  # Set columnspan to 4 for the canvas

doodle_image = Image.open("doodle.png")
doodle_image = ImageTk.PhotoImage(doodle_image)
doodle_label = tk.Label(image=doodle_image)
doodle_label.image = doodle_image
doodle_label.grid(columnspan=4, row=5)
create_tooltip(doodle_label, "Royalty free doodle art by Titatu_Art")

contact_us_btn = tk.Button(root, text="Contact Us", command=open_contact_us, font="Railway", bg="#20bebe", fg="white", height=2, width=15)
contact_us_btn.grid(column=1, row=6, columnspan=2, padx=20, pady=10)

root.mainloop()
