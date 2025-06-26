#option.1

def register():
    name = input("Enter Your Name: ")
    password = input("Enter password: ")
    
    with open("users.txt", "a") as file:
        file.write(f"{name},{password}\n")
    print(" Registered!")

 # option 2
def login():
   
    name = input("Enter Your Name: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as file:
     for line in file:
        saved_name, saved_password = line.strip().split(",")
        if name == saved_name and password == saved_password:
            print("Login!")
            return
    print("Invalid name or password.")
print("Register")
print("Login")

choice = input("Choose 1 or 2: ")

if choice == "1":
    register()
elif choice == "2":
    login()
else:
    print("Invalid choice.")
