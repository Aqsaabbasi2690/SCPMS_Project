import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator_menu():
    while True:
        clear_screen()
        print("\n--- Simple Calculator ---")
        print("1. Start Calculations")
        print("2. Return to Main Menu")

        choice = input("Choose an option (1-2): ").strip()

        if choice == "1":
            while True:
                clear_screen()
                print("\n--- Choose an Operation ---")
                print("1. Addition (+)")
                print("2. Subtraction (-)")
                print("3. Multiplication (*)")
                print("4. Division (/)")
                print("5. Back to Calculator Main Menu")

                op_choice = input("Choose an operation (1-5): ").strip()

                if op_choice == "5":
                    break

                if op_choice not in ["1", "2", "3", "4"]:
                    print("Invalid operation choice. Please enter a number between 1 and 5.")
                    time.sleep(1.5)
                    input("Press Enter to continue...")
                    continue

                try:
                    num1_str = input("Enter first number: ").strip()
                    num1 = float(num1_str)

                    num2_str = input("Enter second number: ").strip()
                    num2 = float(num2_str)

                    result = None
                    operation_symbol = ""

                    if op_choice == "1":
                        result = num1 + num2
                        operation_symbol = "+"
                    elif op_choice == "2":
                        result = num1 - num2
                        operation_symbol = "-"
                    elif op_choice == "3":
                        result = num1 * num2
                        operation_symbol = "*"
                    elif op_choice == "4":
                        if num2 == 0:
                            print("\n--- Result ---")
                            print("Error: Division by zero is not allowed.")
                            input("Press Enter to continue...")
                            continue
                        else:
                            result = num1 / num2
                            operation_symbol = "/"

                    print("\n--- Result ---")
                    print(f"{num1} {operation_symbol} {num2} = {result}")

                except ValueError:
                    print("Invalid input. Please enter valid numerical values for numbers.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
                
                input("Press Enter to continue...")

        elif choice == "2":
            print("Returning to SCPMS Main Menu...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please enter '1' or '2'.")
            time.sleep(1.5)

if __name__ == "__main__":
    calculator_menu()
