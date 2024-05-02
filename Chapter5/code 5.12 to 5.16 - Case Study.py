from enum import Enum # Import the module enum
import datetime

class TaskStatus(Enum): # Enum definition for TaskStatus
 SCHEDULED = 1
 ASSIGNED = 2
 ACTIVE = 3
 COMPLETED = 4


class EmployeePosition(Enum): # Enum definition for EmployeePosition
 ACCOUNTANT = 1
 CASHIER = 2
 SALESREP = 3
 MANAGER=4

class ManagerPrivileges(Enum): # Enum definition for ManagerPrivileges
 ASSIGNTASKS=1
 EDITTASKS=2
 REMOVETASKS=3

class Task: # Class to represent the tasks in the task management system
 def __init__(self,task_id,description,status,due_date):
     self.__task_id=task_id
     self.__description=description
     self.__status=status
     self.__due_date=due_date
     self.__sub_tasks=[]

 def display_task(self):# Method to display tasks’ details
     print(f"Task ID: {self.__task_id}, Task Description: {self.__description}," 
           f"Task Status: {self.__status} Task Due Date: {self.__due_date}")
     if len(self.__sub_tasks)>0:
         print("Displaying subtasks")
         for sub_task in self.__sub_tasks:
             sub_task.display_task()

 # Several get methods to retrieve different class attribute
 def get_task_ID(self):
     return self.__task_id

 def get_task_description(self):
     return self.__description

 def get_status(self):
     return self.__status

 def get_due_date(self):
     return self.__due_date

 def get_sub_tasks(self):
     return self.__sub_tasks

 # Several set methods to update different class attributes
 def set_description(self,description):
     self.__description=description

 def set_status(self,status):
     self.__status=status

 def set_due_date(self,due_date):
     self.__due_date=due_date

 def add_sub_task(self,task): # Method to add sub task to list
     self.__sub_tasks.append(task)

 def remove_sub_task(self,task): # Method to remove sub task from list
     self.__sub_tasks.remove(task)


class Employee: # Class representing an employee in the task management system
 def __init__(self,employee_ID,first_name,last_name,position):
     self._employee_ID=employee_ID
     self._first_name=first_name
     self._last_name=last_name
     self._position=position
     self._tasks=[]

 # Get methods to access employee's ID, first name, last name, and list of task
 def get_employee_ID(self):
     return self._employee_ID

 def get_tasks(self):
     return self._tasks

 def get_first_name(self):
     return self._first_name

 def get_last_name(self):
     return self._last_name

 # Set methods to update first and last names
 def set_first_name(self,first_name):
     self._first_name=first_name

 def set_last_name(self,last_name):
     self._last_name=last_name

 def add_task(self,task): # Method that adds a task
     self._tasks.append(task)

 def remove_task(self,task_id): # Method that removes a task
     for index in range(len(self._tasks)):
         task=self._tasks[index]
         if task.get_task_ID()==task_id:
             self._tasks.pop(index)
             return
 def display_tasks(self): # Method that will print the task with an empty line
     for task in self._tasks:
         task.display_task()
         print("_"*20)


# Define a Manager class that inherits from the Employee class
class Manager(Employee):
 def __init__(self,employee_ID,first_name,last_name,position,privileges):
     # Call the constructor of the base class (Employee) using super()
     super().__init__(employee_ID,first_name,last_name,position)
     self.__privileges=privileges
     self.__employees=[]

 def add_employee(self,employee): # Method to add an employee
     self.__employees.append(employee)

 def assign_task(self,employee,task): # Method to assign a task to employee
     if ManagerPrivileges.ASSIGNTASKS in self.__privileges:
         employee.add_task(task)

 # Method to edit a task for an employee
 def edit_task(self,employee,task_id,task):
     if ManagerPrivileges.EDITTASKS in self.__privileges:
         for t in employee.get_tasks():
             if t.get_task_ID()==task_id:
                 t=task
 def remove_task(self,employee,task_id): # Method to remove a task from an employee
     if ManagerPrivileges.REMOVETASKS in self.__privileges:
         employee.remove_task(task_id)

 def get_employees(self): # Method to retrieve the list of employees
     return self.__employees

 def display_tasks(self,employee): # Method to display tasks of specific employee
     if employee in self.__employees:
         employee.display_tasks()


# Create task objects
task_1=Task(
 "TOO1","check the worksheet",TaskStatus.ACTIVE,datetime.datetime(2023, 11, 30)
)
task_1_1=Task(
 "TOO1","receive the worksheet from the sales department",
 TaskStatus.ACTIVE, datetime.datetime(2023, 11, 25)
)
task_1.add_sub_task(task_1_1)

task_2=Task(
 "TOO2","design a marketing plan for the new product",
 TaskStatus.ASSIGNED, datetime.datetime(2023, 12, 5)
)
task_3 = Task(
 "TOO3", "Review project proposals",
 TaskStatus.ACTIVE, datetime.datetime(2023, 12, 7)
)
task_4 = Task(
 "TOO4", "Prepare monthly sales report",
 TaskStatus.ASSIGNED, datetime.datetime(2023, 12, 12)
)
task_5 = Task(
 "TOO5", "Conduct employee training session",
 TaskStatus.ACTIVE, datetime.datetime(2023, 12, 9)
)
task_6 = Task(
 "TOO6", "Update inventory records",
 TaskStatus.ASSIGNED, datetime.datetime(2023, 12, 11)
)
task_7 = Task(
 "TOO7", "Plan company picnic",
 TaskStatus.ACTIVE, datetime.datetime(2023, 12, 5)
)
task_8 = Task(
 "TOO8", "Create marketing materials for the upcoming event",
 TaskStatus.ASSIGNED, datetime.datetime(2023, 12, 14)
)
task_9 = Task(
 "TOO9", "Review and update customer support guidelines",
 TaskStatus.ACTIVE, datetime.datetime(2023, 12, 8)
)
task_10 = Task(
 "TOO10", "Prepare agenda for the board meeting",
 TaskStatus.ASSIGNED, datetime.datetime(2023, 12, 13)
)

# Create Employee and Manager objects
employee_1=Employee("E001","Ahmed","Samir",EmployeePosition.SALESREP)
employee_2=Employee("E002","John","Adams",EmployeePosition.ACCOUNTANT)
employee_3=Employee("E003","Ann","Davis",EmployeePosition.ACCOUNTANT)
employee_4=Employee("E004","Sara","Smith",EmployeePosition.CASHIER)

manager_1=Manager(
 "M001","Paul","Andreson",
EmployeePosition.MANAGER,
[
ManagerPrivileges.ASSIGNTASKS,
ManagerPrivileges.EDITTASKS,
ManagerPrivileges.REMOVETASKS
])

# Assign employees to manager
manager_1.add_employee(employee_1)
manager_1.add_employee(employee_2)
manager_1.add_employee(employee_3)
manager_1.add_employee(employee_4)

# Assign tasks to employees
manager_1.assign_task(employee_1,task_1)
manager_1.assign_task(employee_1,task_4)
manager_1.assign_task(employee_2,task_2)
manager_1.assign_task(employee_2,task_3)
manager_1.assign_task(employee_2,task_10)
manager_1.assign_task(employee_3,task_5)
manager_1.assign_task(employee_3,task_6)
manager_1.assign_task(employee_3,task_8)
manager_1.assign_task(employee_3,task_9)
manager_1.assign_task(employee_4,task_7)

# Display tasks of specific employees
print("Displaying tasks of employee_1")
manager_1.display_tasks(employee_1)
print("Displaying tasks of employee_2")
manager_1.display_tasks(employee_2)

manager_1.remove_task(employee_3,task_10)
print("Displaying tasks of employee_3")
manager_1.display_tasks(employee_3)

