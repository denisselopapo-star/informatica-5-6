import random
def main():

    Guess = int(input("Take a guess on the coin flip game, if you want Heads type 1, if you prefer Tails type 2: "))

    Coin = random.randint(1,2)
    if Coin == 1:
        print("Heads")
    else:
        print("Tails")

    print("------------------------------")

    if Guess == Coin:
        print("Winner")
    else:
         print("Loser")



if __name__=="__main__":
        main()
