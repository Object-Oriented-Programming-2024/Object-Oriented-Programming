import tkinter as tk

class PlaceGUI:
  """Class to create simple GUI window"""

  # Constructor
  def __init__(self):
      # Create the main window
      self.main_window = tk.Tk()
      self.main_window.title("Phone Book")

      # Create widgets for the window
      self.namelabel = tk.Label(text="Name:")
      self.nameBox = tk.Entry()
      self.phonelabel = tk.Label(text="Phone: ")
      self.phoneBox = tk.Entry()
      self.citylabel = tk.Label(text="City: ")
      self.cityBox = tk.Entry()

      # Create the print button: The background property for windows is "bg" and in Mac systems is "highlightbackground"
      self.printbutton = tk.Button(text="Print!", fg="black",
                                   bg="white", command=self.printbox)
      # Create the clear button
      self.clearbutton = tk.Button(text="Clear!", fg="white",
                                   bg="black", command=self.clearbox)

      # Insert the GUI element into the window using the place layout manager
      self.namelabel.place(x=0,  y=0)
      self.nameBox.place(x=50,  y=0)
      self.phonelabel.place(x=0, y=40)
      self.phoneBox.place(x=50, y=40)
      self.citylabel.place(x=0, y=80)
      self.cityBox.place(x=50, y=80)
      self.clearbutton.place(x=80, y=120)
      self.printbutton.place(x=130, y=120)

      # main loop to display window
      self.main_window.mainloop()

  def printbox(self):
      line = self.nameBox.get() + "," + self.phoneBox.get() + "," + self.cityBox.get()
      print(line)


  def clearbox(self):
      # Clear the entry boxes
      self.nameBox.delete(0, tk.END)
      self.phoneBox.delete(0, tk.END)
      self.cityBox.delete(0, tk.END)


# Create an instance of the MyGUI class.
gui=PlaceGUI()
