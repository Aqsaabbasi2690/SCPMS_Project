""" SCPMS """

import os


os.makedirs("data", exist_ok=True)

SESSION_FILE = "data/logged_in.txt"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_login():
    """Check if user is logged in"""
    return os.path.exists(SESSION_FILE)

def menu():
    clear()
    print("=== Welcome to SCPMS ===")
    if check_login():
        print("1. Diary")
        print("2. Contacts")
        print("3. To-Do List")
        print("4. Expenses")
        print("5. Calculator")
        print("6. Unit Converter")
        print("7. Password Generator")
        print("8. Logout")
        print("9. Exit")
    else:
        print("Please login first!")
        print("1. Login/Register")
        print("2. Exit")

def run(choice):
    try:
        if not check_login():
            if choice == "1":
                exec(open("User Registration & Login System/user_auth.py").read())
            elif choice == "2":
                return False  # Exit
            else:
                print("Please login first!")
                input("Press Enter to continue...")
        else:
            match choice:
                case "1":
                    exec(open("Personal Dairy/dairy.py").read())
                case "2":
                    exec(open("Contact Book/contacts.py").read())
                case "3":
                    exec(open("to-do-list-manager/tasks.py").read())
                case "4":
                    exec(open("Expense Tracker/expense_tracker.py").read())
                case "5":
                    exec(open("Utility Tools Section/calculator.py").read())
                case "6":
                    exec(open("Utility Tools Section/unit_converter.py").read())
                case "7":
                    exec(open("Utility Tools Section/Random_Password_Generator.py").read())
                case "8":
                    if os.path.exists(SESSION_FILE):
                        os.remove(SESSION_FILE)
                    print("Logged out successfully!")
                    input("Press Enter to continue...")
                case "9":
                    return False  # Exit
                case _:
                    print("Invalid choice!")
                    input("Press Enter to continue...")
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to return...")
    return True

while True:
    menu()
    if check_login():
        choice = input("Choose an option (1-9): ")
    else:
        choice = input("Choose an option (1-2): ")

    if not run(choice):
        print("Program ended!")
        break
