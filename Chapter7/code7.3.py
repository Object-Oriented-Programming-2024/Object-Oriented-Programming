import tkinter as tk

class MyGUI:
 """Class to create a simple GUI window with a label window"""

 # Constructor
 def __init__(self):
     # Create the main window
     self.main_window = tk.Tk()
     self.main_window.title("My Window")

     # Create a label widget
     self.label=tk.Label(self.main_window, text="My first Label")

     # Pack the label widget into the main window
     self.label.pack()

     # Main loop to display window
     self.main_window.mainloop()


# Create an instance of the MyLabel class.
my_gui = MyGUI()
