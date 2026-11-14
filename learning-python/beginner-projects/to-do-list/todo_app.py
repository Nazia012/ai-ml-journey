tasks = []
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":   
        while True:
            task = input("Enter your task (or type 'done' to finish): ")
            if task.lower() == "done": # .lower() handles 'DONE' or 'Done'
                break # This exits the INNER loop and goes back to main menu               
            if task: # Checks if the string is not empty
                tasks.append(task)
                print(f"Added: {task}")
    elif choice == "2":
        if not tasks:
            print("There is no tasks.")
        else:
            print("Your Tasks: ")
            for index, item in enumerate(tasks, start=1):
                print(index, item)
    elif choice =="3":
        break
    elif choice == "4":
        if not tasks:
            print("Nothing to delete!")
        else:
            user_input = input("Enter task number to delete: ")
            num = int(user_input)
            index_to_remove = int(num) - 1  # Adjusting for 0-based index
            # Check if the number is within the valid range
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted.")
            else:
                print("Invalid task number.")


