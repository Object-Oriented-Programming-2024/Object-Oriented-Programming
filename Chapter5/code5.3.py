class Task: # Task Class that represents a main class with subtasks.
 def __init__(self, task_id, deadline, description):
     self.__taskID = task_id
     self.__deadline = deadline
     self.__description = description
     self.__subtasks = []  # List to store subtasks

 #Adding a subtask to the list
 def add_subtask(self, task):
     #Adding a subtask to the list
     self.__subtasks.append(task)

 def display_info(self):
     print(f"Task ID: {self.__taskID} || Deadline: {self.__deadline} ||"
           f"Description: {self.__description}")
     if self.__subtasks: # Check if there are subtasks
         print("Subtasks:")
         for task in self.__subtasks: # Display information for each subtask
             task.display_info()


# Creating a main task
maintask = Task(100, "2024-01-10", "Website Design for SOM")

# Creating subtasks
subtask1 = Task(101, "2024-01-15", "Homepage development")
subtask2 = Task(102, "2024-01-20", "Payment Request development")

# Add subtasks to the main task
maintask.add_subtask(subtask1)
maintask.add_subtask(subtask2)

# Display details for the main task including subtasks
maintask.display_info()
