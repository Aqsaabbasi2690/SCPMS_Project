# To-Do List Manager

def add_task():
    task = input("Enter your task: ")
    priority = input("Enter task priority (first priority / second priority / third priority): ")
    with open("task.txt", "a") as file:
        file.write(f"{task} | {priority} | Pending\n")
    print("Task added!")

def view_tasks():
    print("Your Pending Tasks:")
    found = False
    with open("task.txt", "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 3 and parts[2].strip() == "Pending":
                print(f"{parts[0].strip()} [{parts[1].strip()} Priority]")
                found = True
    if not found:
        print("No pending tasks found")

def mark_complete():
    taskname = input("Enter the task to mark as complete: ")
    lines = []
    found = False
    with open("task.txt", "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if parts[0].strip() == taskname and parts[2].strip() == "Pending":
                lines.append(f"{parts[0].strip()} | {parts[1].strip()} | Completed\n")
                found = True
            else:
                lines.append(line)
    with open("task.txt", "w") as file:
        file.writelines(lines)
    if found:
        print("Task marked as complete!")
    else:
        print("Task not found or already completed.")

def delete_task():
    task = input("Enter the task to delete: ")
    lines = []
    found = False
    with open("task.txt", "r") as file:
        for line in file:
            if not line.startswith(task + " |"):
                lines.append(line)
            else:
                found = True
    if found:
        with open("task.txt", "w") as file:
            file.writelines(lines)
        print("Task deleted.")
    else:
        print("Task not found.")

def menu():
    while True:
        print("\n==== To-Do List Manager ====")
        print("1. Add Task")
        print("2. View Pending Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose one option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

menu()
