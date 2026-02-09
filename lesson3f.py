# Create a pyhon program that is able to determine whether a number entered is an odd number or an even number
#number = int(input("Enter your number here"))
#if number % 2:
#    print("The number is even")
#else:
#    print("The number is odd")

# Create a python program to determine whether a person can donate blood based on age and weight of a person. If the weight is greater than 50kgs and age is greater than 18,they can donate blood, else, not possible.

age = int(input("Enter age: "))
weight = float(input("Enter weight: "))

if age >=18 and weight > 50:
    print("Can donate")
else:
    print("Not possible")