import os
import time
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_expense_file(username):
    folder = "data/expenses"
    os.makedirs(folder, exist_ok=True)
    return f"{folder}/{username}_expenses.txt"

def add_expense(username):
    clear_screen()
    print("\n--- Add New Expense ---")
    file = get_expense_file(username)
    try:
        amount_str = input("Enter amount (e.g., 50.75): ").strip()
        amount = float(amount_str)
        if amount <= 0:
            print("Amount must be a positive number.")
            input("Press Enter to continue...")
            return
    except ValueError:
        print("Invalid amount. Please enter a numerical value.")
        input("Press Enter to continue...")
        return

    description = input("Enter description: ").strip()
    if not description:
        print("Description cannot be empty. Aborting.")
        input("Press Enter to continue...")
        return

    date = datetime.today().strftime('%Y-%m-%d')
    try:
        with open(file, "a", encoding='utf-8') as f:
            f.write(f"{date},{amount:.2f},{description}\n")
        print("Expense added successfully!")
        time.sleep(1)
    except Exception as e:
        print(f"Error adding expense: {e}")
        time.sleep(1.5)
    finally:
        input("Press Enter to continue...")

def read_expenses(username):
    file = get_expense_file(username)
    expenses = []
    if not os.path.exists(file):
        return expenses

    try:
        with open(file, "r", encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    try:
                        date_str, amount_str, desc = parts
                        expenses.append({
                            "date": date_str.strip(),
                            "amount": float(amount_str.strip()),
                            "description": desc.strip()
                        })
                    except ValueError:
                        print(f"Warning: Skipping malformed line in expense file: {line.strip()}")
                else:
                    print(f"Warning: Skipping malformed line (incorrect number of parts): {line.strip()}")
    except Exception as e:
        print(f"Error reading expenses file: {e}")
    return expenses

def view_expenses(username):
    clear_screen()
    print("\n--- All Your Expenses ---")
    expenses = read_expenses(username)

    if not expenses:
        print("No expenses found.")
    else:
        expenses.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
        for exp in expenses:
            print(f"{exp['date']} | {exp['description']} | Rs. {exp['amount']:.2f}")
    input("Press Enter to continue...")

def daily_report(username):
    clear_screen()
    print("\n--- Daily Expense Report ---")
    today = datetime.today().strftime('%Y-%m-%d')
    expenses = read_expenses(username)
    
    daily_total = 0
    found_expenses = False
    for exp in expenses:
        if exp['date'] == today:
            print(f"{exp['description']} | Rs. {exp['amount']:.2f}")
            daily_total += exp['amount']
            found_expenses = True
    
    if not found_expenses:
        print(f"No expenses recorded for today ({today}).")
    else:
        print(f"\nTotal expenses today ({today}): Rs. {daily_total:.2f}")
    input("Press Enter to continue...")

def monthly_report(username):
    clear_screen()
    print("\n--- Monthly Expense Report ---")
    this_month_prefix = datetime.today().strftime('%Y-%m')
    expenses = read_expenses(username)
    
    monthly_total = 0
    found_expenses = False
    for exp in expenses:
        if exp['date'].startswith(this_month_prefix):
            monthly_total += exp['amount']
            found_expenses = True
    
    if not found_expenses:
        print(f"No expenses recorded for this month ({this_month_prefix}).")
    else:
        print(f"\nTotal expenses this month ({this_month_prefix}): Rs. {monthly_total:.2f}")
    input("Press Enter to continue...")

def total_expenses(username):
    clear_screen()
    print("\n--- Overall Total Expenses ---")
    expenses = read_expenses(username)
    
    grand_total = sum(exp['amount'] for exp in expenses)
    
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print(f"Total expenses across all records: Rs. {grand_total:.2f}")
    input("Press Enter to continue...")

def expense_tracker_menu(username):
    while True:
        clear_screen()
        print(f"\n--- Expense Tracker for {username} ---")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Daily Report")
        print("4. Monthly Report")
        print("5. Total Expenses (Overall)")
        print("6. Return to Main Menu")

        choice = input("Choose one option (1-6): ").strip()
        
        if choice == "1":
            add_expense(username)
        elif choice == "2":
            view_expenses(username)
        elif choice == "3":
            daily_report(username)
        elif choice == "4":
            monthly_report(username)
        elif choice == "5":
            total_expenses(username)
        elif choice == "6":
            print("Returning to SCPMS Main Menu...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            time.sleep(1.5)

if __name__ == "__main__":
    current_username = "default_user"
    if os.path.exists("data/logged_in.txt"):
        try:
            with open("data/logged_in.txt", "r") as f:
                temp_username = f.read().strip()
                if temp_username:
                    current_username = temp_username
                else:
                    print("Warning: logged_in.txt is empty. Using default_user.")
        except Exception as e:
            print(f"Error reading username from logged_in.txt: {e}. Using default_user.")
    else:
        print("Not logged in. Running as default_user. Please log in via main SCPMS for proper functionality.")
        input("Press Enter to continue...")

    expense_tracker_menu(current_username)
