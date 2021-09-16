# Import module random
import random

# Generate list of 100 random numbers from 0 to 1000
randomlist = random.sample(range(0, 1000), 100)

# Output of generated list
print("Random list\n", randomlist)

# Create empty list for sorted numbers
sorted_list = []

# While random list is not empty do
while randomlist:
    # Variable min gets value of first list element
    min_value = randomlist[0]
    # Go through the random list and compare each number with min
    for x in randomlist:
        # If some element is less than min
        if x < min_value:
            min_value = x  # Variable min gets value of element
    sorted_list.append(min_value)  # Add min to sorted list
    randomlist.remove(min_value)  # Remove element from random list

# Output of sorted list
print("Sorted list\n", sorted_list)

# Set 0 value for variables
even_sum = 0
even_count = 0
odd_sum = 0
odd_count = 0

# Go through the sorted list
for i in sorted_list:
    # Find even or odd number
    if i % 2 == 0:
        even_sum += int(i)  # increase even sum
        even_count += 1  # increase even count
    else:
        odd_sum += int(i)  # increase odd sum
        odd_count += 1  # increase odd count

# Print out averages for even and odd numbers
print("Even Average: " + str(int(even_sum) / int(even_count)))
print("Odd Average: " + str(int(odd_sum) / int(odd_count)))
