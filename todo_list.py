print("Welcome to the To-Do List Manager!")
print("You can add tasks, view your to-do list, or exit the program.")
print("Commands: 'add' to add a task, 'view' to view your to-do list, 'exit' to exit the program.")
print("------------------------------------------------------------------------------------------")

to_do_list = []
while True:
    command = input("Enter a command (add/view/exit): ").strip().lower()
    
    if command == 'add':
        task = input("Enter the task you want to add: ").strip()
        to_do_list.append(task)
        print(f"Task '{task}' added to your to-do list.")
    
    elif command == 'view':
        if not to_do_list:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(to_do_list, start=1): #enumerate() is used to get both the index and the task from the to_do_list. The start=1 argument makes the index start from 1 instead of 0.
                print(f"{index}. {task}")
    
    elif command == 'exit':
        print("Exiting the To-Do List Manager. Goodbye!")
        break
    
    else:
        print("Invalid command. Please enter 'add', 'view', or 'exit'.")