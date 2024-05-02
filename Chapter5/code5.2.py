class Employee:
 def __init__(self, emp_id, first_name, last_name):
     self.__employeeID = emp_id
     self.__firstName = first_name
     self.__lastName = last_name
     self.__tasks_assigned = []  # List to store tasks assigned to the employee

 def get_full_name(self):
     return f"{self.__firstName} {self.__lastName}"

 def assign_task(self, task):
     #adding the task to the employee task list
     self.__tasks_assigned.append(task)
     #updating the task attribute __assigned_employee
     task.assign_to_employee(self)

 def get_assigned_tasks(self):
    return self.__tasks_assigned

 def display_info(self):
     print(f"Employee ID: {self.__employeeID} || Name: {self.get_full_name()}" 
           f"\nAssigned Tasks:")
     for task in self.__tasks_assigned:
         task.display_info()
     print("_"*100)


class Task:
 def __init__(self, task_id, deadline, description):
     self.__taskID = task_id
     self.__deadline = deadline
     self.__description = description
     self.__assigned_employee = None  # Employee to whom the task is assigned

 def assign_to_employee(self, employee):
     self.__assigned_employee = employee

 def display_info(self):
     assigned="Not assigned"
      #Add the name of the employee if a task has been assigned to an Employee
     if self.__assigned_employee!=None:
         assigned=self.__assigned_employee.get_full_name()
     print(f"Task ID: {self.__taskID} || Deadline: {self.__deadline} ||"
           f"Description: {self.__description} || Assigned to: {assigned}")


# Example Usage:
# Creating employees
employee1 = Employee(1, "Andrew", "Baker")
employee2 = Employee(2, "Sarah", "Williams")

# Creating tasks
task1 = Task(101, "2024-01-15", "Code Login Screen")
task2 = Task(102, "2024-01-20", "Code Home Screen")
task3 = Task(103, "2024-01-25", "Code Adding Screen")

# Assigning tasks to employees
employee1.assign_task(task1)
employee1.assign_task(task2)

# Displaying an Employee's information
employee1.display_info()

#Display Task3 assigned to no Employee
task3.display_info()

