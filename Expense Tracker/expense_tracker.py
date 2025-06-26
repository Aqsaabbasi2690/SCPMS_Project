import os
from datetime import datetime
def get_expense_file(username):
    folder = "data/expenses"
    os.makedirs(folder, exist_ok=True)
    return f"{folder}/{username}_expenses.txt"

# Step1
def add_expense(username):
    file = get_expense_file(username)
    amount = input("Enter amount: ")
    description = input("Enter description: ")
    date = datetime.today().strftime('%Y-%m-%d') 
    with open(file, "a") as f:
        f.write(f"{date},{amount},{description}\n")
    print("Expense added!")

# 2
def view_expenses(username):
    file = get_expense_file(username)
    if not os.path.exists(file):
        print("No expenses found")
        return
    with open(file, "r") as f:
        for line in f:
            date, amount, desc = line.strip().split(",")
            print(f"{date} | {desc} | Rs. {amount}")



# 3
def daily_report(username):
    today = datetime.today().strftime('%Y-%m-%d')
    file = get_expense_file(username)
    total = 0
    with open(file, "r") as f:
        for line in f:
            date, amount, _ = line.strip().split(",")
            if date == today:
                total += int(amount)
    print(f"Total expenses today: Rs. {total}")



# 4
def monthly_report(username):
    this_month = datetime.today().strftime('%Y-%m')
    file = get_expense_file(username)
    total = 0
    with open(file, "r") as f:
        for line in f:
            date, amount, _ = line.strip().split(",")
            if date.startswith(this_month):
                total += int(amount)
    print(f"Total expenses of month: Rs. {total}")



# 5
def total_expenses(username):
    file = get_expense_file(username)
    total = 0
    with open(file, "r") as f:
        for line in f:
            _, amount, _ = line.strip().split(",")
            total += int(amount)
    print(f"Total expenses: Rs. {total}")




# main part
def menu(username):
    while True:
        print("\n--- Expense Tracker ---")
        print("1 Add Expense")
        print("2 View All")
        print("3 Daily Report")
        print("4 Monthly Report")
        print("5 Total Expenses")
        print("6 Exit")

        choice = input("Choose one option: ")
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
            break
        else:
            print("Invalid choice.")

username = input("Enter Your Name:")
menu(username)
