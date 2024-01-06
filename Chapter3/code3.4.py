# Create a list of numbers
nums = [2, 4, 6, 8, 10]
print(nums)
# Input: Get a position in the list
position = int(input("Choose the position in the list: "))
# Input: Get denominator for division
denominator = int(input("Choose a number to divide your choice with: "))
# Process: Divide the value from the list with the denominator
result = nums[position] / denominator
# Output: Display output
print(f"Your choice {nums[position]} divided by {denominator} is: ", result)
