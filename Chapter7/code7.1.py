import tkinter as tk

class MyGUI:
 """Class to create simple GUI window"""

 # Constructor
 def __init__(self):
     # Create the main window
     self.main_window = tk.Tk()

     # Main loop to display window
     self.main_window.mainloop()


# Create an instance of the MyGUI class.
my_gui = MyGUI()
