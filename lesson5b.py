# functions with parameters
# They are values that get passed as arguments when given to a function inside of the parenthesis

def greeting(name):
    print(f"{name} how are you, hope everything is fine")

greeting("Precious")
greeting("Mary")
greeting("Joseph")

print("===================")
def message(names):
    print(f"{names} we shall be having a general meeting on date....please avail yourself")

message("joy")
message("Stephen")

print("========================")

# Create a function that accepts parameter to add two numbers
def addition  (x , y):
    sum = x + y
    print("the sum of the numbers is: ", sum)
