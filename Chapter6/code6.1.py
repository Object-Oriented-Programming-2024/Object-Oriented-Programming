# Opening the file for read using 'r' mode
file1 = open('email.txt', 'r')

# Read all the data in the file
file_data = file1.read()

# Close the file
file1.close()

# Print all the data read from the file
print(file_data)
