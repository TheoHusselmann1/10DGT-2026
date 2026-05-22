# ask the user for their name
username = input("Please enter a username: ")

# ask the user for their faviourite number (interger)
fav_num = int(input("Please enter a number: "))

# Double, half and square the user's faviourite number
double = fav_num * 2
half = fav_num / 2
square = fav_num * fav_num

# Greet the user 
print(f"Hello {username}! Your chosen number is {fav_num}.")

# Output the results of the doubling, halving and squaring of their faviourite interger.
'''
# Output of doubling the number
print(double)

# Output of halving the number
print(half)

# Output of squaring the number
print(square)
'''
print()
print("Here all all of your results: ")
print()
print(f"Double {fav_num} is {double}.")
print(f"Half of {fav_num} is {half}.")
print(f"{fav_num} squared is {square}.")
print()
print("Thank you for using this program!")