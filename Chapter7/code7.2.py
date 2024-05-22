import tkinter as tk


class MyFrames:
 """Class to demonstrate the use of the Frames in Windows"""

 def __init__(self):
     # Create the main Window
     self.main_window = tk.Tk()
     self.main_window.title("My Window")

     # Create two frames for the window
     self.top_frame = tk.Frame(
         self.main_window, highlightthickness=2, highlightbackground="blue"
     )
     self.bottom_frame = tk.Frame(
         self.main_window, highlightthickness=2, highlightbackground="red"
     )
     # Pack the two frames into the window
     self.top_frame.pack(padx=10, pady=10)
     self.bottom_frame.pack(padx=10, pady=10)

     # Create a label in each frame and pack it in
     top_label = tk.Label(self.top_frame, text="Frame 1", width=70, height=20)
     top_label.pack()
     bottom_label = tk.Label(self.bottom_frame, text="Frame 2", width=70, height=20)
     bottom_label.pack()

     self.main_window.mainloop()


# Create an object to show the GUI
show_window = MyFrames()
