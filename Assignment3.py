#IF ELSE...ELSE
income =int(input("Enter your income: "))
if income >=0 and income <= 5999:
    print(150.00)
elif income >= 6000 and income <= 7999:
    print(300.00)
elif income >= 8000 and income <= 11999:
    print(400.00)
elif income >= 12000 and income <= 14999:
    print(500.00)
elif income >= 15000 and income <= 19999:
    print(600.00)
elif income >= 20000 and income <= 24999:
    print(750.00)
elif income >= 25000 and income <= 29999:
    print(850.00)
elif income >= 30000 and income <= 49999:
    print(1000.00)
elif income >= 50000 and income <= 99999:
    print(1500.00)
else :
    print(2000.00)
