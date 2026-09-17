def main():
    tasks = []
    while True:
        print(f"tasks to do:{len(tasks)}")
        print(tasks)
        new_task = input("Enter task: ").capitalize().strip()

        if new_task == "Exit":
            break
        elif new_task not in tasks:
            tasks.append(new_task)
        elif new_task in task:
            tasks.remove(new_task)
            prin("task removed from the list")

if __name__=="__main__":
    main()
