#!/usr/bin/env python3
"""
Main Menu
"""

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear()
    print("=== Welcome to SCPMS ===")
    print("1. Login")
    print("2. Diary") 
    print("3. Contacts")
    print("4. Todo")
    print("5. Expenses")
    print("6. Calculator")
    print("7. Unit Converter")
    print("8. Password Gen")
    print("9. Exit")

def run(choice):
    try:
        if choice == "1":
            exec(open("User Registration & Login System/user_auth.py").read())
        elif choice == "2":
            exec(open("Personal Dairy/dairy.py").read())
        elif choice == "3":
            exec(open("Contact Book/contacts.py").read())
        elif choice == "4":
            exec(open("to-do-list-manager/tasks.py").read())
        elif choice == "5":
            exec(open("Expense Tracker/expense_tracker.py").read())
        elif choice == "6":
            exec(open("Utility Tools Section/calculator.py").read())
        elif choice == "7":
            exec(open("Utility Tools Section/unit_converter.py").read())
        elif choice == "8":
            exec(open("Utility Tools Section/Random_Password_Generator.py").read())
        else:
            print("Invalid choice!")
    except:
        print("File not found!")
    
    input("Enter to return:")

while True:
    menu()
    choice = input("Choose 1-9: ")
    if choice == "9":
        print("program ended!")
        break
    
    run(choice)
