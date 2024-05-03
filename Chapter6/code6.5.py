import csv
# Opening the CSV file
file = open('users.csv', mode='r')
# Reading the CSV file
csvFile = csv.reader(file)
# Display the contents of the CSV file
for lines in csvFile:
 print(lines)
file.close()
