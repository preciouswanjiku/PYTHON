# python list
# A list in python is a collection of items that are odered in a certain way.
# A list is introduced by a square bracket.
# The items of a list are stored inside indexes. Note: In programming we start countig from index zero(0).bmw, benz, hiance,...
# A list is mutable, ie: The content of the list can be changed

cars = ["BMW","probox" , "landcruiser" ,"prado", "mercedes", "jeep","rolsroyce","Appocalypse", "Lamborgini"]
print(cars)
print(type(cars))

#Accessing items of a list
print(cars[2])
print("The car on idex four is:", cars[4])

#List slicing: This is creating a list from a given bigger list.
print(cars[4:])

# Printing from index zero to index three
print(cars[:4])

# printing from landcruiser to jeep
print(cars[2:5])

#list-mutability
#we use the function append to add an item at the end of a list
cars.append("subaru")
print(cars)

cars.append("vits")
print(cars)

#We use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

#We can use an index to add items to a list
cars[5] = "Pajero"
print(cars)

#We can sort functions to sort out items in alphabetical order.
cars.sort()
print(cars)