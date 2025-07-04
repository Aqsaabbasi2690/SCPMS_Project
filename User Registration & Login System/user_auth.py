import os


if not os.path.exists("data"):
    os.makedirs("data")

# option.1  
def register():
    name = input("Enter Your Name: ")
    password = input("Enter password: ")
    
    with open("data/users.txt", "a") as file:
        file.write(f"{name},{password}\n")
    print("Registered!")

# option 2
def login():
    name = input("Enter Your Name: ")
    password = input("Enter password: ")
    
    try:
        with open("data/users.txt", "r") as file:
            for line in file:
                saved_name, saved_password = line.strip().split(",")
                if name == saved_name and password == saved_password:
                    print("Login!")
                    with open("data/logged_in.txt", "w") as f:
                        f.write("authenticated")
                    return
        print("Invalid name or password.")
    except:
        print("No users found. Register first.")

print("1.Register")
print("2.Login")
print("3.Exit")

choice = input("Choose 1 or 3: ")

if choice == "1":
    register()
elif choice == "2":
    login()
elif choice == "3":
    exit()
else:
    print("Invalid choice.")
