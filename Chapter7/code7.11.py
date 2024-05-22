import tkinter as tk

class GridGUI:
  """Class to create simple GUI window"""

  # Constructor
  def __init__(self):
      # Create the main window
      self.main_window = tk.Tk()
      self.main_window.title("Phone Book")
      # Setting the size of the screen (250 width and 200 height)
      self.main_window.geometry("250x200")

      # Create widgets for the window
      # Create Label and Entry for data
      self.namelabel = tk.Label(text="Name:")
      self.nameBox = tk.Entry()
      self.phonelabel = tk.Label(text="Phone: ")
      self.phoneBox = tk.Entry()
      self.citylabel = tk.Label(text="City: ")
      self.cityBox = tk.Entry()

      # Create a print button: The background property for windows is "bg" and in Mac systems is "highlightbackground"
      self.printbutton = tk.Button(text="Print!", fg="black",
                                   bg="white", command=self.printbox)
      # Create clear button
      self.clearbutton = tk.Button(text="Clear!", fg="white",
                                   bg="black", command=self.clearbox)

      # Insert the GUI element into the window using the grid layout manager
      self.namelabel.grid(row=0, column=0, padx=10, pady=10)
      self.nameBox.grid(row=0, column=1, padx=10, pady=10)
      self.phonelabel.grid(row=1, column=0,padx=10, pady=10)
      self.phoneBox.grid(row=1, column=1,padx=10, pady=10)
      self.citylabel.grid(row=2, column=0,padx=10, pady=10)
      self.cityBox.grid(row=2, column=1,padx=10, pady=10)
      self.printbutton.grid(row=3, column=1,padx=10, pady=10, sticky="e")
      self.clearbutton.grid(row=3, column=1,padx=10, pady=10, sticky="w")

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
gui=GridGUI()
