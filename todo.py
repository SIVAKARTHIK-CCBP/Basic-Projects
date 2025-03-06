# Simple To-Do List Application in Python

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"'{task}' has been added to the list.")

def remove_task(tasks):
    try:
        task_num = int(input("Enter the no of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"'{removed_task}' has been removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Thank you,have a nice day!")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
