def rectangle_area():
    length = 10
    width = 5
    area = length * width
    print("Area of rectangle is: ", area)

rectangle_area()

def calculate_numbers(a, b):
    sum = a + b
    difference = a - b
    product = a * b
    division = a / b
    print("sum: ", sum)
    print("The difference: ", difference)
    print("The product: ", product)
    print("The division: ", division)

calculate_numbers(50, 10)

def Check_number(num):
    if num > 0 :
        print("The number is positive")
    elif num < 0 :
        print("The number is negative")
    else:
        print("The number is zero")

Check_number(5)
Check_number(-1)
Check_number(0)

def sum_to_n(n):
    total = 0
    for i in range (1, n + 1):
        total = total + i
    return total

result = sum_to_n(6)
print("sum is: ", result)

# uses of loop function
# 1. Repeating tasks
# 2. helps in processing items in list, tuples or strings
#3. It helps in mathematical operations like finding sums or averages

def square_upto(n):
    i = 1
    while i <= n:
        print("The square if", i ,"is", i * i)
        i+= 1

square_upto(10)

#uses of while loop function
# 1. Repeating tasks until a condition changes
# 2. Used to keep asking the user for input until they give the correct answer
# 3. Used to perform repeated calculations

        