# Python functions
# They are a program of codes / statements that perform a given task/ function. they can be reused throuh out the program to perform different tasks. functions are defined using def key word. we have two main types of functions, ie: In-Built functions - they come pre installed wit the interpreter, ie: print(), pop() etc.., User defined functions- they are created by a programer to solve a given task.
# To define a function, you need to give it a name followed by parenthasis.
# For the functions, it is useally indented, and to invoke a function, use the function name.

def greetings ():
    print("Hello, how are you doing")

# Below we call the function by use of its name

greetings()

print("======================")
#Addiction function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the number is:", sum)

addition()

print("=======================")

# Create a function that is able to multiply three values

def multiplication():
    num3 = 20
    num4 = 30
    num5 = 40
    product =num3 * num4 * num5
    print("The product of the numbers is: ", product)

multiplication()

print("=====================")
#Below is a division function
def divide():
    number1 =int(input("Enter the first number"))
    number2 =int(input("Enter the second number"))
    quotient = number1 / number2
    print("the answer is: ", quotient)