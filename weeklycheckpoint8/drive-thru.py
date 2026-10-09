def main():


    print("Welcome to Happy Meal!")
    welcome()
    order = int(input("What would you like to eat today? Pleae enter the number of the item you want: "))
    get_item(order)

def welcome():
    menu = ["Cheeseburger","Fries","Soda","Ice Cream","Cookie"]
    print("Here's the menu: ")
    for food in range(len(menu)):
        print(f"{food+1} {menu[food]}")

def get_item(item):
    emoji = ["🍔", "🍟", "🥤", "🍦", "🍪"]
    if item == 1:
        print(f"here i your order {emoji[0]}")
    elif item == 2:
        print(f"here i your order {emoji[1]}")
    elif item == 3:
        print(f"here i your order {emoji[2]}")
    elif item == 4:
        print(f"here i your order {emoji[3]}")
    elif item == 5:
        print(f"here i your order {emoji[4]}")
    else:
        print("invalid option")


if __name__=="__main__":
    main()




