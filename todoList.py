#todolist
import time
import os

FILENAME = "tasks.txt"
tasks = []

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                tasks.append(line.strip())

def save_tasks():
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def show_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    time.sleep(2)

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks()
    print("Task added.")
    time.sleep(2)

def remove_task():
    show_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks()
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    time.sleep(2)

def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("Choose a option (1-4): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()