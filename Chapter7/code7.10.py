import tkinter as tk

class PackedGUI:
  """Class to create simple GUI window"""

  # Constructor
  def __init__(self):
      # Create the main window
      self.main_window = tk.Tk()
      self.main_window.title("Phone Book")
      # Setting the size of the screen (300 width and 300 height)
      self.main_window.geometry("300x300")

      # Create widgets for the window
      # Create Label and Entry for data
      self.namelabel = tk.Label(text="Name:")
      self.nameBox = tk.Entry()
      self.phonelabel = tk.Label(text="Phone: ")
      self.phoneBox = tk.Entry()
      self.citylabel = tk.Label(text="City: ")
      self.cityBox = tk.Entry()
      # Creating buttons. The background property for windows is "bg" and in Mac systems is "highlightbackground"
      self.printbutton = tk.Button(text="Print!",
                                   fg="black", bg="white", command=self.printbox)
      self.clearbutton = tk.Button(text="Clear!", fg="white",
                               bg="black", command=self.clearbox)
      # Insert the GUI element into the window using the pack layout manager
      self.namelabel.pack()
      self.nameBox.pack(padx=12, pady=3)
      self.phonelabel.pack()
      self.phoneBox.pack(padx=12, pady=3)
      self.citylabel.pack()
      self.cityBox.pack(padx=12, pady=3)
      self.printbutton.pack(padx=12, pady=3)
      self.clearbutton.pack(padx=12, pady=3)
      # main loop to display window
      self.main_window.mainloop()

  # Print the output
  def printbox(self):
      line = self.nameBox.get() + "," + self.phoneBox.get() + "," + self.cityBox.get()
      print(line)

  # Create clear button
  def clearbox(self):
      # Clear the entry boxes
      self.nameBox.delete(0, tk.END)
      self.phoneBox.delete(0, tk.END)
      self.cityBox.delete(0, tk.END)
  
gui=PackedGUI()
