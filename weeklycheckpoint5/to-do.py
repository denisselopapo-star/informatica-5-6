def main():

    tasks = []

    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)
        command = input("What do you want to do? (add, complete, exit): ")
        if command == "add":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
        elif command == "complete":
            remove_task = input("Which task did you complete? ")
            tasks.remove(remove_task)
        elif command == "exit":
            print("See you later!")
            break



if __name__=="__main__":
    main()
