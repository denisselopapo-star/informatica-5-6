def main():
    not_validated = True #Initialization

    while not_validated: #Condition
        try:
            number = int(input("Enter a number between 1 and 10: "))
            not_validated = False
            if number == range(1,11):
                print("Valid number")

        except ValueError:
            print("You must enter a number between 1 and 10.")

if __name__=="__main__":
    main()
