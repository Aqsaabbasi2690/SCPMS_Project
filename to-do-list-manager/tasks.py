import os
import time

os.makedirs("data", exist_ok=True)
task_file = "data/task.txt"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_task():
    print("\n--- Add New Task ---")
    task = input("Enter your task: ").strip()
    if not task:
        print("Task cannot be empty. Aborting.")
        input("Press Enter to continue...")
        return

    while True:
        priority = input("Enter task priority (first priority / second priority / third priority): ").strip().lower()
        if priority in ["first priority", "second priority", "third priority"]:
            break
        else:
            print("Invalid priority. Please enter 'first priority', 'second priority', or 'third priority'.")
            time.sleep(1)

    try:
        with open(task_file, "a", encoding='utf-8') as file:
            file.write(f"{task} | {priority} | Pending\n")
        print("Task added successfully!")
        time.sleep(1)
    except Exception as e:
        print(f"Error adding task: {e}")
        time.sleep(1.5)
        input("Press Enter to continue...")

def view_pending_tasks():
    print("\n--- Your Pending Tasks ---")
    try:
        with open(task_file, "r", encoding='utf-8') as file:
            tasks = []
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3 and parts[2].strip().lower() == "pending":
                    tasks.append(parts)

            if not tasks:
                print("No pending tasks found.")
            else:
                priority_order = {"first priority": 1, "second priority": 2, "third priority": 3}
                tasks.sort(key=lambda x: priority_order.get(x[1].strip().lower(), 99))

                for i, task_parts in enumerate(tasks):
                    task_name = task_parts[0].strip()
                    task_priority = task_parts[1].strip()
                    print(f"{i+1}. {task_name} [{task_priority.capitalize()}]")
    except FileNotFoundError:
        print("No tasks file found. Please add tasks first.")
    except Exception as e:
        print(f"An error occurred while viewing tasks: {e}")
    input("Press Enter to continue...")

def mark_task_as_complete():
    print("\n--- Mark Task as Complete ---")
    try:
        with open(task_file, "r", encoding='utf-8') as file:
            all_lines = file.readlines()

        pending_tasks_for_selection = []
        original_indices = []
        for i, line in enumerate(all_lines):
            parts = line.strip().split("|")
            if len(parts) == 3 and parts[2].strip().lower() == "pending":
                pending_tasks_for_selection.append(parts)
                original_indices.append(i)

        if not pending_tasks_for_selection:
            print("No pending tasks to mark as complete.")
            input("Press Enter to continue...")
            return

        print("\n--- Select Task to Mark Complete ---")
        priority_order = {"first priority": 1, "second priority": 2, "third priority": 3}
        sorted_tasks_with_orig_idx = sorted(
            zip(pending_tasks_for_selection, original_indices),
            key=lambda x: priority_order.get(x[0][1].strip().lower(), 99)
        )

        for i, (task_parts, _) in enumerate(sorted_tasks_with_orig_idx):
            task_name = task_parts[0].strip()
            task_priority = task_parts[1].strip()
            print(f"{i+1}. {task_name} [{task_priority.capitalize()}]")
        print("-----------------------------------")

        while True:
            try:
                choice = input("Enter the number of the task to mark as complete (or '0' to cancel): ").strip()
                if choice == '0':
                    print("Operation cancelled.")
                    input("Press Enter to continue...")
                    return

                selected_list_index = int(choice) - 1
                if 0 <= selected_list_index < len(sorted_tasks_with_orig_idx):
                    original_line_index = sorted_tasks_with_orig_idx[selected_list_index][1]
                    
                    parts_to_update = all_lines[original_line_index].strip().split("|")
                    if len(parts_to_update) == 3:
                        task_name_to_confirm = parts_to_update[0].strip()
                        all_lines[original_line_index] = f"{parts_to_update[0].strip()} | {parts_to_update[1].strip()} | Completed\n"
                        
                        with open(task_file, "w", encoding='utf-8') as file:
                            file.writelines(all_lines)
                        print(f"Task '{task_name_to_confirm}' marked as complete!")
                    else:
                        print("Error: Invalid task format found in file.")
                    input("Press Enter to continue...")
                    return
                else:
                    print("Invalid task number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An unexpected error occurred during selection: {e}")

    except FileNotFoundError:
        print("No tasks file found. Please add tasks first.")
        input("Press Enter to continue...")
    except Exception as e:
        print(f"An error occurred while marking task complete: {e}")
        input("Press Enter to continue...")

def delete_task():
    print("\n--- Delete Task ---")
    try:
        with open(task_file, "r", encoding='utf-8') as file:
            all_lines = file.readlines()

        if not all_lines:
            print("No tasks to delete.")
            input("Press Enter to continue...")
            return

        print("\n--- Select Task to Delete ---")
        for i, line in enumerate(all_lines):
            parts = line.strip().split("|")
            task_name = parts[0].strip() if len(parts) > 0 else "Unnamed Task"
            status = parts[2].strip() if len(parts) > 2 else "Unknown Status"
            priority = parts[1].strip() if len(parts) > 1 else "Unknown Priority"
            print(f"{i+1}. {task_name} [{priority.capitalize()}] ({status})")
        print("---------------------------")

        while True:
            try:
                choice = input("Enter the number of the task to delete (or '0' to cancel): ").strip()
                if choice == '0':
                    print("Deletion cancelled.")
                    input("Press Enter to continue...")
                    return

                selected_index = int(choice) - 1
                if 0 <= selected_index < len(all_lines):
                    deleted_task_parts = all_lines[selected_index].strip().split("|")
                    deleted_task_name = deleted_task_parts[0].strip() if len(deleted_task_parts) > 0 else "Unnamed Task"

                    all_lines.pop(selected_index)

                    with open(task_file, "w", encoding='utf-8') as file:
                        file.writelines(all_lines)
                    print(f"Task '{deleted_task_name}' deleted successfully!")
                    input("Press Enter to continue...")
                    return
                else:
                    print("Invalid task number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An unexpected error occurred during deletion: {e}")

    except FileNotFoundError:
        print("No tasks file found.")
        input("Press Enter to continue...")
    except Exception as e:
        print(f"An error occurred while preparing to delete tasks: {e}")
        input("Press Enter to continue...")

def todo_menu():
    while True:
        clear_screen()
        print("\n==== To-Do List Manager ====")
        print("1. Add Task")
        print("2. View Pending Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Return to Main Menu")

        choice = input("Choose one option (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_pending_tasks()
        elif choice == "3":
            mark_task_as_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Returning to SCPMS Main Menu...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            time.sleep(1.5)

if __name__ == "__main__":
    todo_menu()
