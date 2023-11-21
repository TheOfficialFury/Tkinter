import tkinter as tk


# Defines the window element.
window = tk.Tk()

# Defines a "Label" element.
label = tk.Label(text="Hey there!")
label.pack() # This makes sure the label actually displays.

# This line actually makes everything work. This is essential for the functioning of tkinter.
window.mainloop()