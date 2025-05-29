Cheat Sheet Breakdown with Canvas

1. Application Setup
   Purpose:
   Initialize the main window and configure its properties.
   What’s New:
   The Canvas widget is added to the content_frame for drawing shapes and placing widgets.

2. Global Variables
   Purpose:
   Store constants or variables that need to be accessed across multiple functions.
   What’s New:
   user_name is a StringVar bound to the Entry widget for dynamic data handling.

3. Functions
   Purpose:
   Keep the logic separate from the UI for better readability and maintainability.
   What’s New:
   on_canvas_click(event): Demonstrates how to bind mouse events to the canvas.

4. UI Layout
   Purpose:
   Define the structure and appearance of the user interface.
   What’s New:
   Canvas:
   Added a Canvas widget to the content_frame.
   Used create_rectangle(), create_oval(), and create_text() to draw shapes and text.
   Used create_window() to place widgets (like Entry and Button) inside the canvas.
   Event Binding:
   Bound the <Button-1> event (left mouse click) to the on_canvas_click() function.
   Key Features of Canvas in This Cheat Sheet
   Shapes:

Key Features of Canvas in This Cheat Sheet

Shapes:
create_rectangle(x1, y1, x2, y2, ...): Draws a rectangle.
create_oval(x1, y1, x2, y2, ...): Draws an oval or circle.
create_text(x, y, text="...", ...): Adds text to the canvas.
Widgets Inside Canvas:
create_window(x, y, window=widget): Places a widget (like Entry or Button) at specific coordinates on the canvas.

Event Binding:
canvas.bind("<event>", callback): Binds events (e.g., mouse clicks) to the canvas.

How to Expand This Template
Add Images:
image = tk.PhotoImage(file="path_to_image.png")
canvas.create_image(300, 200, image=image)

Add Scrollbars:
scrollbar = tk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.config(yscrollcommand=scrollbar.set)

Animations:
def move_shape():
canvas.move(rect, 5, 0) # Move the rectangle 5 pixels to the right
root.after(50, move_shape) # Repeat after 50ms

    rect = canvas.create_rectangle(50, 50, 200, 150, fill="blue")
    move_shape()

Best Practices
Use Frames to organize your layout into sections (e.g., header, content, footer).

    Use Canvas for custom visuals and precise positioning.

    Keep your functions modular and reusable.

    Use event binding to make your application interactive.
