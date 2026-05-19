# Create an error handling function
# Author: Theo Husselmann
# Current Version: V3.0.0

# V1.0.0

'''
# Code that tests that a valid number is entered (V1)
done = False # Boolean variable set to False
# While loop that runs until a valid number is entered
while not done:
    num = int(input("Please enter your number: "))
    done = True

print(f"The number you entered is {num}.")
'''

# Code that tests that a valid number is entered 
# Create a function to call every time I ask the user for a number. A function is a chink of code that does something. 
# I can use a fucntion over and over. To use a function I 'call' it by writing its name.

# V2.0.0

'''
def test_int_num(): # test_int_num() is the name of the function
    done = False
    while not done:
        try: # This tries for a valid input
            num = int(input("Please enter your number: "))
            done = True

        except ValueError:
            print("That is not a valid integer.") 
    
    return(num)

# Main routine

num_1 = test_int_num()
print(f"You entered {num_1} as your first number.")

num_2 = test_int_num()
print(f"You entered {num_2} as your second number")
print() # One way of creating a line break

# Addition
sum = num_1 + num_2 
print(f"\nYour two numbers added together are {sum}") # \n creates a line break within a string.

# Multiplication
multiply = num_1 * num_2 
print(f"Your two numbers multiplied with eachother results in {multiply}")

# Division
divide = num_1 / num_2
print(f"{num_1} divided by {num_2} is equal to {divide}.")
'''

# Refining my code. making it more pythonic
# V3.0.0

# FUNCTION

def test_init_num(question, low, high): # 'question, low, high' is a placeholder
    done = False
    error = f"Whoops, that is not an interget between {low} and {high}."
    while not done:
        # print(question)
        try: # tries valid input
            num = int(input(question))
            if num >= low and num <= high :
                done = True 

            else:
                print(error)
                print()

        except ValueError:
            print("That is not a valid interger")

    return(num)

# MAIN ROUTINE

# 'num_1' variable
num_1 = test_init_num("Please enter your first number between 1 and 10: ", 1, 10)
print(f"You entered {num_1} as your first number.\n")

# 'num_2' variable
num_2 = test_init_num("Please enter your second number between 10 and 20: ", 10, 20)
print(f"You enter {num_2} as your second number.\n")

# 'num_3' variable
num_3 = test_init_num("Please enter your third number between 20 and 30: ", 20, 30)
print(f"You entered {num_3} as your second number.\n")

# CALCULATIONS

# Addition
sum = num_1 + num_2 + num_3
print(f"\nYour two numbers added together are {sum}") # \n creates a line break within a string.

# Multiplication
multiply = num_1 * num_2 * num_3
print(f"Your two numbers multiplied with eachother results in {multiply}")

# Division
divide = num_1 / num_2 / num_3
print(f"{num_1} divided by {num_2} is equal to {divide}.")