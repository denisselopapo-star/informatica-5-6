import random

def main():

    print("Welcome to Mathenaitor plus!")
    streak = 0
    star = "⭐"


    while streak != 3:
        print("what is ", number1,"+",number2,"?")
        number1 = random.randint(1,99)
        number2 = random.randint(1,99)
        operation = number1 + number2
        guess = int(input("Your answer: "))
        if guess != operation:
            print("Incorrect!")
            print("The answer was: ", operation)
            elif guess == operation:
                streak += 1
            if streak == 1:
                print("Correct!")
                print("Streak: ", star)
            elif streak == 2
                print("Streak: ", star + star)
            else:
                print("Streak:" star + star + star)
                print("great job!")



if __name__=="__main__":
        main()

