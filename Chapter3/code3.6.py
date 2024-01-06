try:
 # Open a file
 file = open("data1.txt", "r+")
 # Read from a file
 content = file.read()
 # Print everything in the file
 print("File content:", content)

# Catch file-related errors
except (FileNotFoundError, PermissionError, OSError) as ex:
 # ]Display User-defined error message
 print("An error occurred during file operations:")
 # Prints the message provided by the built-in error class
 print(ex)
