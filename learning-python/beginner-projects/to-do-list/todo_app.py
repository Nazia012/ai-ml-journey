tasks = [] 

while True: 
    # --- THIS IS THE MAIN MENU ---
    print("\n1. Add a Task")
    print("2. View my Tasks")
    print("3. Quit the game")
    
    choice = input("Pick a number: ") 

    # --- THIS IS THE ADD SCREEN ---
    if choice == "1": 
        t = input("What do you want to add? ") 
        tasks.append(t)     
        print("Task Saved!")

    # --- THIS IS THE VIEW SCREEN ---
    elif choice == "2": 
        print("Here is your list:")
        print(tasks)     

    # --- THIS IS THE QUIT SCREEN ---
    elif choice == "3": 
        print("Bye!")
        break
