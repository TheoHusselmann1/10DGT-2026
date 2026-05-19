# Demonstrate how to use an IF statement
# Author: Theo Husselmann
# 1st May 2026
# V1.0.0

''' TODO: Create a program that will ask the user whether they like Computers or not.
if they do not like Computers, I will try to persuade them to try it. '''


# Checking whether you like Computers. (Stores the answers in a variable)



like_computers = input("Do you like Computers? ")
# print(like_computers)

if like_computers == "yes":
    print("Nice! I love computers too!")

elif like_computers == "no":
    print("That's a shame")

else:
    print("Try Again.")

keep_going = input("Press <enter> to continue")

# Number Demo 
num_1 = int(input("Please enter your first number: "))
num_2 = int(input("Please enter your second number: "))

sum = num_1 + num_2 

print(f"The answer to both your numbers added together is {sum}")
