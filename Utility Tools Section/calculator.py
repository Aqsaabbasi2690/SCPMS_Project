import os
if not os.path.exists("data/logged_in.txt"):
    print("Access Denied. Please log in first.")
    exit()




num1 = int( input("Enter first number:"))
num2 = int(input("Enter second number:"))
print("num1 + num2:",num1 + num2)
print("num1 - num2:",num1 - num2)
print("num1 * num2:",num1 * num2)
print("num1 / num2:",num1 / num2)

