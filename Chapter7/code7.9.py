import tkinter as tk
from tkinter import ttk


class EasyWidget:
 """Class to create a GUI for widget preference"""

 def __init__(self):
     # Create the main window
     self.main_window = tk.Tk()
     self.main_window.title("Widget Preference")

     # Create a label for the question
     question_label = tk.Label(self.main_window, text="Which Tkinter widget is easier to use?")

     question_label.pack(pady=10,padx=10)

     # Create a ComboBox for widget choices
     self.widget_choices = ttk.Combobox(self.main_window, values=["Button", "Label", "Entry"])

     self.widget_choices.pack(anchor='center', padx=10)

     # Create a button to submit the choice
     submit_button = tk.Button(self.main_window, text="Submit", command=self.submit_choice)
     submit_button.pack(pady=10)

     # Main loop to display window
     self.main_window.mainloop()

 def submit_choice(self):
     # Method to handle button click event
     chosen_widget = self.widget_choices.get()
     print("Your preferred widget:", chosen_widget)


# Create an instance of the WidgetPreference class
widget_easy = EasyWidget()
