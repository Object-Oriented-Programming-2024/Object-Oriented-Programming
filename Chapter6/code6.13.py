import pickle

# Open file for binary reading
inputfile = open('phonedata.dat', 'rb')

# Unpickle the object from the file
pb = pickle.load(inputfile)

# Print the dictionary
print(pb)

# Close the file
inputfile.close()
