# Loops -> sometimes we may need to do a piece of work repeated times, and in such cases, we may use loops.
# A loop is a control structure that allows us to execute a block of code repeatedly until a certain condition is met.
# There are two types of loops in python, ie the for loop and the while loop.
# Below is the syntax for a loop in python.
""""
for variable in range (n)
    #block of code to be executed.
"""

print("Hello Moses")
print("Hello Moses")
print("Hello Moses")
print("Hello Moses")
print("Hello Moses")


for greeting in range(5):
    print("Hello moses", greeting)


print("===================")

for number in range (10, 20):
    print(number)

print("====================")
# Find the even numbers in the range of 50 to 71
for number in range(50, 71, 2):
    print(number)

print("======================")
# Create a python program that indicates the odd numbers from 100 to 150
for number in range(101, 150, 2):
    print(number)

print("========================")
# Create a program that prints the multiples of three starting from 201 to 150
for number in range(201, 149, -3):
    print(number)

print("=====================")
# create a python program that prints the leap years in between 2000 and 2024


