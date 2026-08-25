def main():
    print("Thank you for consuming at Tequeria Tacos!" )

    rate = float(input("Rate us with a decimal number from 0 to 5: "))

    if rate > 5:
        print("Thank you! But choose a smaller number")
    elif rate > 4.5:
        print("Perfection!")
    elif rate > 4:
        print("Excellent!")
    elif rate > 3:
        print("Good!")
    elif rate > 2:
        print("Fair")
    elif rate > 1:
        print("Poor")
    else:
        print("Thank you, have a wonderfull day!")




if __name__=="__main__":
    main()
