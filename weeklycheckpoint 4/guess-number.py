import random
def main():

    name = input("Hello! What is your name? ").title()
    print("Well,", name,",I am thinking of a number between 1 and 100.")
    number = random.randint(1,100)
    guess = 0

    while guess != number:
        guess = int(input("Take a guess "))
        if guess < number:
            print("Your answer is to low")
        elif guess > number:
            print("Your answar is to high")
        elif guess == number:
            print("Good job",name,"You guessed my number!")
        else:
            print("")



if __name__=="__main__":
        main()

