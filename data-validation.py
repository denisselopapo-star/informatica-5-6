def main():
    name = input("Enter a name:")
    print(f"Stored name: {name}")

    not_validated = True #Initialization

    while not_validated: #Condition
        try:
            number = int(input("Enter a number between 1 and 10: "))
            if number >= 1 and number <= 10:
                print("Success!")
                not_validated = False
        except ValueError:
            print("You must enter a number between 1 and 10.")

if __name__=="__main__":
    main()
