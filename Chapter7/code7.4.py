import tkinter as tk

class MyGUI:
 """Class to create a simple GUI window with a label and Entry in a window. """

 # Constructor
 def __init__(self):
     # Create the main window
     self.main_window = tk.Tk()
     self.main_window.title("My Window")

     # Create a label widget and pack it into the main window
     self.label=tk.Label(self.main_window, text="What is your name?")
     self.label.pack()

     # Create an entry widget with a border thickness of 3
     self.entry = tk.Entry(self.main_window, bd=3)

     # Pack the entry into the main window
     self.entry.pack()

     # Main loop to display window
     self.main_window.mainloop()


# Create an instance of the MyLabel class.
my_gui = MyGUI()
