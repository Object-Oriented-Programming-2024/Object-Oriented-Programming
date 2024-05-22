import tkinter as tk

class FeedbackForm:
 """Class to create a feedback form GUI"""

 def __init__(self):
     # Create the main window
     self.main_window = tk.Tk()
     self.main_window.title("Feedback Form")

     # Create a label for the form title (centered)
     title_label = tk.Label(self.main_window, text="Feedback Form")
     title_label.pack(pady=(10, 0))  # Centered with 10 pixels padding at the top

     # Create a label for the name entry
     name_label = tk.Label(self.main_window, text="Enter your name:")
     name_label.pack(anchor='w', padx=10)  # Label’s positioned left with padding

     # Create an entry widget for the user's name
     self.name_entry = tk.Entry(self.main_window, width=30)
     self.name_entry.pack(anchor='w', padx=10)  # Entry’s positioned left with padding

     # Create a label for the feedback entry
     feedback_label = tk.Label(self.main_window, text="Enter your feedback:")
     feedback_label.pack(anchor='w', padx=10)  # Label’s positioned left with padding

     # Create a text widget for the user's feedback
     self.feedback_text = tk.Text(self.main_window, width=50, height=10)
     self.feedback_text.pack(anchor='w', padx=10)  # Text’s positioned left with padding

     # Main loop to display window
     self.main_window.mainloop()


# Create an instance of the FeedbackForm class
feedback_form = FeedbackForm()
