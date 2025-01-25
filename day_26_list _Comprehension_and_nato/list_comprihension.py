# Read the contents of file1.txt
with open("/Users/sudipto/Documents/code/projects/100days of code/day_26_list _Comprehension_and_nato/file1.txt") as file1:
    file1_numbers = file1.readlines()

# Read the contents of file2.txt
with open("/Users/sudipto/Documents/code/projects/100days of code/day_26_list _Comprehension_and_nato/file2.txt") as file2:
    file2_numbers = file2.readlines()

# Convert the contents to lists of integers
file1_numbers = [int(num.strip()) for num in file1_numbers]
file2_numbers = [int(num.strip()) for num in file2_numbers]

# Find the common numbers using list comprehension
result = [num for num in file1_numbers if num in file2_numbers]

# Print the result
print(result)