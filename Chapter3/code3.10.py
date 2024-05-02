try:
 # Create a list of numbers
 nums = [2, 4, 6, 8, 10]
 print(nums)
 # Input: Get position in list
 position = int(input("Choose the position in the list: "))
 # Input: Get denominator for division
 denominator = int(input("Choose a number to divide your choice with: "))
 # Process: Divide the value from list with denominator
 result = nums[position] / denominator
except IndexError as ex:
 print("Position should be between 0 and 4 only.", ex)
except ZeroDivisionError as ex:
 print("Denominator cannot be 0.", ex)
except:
 print("Something went wrong.")
else:
 # Output: Display output
 print(f"Your choice {nums[position]} divided by {denominator} is: ", result)
finally: # This clause will run whether an exception occurred or no
 print("Bye")
