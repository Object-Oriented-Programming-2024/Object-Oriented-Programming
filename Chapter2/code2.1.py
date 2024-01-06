#Technique 1:
color_names = ["red", "orange", "black", "white", "red"] # Create a list of color names
print(color_names)  #Print the list
#Technique 2:
student_grades = []  #Create an empty list
student_grades.append(89)  #Add an item to the end of the list
student_grades.append(55)
student_grades.append(68)
student_grades.append(83)
student_grades.append(93)
print(student_grades)  #Print the list
#Technique 3:
diverse_list=[]  #Create an empty list with different types of data types
diverse_list.insert(0,"Adam Smith")  #Add an item at index 0
diverse_list.insert(1, 125923)
diverse_list.insert(2, 125971)
diverse_list.insert(3, "Ann Davis")
print(diverse_list) #Print the list

# The below code lines show the different techniques to delete an element from a list.
student_grades.pop() # Delete the last element of list “student_grades”
student_grades.pop(1) # Delete element of index 1 in “student_grades” corresponding to “55”
diverse_list.remove(125923) # Delete a specific element from diverse_list.
del diverse_list[-1] # Delete the element with index -1 : the last element in the list
