# Demonstrate how variables are created and how they work
# Author: Theo Husselmann
# Date: 6 May 2026
# V1.0.0

# TODO:
#   Store a string
#   Store different types of numbers 
#   Assign the valkue of one variable to another
#   Do calculations with variables and store the results.

#   Store a string example program
greeting = "Hello World!"
print(greeting)
random_variable = "7" # Storing a number as text
print(random_variable)

# Store different types of numbers
# Storing an interger (whole numeber)
num_1 = 7
print(f"The variable called num_1 which containes {num_1} is a {type(num_1)}")

# Stores a float number (A number with a decimal)
num_2 = 9.5
print(f"The variable called num_2 which containes {num_2} is a {type(num_2)}")

# Assign the value of one variable to another
num_2 = greeting
print(f"num_2 has the value of {greeting}")
print(f"num_2 has the value of {type(num_2)}")

# Do calculations with variables and store the results
# Create a new/reassign variable
num_1 = 5
num_2 = 18

# Add up numbers
sum = 5 + 18 # Not good practice
print(sum)

sum = num_1 + num_2
print(sum)

#Add up strings. This is called concatenation
sum_string1 = "18"
sum_string2 = "5"

sum_string_total = sum_string1 + sum_string2 
print(sum_string_total)
# Total prints as 185. This is not a number. It is text.

# Print formatting.
# f stands for 'format'.
# Insert the value of the variable into the string using curly brackets.
print(f"My calculation for adding {num_1} and {num_2} together is {sum}.")

# Old way of formationg strings 
print("My calculation for concatenating {} and {} is {}".format(sum_string1, sum_string2, sum_string_total))

# Greet someone
name = "Theo"
print("My name is ",name)
print("My name is {}.".format(name))
# New way of formatting strings in Python
print(f"My name is {name}.")