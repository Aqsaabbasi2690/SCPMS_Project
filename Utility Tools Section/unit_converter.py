import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def convert_units():
    while True:
        clear_screen()
        print("\n--- Unit Converter ---")
        print("1. Length (Meters <-> Feet)")
        print("2. Weight (KG <-> Pounds)")
        print("3. Temperature (Celsius <-> Fahrenheit)")
        print("4. Back to Unit Converter Menu")

        unit_choice = input("Choose an option (1-4): ").strip()

        if unit_choice == "4":
            break
        
        if unit_choice not in ["1", "2", "3"]:
            print("Invalid unit type choice. Please enter a number between 1 and 4.")
            time.sleep(1.5)
            input("Press Enter to continue...")
            continue

        try:
            val = float(input("Enter value to convert: ").strip())

            if unit_choice == "1":
                clear_screen()
                print(f"\n--- Converting Length ({val}) ---")
                print("1. Meters to Feet")
                print("2. Feet to Meters")
                option = input("Choose one conversion (1-2): ").strip()
                if option == "1":
                    print(f"{val:.2f} meters = {val * 3.281:.2f} feet")
                elif option == "2":
                    print(f"{val:.2f} feet = {val / 3.281:.2f} meters")
                else:
                    print("Invalid conversion option.")

            elif unit_choice == "2":
                clear_screen()
                print(f"\n--- Converting Weight ({val}) ---")
                print("1. KG to Pounds")
                print("2. Pounds to KG")
                option = input("Choose one conversion (1-2): ").strip()
                if option == "1":
                    print(f"{val:.2f} kg = {val * 2.20462:.2f} pounds")
                elif option == "2":
                    print(f"{val:.2f} pounds = {val / 2.20462:.2f} kg")
                else:
                    print("Invalid conversion option.")

            elif unit_choice == "3":
                clear_screen()
                print(f"\n--- Converting Temperature ({val}) ---")
                print("1. Celsius to Fahrenheit")
                print("2. Fahrenheit to Celsius")
                option = input("Choose one conversion (1-2): ").strip()
                if option == "1":
                    print(f"{val:.2f}°C = {(val * 9/5) + 32:.2f}°F")
                elif option == "2":
                    print(f"{val:.2f}°F = {(val - 32) * 5/9:.2f}°C")
                else:
                    print("Invalid conversion option.")

        except ValueError:
            print("Invalid input. Please enter a numerical value for conversion.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        input("Press Enter to continue...")

def unit_converter_menu():
    while True:
        clear_screen()
        print("\n==== Unit Converter ====")
        print("1. Start Conversions")
        print("2. Return to Main Menu")

        main_choice = input("Choose an option (1-2): ").strip()

        if main_choice == "1":
            convert_units()
        elif main_choice == "2":
            print("Returning to SCPMS Main Menu...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please enter '1' or '2'.")
            time.sleep(1.5)

if __name__ == "__main__":
    unit_converter_menu()
