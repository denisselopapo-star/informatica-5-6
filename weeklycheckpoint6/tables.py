def main():

    app = ""
    while True:
        app = input("Do you want to continue or exit: ").strip().title()
        if app == "Exit":
            print("See you later!")
            break

        if app == "Continue":
            numbers = [1,2,3,4,5,6,7,8,9,10]
            table = int(input("Enter a number from 1 to 10: "))

            if table in numbers:
                for n in range(len(numbers)):
                    mul = table * (n+1)
                    print(f"{n+1} x {table} is {mul}")
            followup = input("Do you want to exit or continue? ").strip().title()
        if followup == "Exit":
            break


if __name__=="__main__":
    main()

