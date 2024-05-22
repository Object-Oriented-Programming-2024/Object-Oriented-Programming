import tkinter as tk

class CheckButtonForm:
 """Class to create a simple GUI with check buttons"""

 def __init__(self):
     # Create the main window
     self.main_window = tk.Tk()
     self.main_window.title("Check Button Form")

     # Create a label to ask a   question
     title_label = tk.Label(self.main_window, text="Which of the following statements do you agree with.")
     title_label.pack(anchor='w', padx=20, pady=10)  # Centered with 10 pixels padding at the top

     # Create a check button for getting a Yes or No answer to an option
     self.option0_var = tk.BooleanVar()
     option0_button = tk.Checkbutton(self.main_window, text="It is easy to create a UI with Tkinter?", variable=self.option0_var, compound="right", padx=15)
     option0_button.pack(anchor='w', padx=20)  # Check button positioned left with padding

     # Create a check button for getting a Yes or No answer to an option
     self.option1_var = tk.BooleanVar()
     option1_button = tk.Checkbutton(self.main_window, text="Tkinter provides a variety of widgets for UI design.", variable=self.option1_var,compound="left", padx=15)
     option1_button.pack(anchor='w', padx=20)  # Check button positioned left with padding

     # Create a button to submit response
     submit_button = tk.Button(self.main_window, text="Submit", command=self.submit_response)
     submit_button.pack(pady=10)  # Add some padding below the button

     # Main loop to display window
     self.main_window.mainloop()

 def submit_response(self):
     # Method to handle button click event
     if self.option0_var.get():
         print(f"For Option 1 User Selected: Yes")
     else:
         print(f"For Option 1 User Selected: No")

     if self.option1_var.get():
         print(f"For Option 2 User Selected: Yes")
     else:
          print(f"For Option 2 User Selected: No")


# Create an instance of the CheckButtonForm class
check_button_form = CheckButtonForm()
