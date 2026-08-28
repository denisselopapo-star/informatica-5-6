def main():

    #Difficulty: Easy - Absolute Value Calculator

    Integer = int(input("Enter an integer: "))
    Negative = Integer * -1

    if Integer < 0:
        print(Negative)
    else:
        print(Integer)

    #Difficulty: Medium - Input Calculator

    print("Type your two numbers and the operation of your preference")
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    operation = input("Type your operation add, subtract or multiply: ")
    add = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2

    if operation == "add":
        print(add)
    elif operation == "subtract":
        print(subtract)
    elif operation == "multiply":
        print(multiply)
    else:
        print()


if __name__=="__main__":
    main()

