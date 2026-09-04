import random

def main():

    print("Welcome to Mathenaitor plus!")
    number1 = random.randint(1,99)
    number2 = random.randint(1,99)
    guess = 0
    attempts = 3
    operation = number1 + number2
    streak = "⭐"

    print("what is ", number1,"+",number2,"?")
    guess = int(input("your answer: "))
    while attempts > 0:
        if guess != operation:
        print("Incorrect!")
        print("The answer was: ", operation)
        elif guess == operation:
            print("Correct!")
            print("Streak: ",streak)
            break



if __name__=="__main__":
        main()

