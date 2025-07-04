
""" Main Menu """

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_login():
    """Check if user is logged in"""
    return os.path.exists("logged_in.txt")

def menu():
    clear()
    if check_login():
        print("=== Welcome to SCPMS ===")
        print("1. Diary")
        print("2. Contacts")
        print("3. Todo")
        print("4. Expenses")
        print("5. Calculator")
        print("6. Unit Converter")
        print("7. Password Gen")
        print("8. Logout")
        print("9. Exit")
    else:
      
        print("=== Welcome to SCPMS ===")
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
                return True
        else:
         
            if choice == "1":
                exec(open("Personal Dairy/dairy.py").read())
            elif choice == "2":
                exec(open("Contact Book/contacts.py").read())
            elif choice == "3":
                exec(open("to-do-list-manager/tasks.py").read())
            elif choice == "4":
                exec(open("Expense Tracker/expense_tracker.py").read())
            elif choice == "5":
                exec(open("Utility Tools Section/calculator.py").read())
            elif choice == "6":
                exec(open("Utility Tools Section/unit_converter.py").read())
            elif choice == "7":
                exec(open("Utility Tools Section/Random_Password_Generator.py").read())
            elif choice == "8":
                # Logout
                if os.path.exists("logged_in.txt"):
                    os.remove("logged_in.txt")
                print("Logged out successfully!")
                input("Press Enter to continue...")
            else:
                print("Invalid choice!")
                input("Press Enter to continue...")
    except Exception as e:
        print(f"Error: {e}")
        input("Enter to return:")
    
    return True

while True:
    menu()
    if check_login():
        choice = input("Choose 1-9: ")
        if choice == "9":
            print("Program ended!")
            break
    else:
        choice = input("Choose 1-2: ")
        if choice == "2":
            print("Program ended!")
            break
    
    if not run(choice):
        break
