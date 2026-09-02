def main():

    #FINITE LOOP
    answer = ""
    followup = ""
    while answer != "Yes!":
        answer = input("Are we there yet? ").title().strip()
        if answer == "Yes":
            followup = input("Really? ").title().strip()
        if followup == "Yes":
             break

    print("WE are here!")


if __name__=="__main__":
        main()

