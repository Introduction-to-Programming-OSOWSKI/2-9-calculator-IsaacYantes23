def calculate(option,x,y):
    if option == "add":
        return x + y
    elif option == "subtract":
        return x - y
    elif option == "multiply":
        return x * y
    else:
        return x / y

print(calculate("multiply",10, 10))