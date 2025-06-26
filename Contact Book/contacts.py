
import csv

contact_file = "contacts.csv"

# option 1
def add_contact():
    Name = input("Enter Name: ")
    Phone = input("Enter Phone No: ")
    Email = input("Enter  Email: ")
    Address = input("Enter Address: ")

    with open(contact_file, "a", newline='') as file:
        writer = csv.writer(file) # prepare file to write csv rows
        writer.writerow([Name, Phone, Email, Address])
    print("Contact added\n")


# option 2
def view_contacts():
    try:
        with open(contact_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print("Name:", row[0], "| Phone:", row[1], "| Email:", row[2], "| Address:", row[3])
    except FileNotFoundError:
        print("No contacts found")


# option 3
def edit_contact():
    name_to_edit = input("Enter Name of contact to edit: ")
    new_name = input("Enter new Name: ")
    new_phone = input("Enter new Phone No: ")
    new_email = input("Enter new Email: ")
    new_address = input("Enter new Address: ")

    data = []
    found = False
    with open(contact_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name_to_edit:
                data.append([new_name, new_phone, new_email, new_address])
                found = True
            else:
                data.append(row)

    if found:
        with open(contact_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("Contact updated\n")
    else:
        print("Contact not found\n")


# option 4
def delete_contact():
    name_to_delete = input("Enter Name of contact to delete: ")
    lines = []
    found = False
    with open(contact_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != name_to_delete:
                lines.append(row)
            else:
                found = True

    if found:
        with open(contact_file, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lines)
        print("Contact deleted\n")
    else:
        print("Contact not found\n")


# option 5
def search_contact():
    name_to_search = input("Enter Name of contact to search: ")
    found = False
    with open(contact_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name_to_search:
                print("Name:", row[0], "| Phone:", row[1], "| Email:", row[2], "| Address:", row[3])
                found = True
                break
    if not found:
        print("Contact not found\n")


# main function

def contact_menu():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add\n2. View\n3. Search\n4. Edit\n5. Delete\n6. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            exit()
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    contact_menu()   
