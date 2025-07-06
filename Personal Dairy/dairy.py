import os
import datetime

os.makedirs("data", exist_ok=True) 
note_file = "data/notes.txt"



def add():
    """Adds a new note with an automatically generated timestamp."""

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = input("Write your note: ")
    with open(note_file, "a") as file:
        file.write(f"{timestamp}: {note}\n")
    print("Note added successfully!")

def view():
    """Views notes. Displays all if no specific date is entered."""
    try:
        with open(note_file, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No notes found.")
                return

            print("\n--- Your Notes ---")
            for i, line in enumerate(lines):
               
                parts = line.strip().split(":", 1)
                if len(parts) > 1:
                    timestamp = parts[0]
                    content = parts[1].strip()
                    print(f"{i+1}. [{timestamp}] {content}")
                else:
                    print(f"{i+1}. {line.strip()}") 
            print("------------------")

        input("Press Enter to continue...")

    except FileNotFoundError:
        print("No notes file found. Add a note first.")
    except Exception as e:
        print(f"An error occurred while viewing notes: {e}")

def edit():
    """Edits an existing note."""
    try:
        with open(note_file, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No notes to edit.")
            input("Press Enter to continue...")
            return

        print("\n--- Notes to Edit ---")
        for i, line in enumerate(lines):
            parts = line.strip().split(":", 1)
            display_line = f"[{parts[0]}] {parts[1].strip()}" if len(parts) > 1 else line.strip()
            print(f"{i+1}. {display_line}")
        print("---------------------")

        while True:
            try:
                choice = input("Enter the number of the note to edit (or '0' to cancel): ")
                if choice == '0':
                    print("Edit cancelled.")
                    input("Press Enter to continue...")
                    return

                note_index = int(choice) - 1
                if 0 <= note_index < len(lines):
                    old_note_content = lines[note_index].strip().split(":", 1)[1].strip() if len(lines[note_index].strip().split(":", 1)) > 1 else lines[note_index].strip()
                    print(f"Editing note: {old_note_content}")
                    new_note_text = input("Enter new note content: ")
                    
                    
                    timestamp_part = lines[note_index].strip().split(":", 1)[0]
                    lines[note_index] = f"{timestamp_part}: {new_note_text}\n"

                    with open(note_file, "w") as file:
                        file.writelines(lines)
                    print("Note updated successfully!")
                    input("Press Enter to continue...")
                    return
                else:
                    print("Invalid note number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    except FileNotFoundError:
        print("No notes file found. Add a note first.")
        input("Press Enter to continue...")
    except Exception as e:
        print(f"An error occurred while editing notes: {e}")
        input("Press Enter to continue...")

def delete():
    """Deletes an existing note."""
    try:
        with open(note_file, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No notes to delete.")
            input("Press Enter to continue...")
            return

        print("\n--- Notes to Delete ---")
        for i, line in enumerate(lines):
            parts = line.strip().split(":", 1)
            display_line = f"[{parts[0]}] {parts[1].strip()}" if len(parts) > 1 else line.strip()
            print(f"{i+1}. {display_line}")
        print("-----------------------")

        while True:
            try:
                choice = input("Enter the number of the note to delete (or '0' to cancel): ")
                if choice == '0':
                    print("Delete cancelled.")
                    input("Press Enter to continue...")
                    return

                note_index = int(choice) - 1
                if 0 <= note_index < len(lines):
                    deleted_note = lines.pop(note_index) 
                    with open(note_file, "w") as file:
                        file.writelines(lines)
                    print(f"Note '{deleted_note.strip().split(':', 1)[1].strip()}' deleted successfully!")
                    input("Press Enter to continue...")
                    return
                else:
                    print("Invalid note number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    except FileNotFoundError:
        print("No notes file found. Add a note first.")
        input("Press Enter to continue...")
    except Exception as e:
        print(f"An error occurred while deleting notes: {e}")
        input("Press Enter to continue...")



while True:
    print("\n--- Note Manager ---")
    print("1. Add Note")
    print("2. View Note")
    print("3. Edit Note")
    print("4. Delete Note")
    print("5. Exit")

    choice = input("Choose an option 1-5: ")

    match choice:
        case "1":
            add()
        case "2":
            view()
        case "3":
            edit()
        case "4":
            delete()
        case "5":
            break
        case _:
            print("Invalid choice")
            input("Press Enter to continue...")
