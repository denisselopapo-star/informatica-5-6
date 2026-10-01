def main():
    valid_nums = []
    for i in range(1,11):
        valid_nums.append(str(i))

    while True:
        print("Welcome to the times table quiz!")
        times_table = input("Enter a times table that you would like to be tested on: ").lower().strip()
        if times_table == "exit":
            break

        elif times_table in valid_nums:
            max_value = int(input("Enter a maximum value for the times table: "))

            print(f"here is your quiz on the {times_table} times table")

            for x in range(1, max_value+1):
                answer = x* int(times_table)
                user_answer = int (input(f"{times_table}x{x}="))
                if user_answer == answer:
                    print("Correct!")
                elif user_answer != answer:
                    print("Incorrect")
                    print(f"The correct answer of {x} times {times_table} is {answer}")
            if max_value == max_value:
                print("You are finish!")
                break

        else:
            print("Invalid command")

if __name__=="__main__":
    main()
