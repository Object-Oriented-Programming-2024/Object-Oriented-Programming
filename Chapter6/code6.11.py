import pickle

# Dictionary for phone book
phonebook = {
         'Javed': '507937682',
         'James': '559038281',
         'Joanne': '509073672'}

# Open file for binary writing
outputfile = open('phonedata.dat', 'wb')

# Pickle the object to the file
pickle.dump(phonebook, outputfile)

# Close the file
outputfile.close()
