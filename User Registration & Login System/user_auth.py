import os


if not os.path.exists("data"):
    os.makedirs("data")

#  Register
def register():
    name = input("Enter Your Name: ")
    password = input("Enter password: ")

 
    if os.path.exists("data/users.txt"):
        with open("data/users.txt", "r") as file:
            for line in file:
                saved_name, _ = line.strip().split(",")
                if name == saved_name:
                    print("User already exists. Please login.")
                    return

    with open("data/users.txt", "a") as file:
        file.write(f"{name},{password}\n")
    print("Registered , Now Please Log in !")

# Login
def login():
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        name = input("Enter Your Name: ")
        password = input("Enter password: ")

        try:
            with open("data/users.txt", "r") as file:
                found_user = False
                for line in file:
                    saved_name, saved_password = line.strip().split(",")
                    if name == saved_name and password == saved_password:
                        print("Login successful!")
                        with open("data/logged_in.txt", "w") as f:
                            f.write("authenticated")
                        return True 
                if not found_user:
                    print("Wrong credentials, try again.")
                    attempts += 1
        except FileNotFoundError:
            print("No users found. Please register first.")
            return False 
    
    print(f"You have entered wrong details for {max_attempts} times.")
    print("Returning to the main menu.")
    return False


def main_menu():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose 1, 2, or 3: ")

        if choice == "1":
            register()
        elif choice == "2":
            login_successful = login()
 
            pass 
        elif choice == "3":
            print(" program end.")
            exit()
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()
