import os
if not os.path.exists("data/logged_in.txt"):
    print("Access Denied. Please log in first.")
    exit()



unit = input("Which unit you want to convert? (Weight / Length / Temperature): ").lower()

if unit == "length":
    val = float(input("Enter value: "))
    print("1. Meters to Feet\n2. Feet to Meters")
    option = input("Choose one option: ")
    if option == "1":
        print(f"{val} meters = {val * 3.281:.2f} feet")
    else:
        print(f"{val} feet = {val / 3.281:.2f} meters")

elif unit == "weight":
    val = float(input("Enter value: "))
    print("1. KG to Pounds\n2. Pounds to KG")
    option = input("Choose one option: ")
    if option == "1":
        print(f"{val} kg = {val * 2.20462:.2f} pounds")
    else:
        print(f"{val} pounds = {val / 2.20462:.2f} kg")

elif unit == "temperature":
    val = float(input("Enter temperature: "))
    print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
    option = input("Choose one option: ")
    if option == "1":
        print(f"{val}°C = {(val * 9/5) + 32:.2f}°F")
    else:
        print(f"{val}°F = {(val - 32) * 5/9:.2f}°C")

else:
    print("Invalid option.")
