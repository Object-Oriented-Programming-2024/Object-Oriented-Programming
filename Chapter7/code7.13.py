import tkinter as tk

class MyCalc:
     """Class to represent calculator layout"""

     # Constructor
     def __init__(self):
         # Create the window
         self.main_window = tk.Tk()
         self.main_window.title("My Calculator")

         # Create two frames inside the window
         self.top_frame = tk.Frame(self.main_window)
         self.bottom_frame = tk.Frame(self.main_window)

         # Entry in the top frame
         self.entry = tk.Entry(self.top_frame, width=25, justify="right")
         self.entry.grid(row=0, columnspan=4, sticky="W")

         # Buttons in the bottom frame and in grid layout
         self.cls = tk.Button(self.bottom_frame, text="Clear", width=4)
         self.cls.grid(row=1, column=0)
         self.bck = tk.Button(self.bottom_frame, text="", width=4)
         self.bck.grid(row=1, column=1)
         self.lbl = tk.Button(self.bottom_frame, text="", width=4)
         self.lbl.grid(row=1, column=2)
         self.clo = tk.Button(self.bottom_frame, text="Close")
         self.clo.grid(row=1, column=3)
         self.sev = tk.Button(self.bottom_frame, text="7", width=4)
         self.sev.grid(row=2, column=0)
         self.eig = tk.Button(self.bottom_frame, text="8", width=4)
         self.eig.grid(row=2, column=1)
         self.nin = tk.Button(self.bottom_frame, text="9", width=4)
         self.nin.grid(row=2, column=2)
         self.div = tk.Button(self.bottom_frame, text="/", width=4)
         self.div.grid(row=2, column=3)

         self.fou = tk.Button(self.bottom_frame, text="4", width=4)
         self.fou.grid(row=3, column=0)
         self.fiv = tk.Button(self.bottom_frame, text="5", width=4)
         self.fiv.grid(row=3, column=1)
         self.six = tk.Button(self.bottom_frame, text="6", width=4)
         self.six.grid(row=3, column=2)
         self.mul = tk.Button(self.bottom_frame, text="*", width=4)
         self.mul.grid(row=3, column=3)

         self.one = tk.Button(self.bottom_frame, text="1", width=4)
         self.one.grid(row=4, column=0)
         self.two = tk.Button(self.bottom_frame, text="2", width=4)
         self.two.grid(row=4, column=1)
         self.thr = tk.Button(self.bottom_frame, text="3", width=4)
         self.thr.grid(row=4, column=2)
         self.mns = tk.Button(self.bottom_frame, text="-", width=4)
         self.mns.grid(row=4, column=3)

         self.zer = tk.Button(self.bottom_frame, text="0", width=4)
         self.zer.grid(row=5, column=0)
         self.dot = tk.Button(self.bottom_frame, text=".", width=4)
         self.dot.grid(row=5, column=1)
         self.equ = tk.Button(self.bottom_frame, text="=", width=4)
         self.equ.grid(row=5, column=2)
         self.pls = tk.Button(self.bottom_frame, text="+", width=4)
         self.pls.grid(row=5, column=3)

         # Pack both the frames
         self.top_frame.pack()
         self.bottom_frame.pack()

         # Display window and keep focus
         self.main_window.mainloop()

# Create an object of the calculator
mycal = MyCalc()
