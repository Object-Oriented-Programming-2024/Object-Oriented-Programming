import tkinter as tk

class EasyWidget:
 """Class to create a GUI for selectin easiest widget"""

 def __init__(self):
     # Create the main window
     self.main_window = tk.Tk()
     self.main_window.title("Widget Preference")

     # Create a label for the question
     question_label = tk.Label(self.main_window, text="Which Tkinter widget is easier to use?")

     question_label.pack(pady=10)

     # Variable to store the selected widget
     self.widget_choice = tk.StringVar()

     # Create radio buttons for widget choices
     tk.Radiobutton(self.main_window, text="Button", variable=self.widget_choice,
                    value="Button").pack(anchor='w', padx=10)
     tk.Radiobutton(self.main_window, text="Label", variable=self.widget_choice,
                    value="Label").pack(anchor='w', padx=10)
     tk.Radiobutton(self.main_window, text="Entry", variable=self.widget_choice,
                    value="Entry").pack(anchor='w', padx=10)

     # Create a button to submit the selected radio button
     submit_button = tk.Button(self.main_window, text="Submit",command=self.submit_choice)
     submit_button.pack(pady=10)

     # Main loop to display window
     self.main_window.mainloop()

 def submit_choice(self):
     # Method to handle button click event
     chosen_widget = self.widget_choice.get()
     print("Your selected widget:", chosen_widget)


# Create an instance of the EasyWidget class
widget_easy = EasyWidget()
