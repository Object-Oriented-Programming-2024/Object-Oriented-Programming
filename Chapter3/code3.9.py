try:
 # Create a list of numbers
 nums = [2, 4, 6, 8, 10]
 print(nums)
 # Input: Get a position in the list
 position = int(input("Choose the position in the list: "))
 # Input: Get denominator for division
 denominator = int(input("Choose a number to divide your choice with: "))
 # Process: Divide the value from the list with the denominator
 result = nums[position] / denominator
except IndexError as ex:
 print("Position should be between 0 and 4 only.", ex)
except ZeroDivisionError as ex:
 print("Denominator cannot be 0.", ex)
except:
 print("Something went wrong.")
else: # This clause will execute only when there are no exceptions raised
 # Output: Display result
 print(f"Your choice {nums[position]} divided by {denominator} is: ", result)
