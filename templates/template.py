import tkinter as tk  # Import the Tkinter library
from tkinter import ttk  # Import ttk for modern widgets (optional)

# ============================
# 1. Application Setup
# ============================
# Create the main application window
root = tk.Tk()
root.title("My Application")  # Set the window title
root.geometry("800x600")  # Set the window size (width x height)
root.resizable(False, False)  # Disable resizing (optional)

# ============================
# 2. Global Variables
# ============================
# Define any global variables or constants here
# This helps in keeping the code organized and makes it easier to manage
# Global Variables
user_name = ""  # Placeholder for user input (e.g., from an Entry widget)
# Placeholder for selected option (e.g., from radio buttons)
selected_option = 0
slider_value = 0.0  # Placeholder for slider value (e.g., from a Scale widget)
is_checked = False  # Placeholder for checkbox state (True/False)

# Global Constants
# Constants are typically defined in uppercase to distinguish them from variables
# Constants are used for values that do not change throughout the program
# This can include configuration settings, file paths, etc.
# Example Constants
APP_VERSION = "1.0.0"  # Application version (constant)
APP_NAME = "My App"  # Application name (constant)

# Tkinter Special Variables
# Stores text input dynamically (e.g., from an Entry widget)
user_name = tk.StringVar()
selected_option = tk.IntVar()  # Stores an integer value (e.g., from radio buttons)
slider_value = tk.DoubleVar()  # Stores a floating-point value (e.g., from a slider)
# Stores a boolean value (True/False, e.g., from a checkbox)
is_checked = tk.BooleanVar()

# Default Values
user_name.set("Enter your name")  # Set a default value for the Entry widget
selected_option.set(1)  # Default to the first radio button
slider_value.set(50.0)  # Default slider value
is_checked.set(False)  # Default checkbox state (unchecked)

# ============================
# 3. Functions
# ============================
# Define all your functions here to keep the logic separate from the UI
# This helps in maintaining the code and makes it easier to read
# Functions to handle button clicks, events, etc.


def on_button_click():
    """Handles the button click event."""
    print("Button clicked!")  # Print a message to the console
    label.config(text="Button clicked!")  # Update the label text


def greet_user():
    """Handles the greeting logic when the user submits their name."""
    name = user_name.get()  # Get the value from the Entry widget
    output_label.config(text=f"Hello, {name}! Welcome to {APP_NAME}!")


def clear_output():
    """Clears the output label."""
    output_label.config(text="")


def on_canvas_click(event):
    """Handles clicks on the canvas."""
    print(f"You clicked at ({event.x}, {event.y})")


# ============================
# 4. UI Layout
# ============================
# Use Frames to organize sections of the UI (optional but recommended)
header_frame = tk.Frame(root, bg="lightblue", height=100)
header_frame.pack(fill="x")  # Fill horizontally

content_frame = tk.Frame(root, bg="white")
content_frame.pack(fill="both", expand=True)

footer_frame = tk.Frame(root, bg="lightgray", height=50)
footer_frame.pack(fill="x")

# ----------------------------
# Header Section
# ----------------------------
header_label = tk.Label(
    header_frame, text="Welcome to My App", font=("Arial", 24), bg="lightblue")
header_label.pack(pady=20)

# ----------------------------
# Content Section with Canvas
# ----------------------------
# Create a Canvas
canvas = tk.Canvas(content_frame, width=600, height=400, bg="white")
canvas.pack(pady=20)

# Add Shapes to the Canvas
canvas.create_rectangle(
    50, 50, 200, 150, fill="lightblue", outline="blue", width=2)
canvas.create_oval(300, 50, 450, 150, fill="lightgreen",
                   outline="green", width=2)
canvas.create_text(150, 200, text="Canvas Example",
                   font=("Arial", 16), fill="black")

# Bind Events to the Canvas
canvas.bind("<Button-1>", on_canvas_click)  # Left mouse click

# Add an Entry Widget Inside the Canvas
name_entry = tk.Entry(root, textvariable=user_name,
                      font=("Arial", 14), width=20)
canvas.create_window(150, 100, window=name_entry)

# Add a Button Inside the Canvas
submit_button = tk.Button(
    root, text="Submit", command=greet_user, font=("Arial", 12))
canvas.create_window(150, 140, window=submit_button)

# ----------------------------
# Output Section
# ----------------------------
output_label = tk.Label(content_frame, text="", font=("Arial", 14), fg="green")
output_label.pack(pady=20)

# ----------------------------
# Footer Section
# ----------------------------
footer_label = tk.Label(footer_frame, text="© 2025 My App. All rights reserved.", font=(
    "Arial", 10), bg="lightgray")
footer_label.pack(pady=10)

# ============================
# 5. Run the Application
# ============================
# Start the Tkinter event loop
root.mainloop()
# End of the script
# ============================
