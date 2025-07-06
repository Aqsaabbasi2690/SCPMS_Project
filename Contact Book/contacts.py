import os
import csv
import time
import re

os.makedirs("data", exist_ok=True)
contact_file = "data/contacts.csv"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_contact():
    clear_screen()
    print("\n--- Add New Contact ---")
    
    Name = input("Enter Name: ").strip()
    if not Name:
        print("Contact Name cannot be empty. Aborting.")
        input("Press Enter to continue...")
        return

    Phone = ""
    while True:
        Phone = input("Enter Phone No (digits only, e.g., 09801234567): ").strip()
        if not Phone:
            print("Phone number cannot be empty.")
            continue
        if not Phone.isdigit():
            print("Invalid phone number. Please enter digits only.")
        else:
            break

    Email = ""
    while True:
        Email = input("Enter Email (e.g., example@gmail.com): ").strip()
        if not Email:
            print("Email cannot be empty.")
            continue
        if not re.match(r"[^@]+@[^@]+\.[^@]+", Email):
            print("Invalid email format. Please enter a valid email address.")
        else:
            break

    Address = input("Enter Address: ").strip()
    if not Address:
        print("Address cannot be empty.")

    try:
        with open(contact_file, "a", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([Name, Phone, Email, Address])
        print("Contact added successfully!")
        time.sleep(1)
    except Exception as e:
        print(f"Error adding contact: {e}")
        time.sleep(1.5)
    finally:
        input("Press Enter to continue...")

def view_contacts():
    clear_screen()
    print("\n--- Your Contacts ---")
    try:
        with open(contact_file, "r", encoding='utf-8') as file:
            reader = csv.reader(file)
            contacts = list(reader)

            if not contacts:
                print("No contacts found.")
                
            else:
                for i, row in enumerate(contacts):
                    name = row[0] if len(row) > 0 else "N/A"
                    phone = row[1] if len(row) > 1 else "N/A"
                    email = row[2] if len(row) > 2 else "N/A"
                    address = row[3] if len(row) > 3 else "N/A"
                    print(f"{i+1}. Name: {name} | Phone: {phone} | Email: {email} | Address: {address}")
    except FileNotFoundError:
        print("No contacts file found. Please add contacts first.")
    except Exception as e:
        print(f"An error occurred while viewing contacts: {e}")
    finally:
        input("Press Enter to continue...")

def search_contact():
    clear_screen()
    print("\n--- Search Contact ---")
    name_to_search = input("Enter Name of contact to search: ").strip()
    if not name_to_search:
        print("Search name cannot be empty. Aborting search.")
        input("Press Enter to continue...")
        return

    found = False
    try:
        with open(contact_file, "r", encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0 and row[0].lower() == name_to_search.lower():
                    print("\n--- Contact Found ---")
                    name = row[0] if len(row) > 0 else "N/A"
                    phone = row[1] if len(row) > 1 else "N/A"
                    email = row[2] if len(row) > 2 else "N/A"
                    address = row[3] if len(row) > 3 else "N/A"
                    print(f"Name: {name} | Phone: {phone} | Email: {email} | Address: {address}")
                    found = True
                    break
        if not found:
            print(f"Contact '{name_to_search}' not found.")
    except FileNotFoundError:
        print("No contacts file found.")
    except Exception as e:
        print(f"An error occurred while searching: {e}")
    finally:
        input("Press Enter to continue...")


def edit_contact():
    clear_screen()
    print("\n--- Edit Contact ---")
    try:
        with open(contact_file, "r", encoding='utf-8') as file:
            reader = csv.reader(file)
            contacts = list(reader)

        if not contacts:
            print("No contacts to edit.")
            input("Press Enter to continue...")
            return
        
        print("\n--- Select Contact to Edit ---")
        for i, row in enumerate(contacts):
            name = row[0] if len(row) > 0 else "N/A"
            print(f"{i+1}. Name: {name}")
        print("--------------------")

        selected_index = -1
        while True:
            try:
                choice = input("Enter the number of the contact to edit (or '0' to cancel): ").strip()
                if choice == '0':
                    print("Edit cancelled.")
                    input("Press Enter to continue...")
                    return

                selected_index = int(choice) - 1
                if 0 <= selected_index < len(contacts):
                    break
                else:
                    print("Invalid contact number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An unexpected error occurred during selection: {e}")
                input("Press Enter to continue...")
                return

        current_contact_padded = contacts[selected_index] + ["", "", "", ""] 
        current_name = current_contact_padded[0]
        current_phone = current_contact_padded[1]
        current_email = current_contact_padded[2]
        current_address = current_contact_padded[3]

        print(f"\n--- Editing Contact: {current_name} (Index: {selected_index + 1}) ---")
        
        updated_any_field = False

        while True:
            print("\nWhat do you want to change for this contact?")
            print(f"1. Name (current: {current_name or 'N/A'})")
            print(f"2. Phone No (current: {current_phone or 'N/A'})")
            print(f"3. Email (current: {current_email or 'N/A'})")
            print(f"4. Address (current: {current_address or 'N/A'})")
            print("5. Save Changes and Return")
            print("6. Discard Changes and Return")

            field_choice = input("Enter your choice (1-6): ").strip()

            if field_choice == "1":
                new_name = input(f"Enter new Name (leave blank to keep current: {current_name}): ").strip()
                if new_name:
                    contacts[selected_index][0] = new_name
                    current_name = new_name
                    updated_any_field = True
                    print("Name updated in memory.")
                else:
                    print("Name not changed.")
            elif field_choice == "2":
                new_phone = input(f"Enter new Phone No (leave blank to keep current: {current_phone}): ").strip()
                if new_phone:
                    if not new_phone.isdigit():
                        print("Invalid phone number. Please enter digits only.")
                    else:
                        while len(contacts[selected_index]) <= 1:
                            contacts[selected_index].append("")
                        contacts[selected_index][1] = new_phone
                        current_phone = new_phone
                        updated_any_field = True
                        print("Phone No updated in memory.")
                else:
                    print("Phone No not changed.")
            elif field_choice == "3":
                new_email = input(f"Enter new Email (leave blank to keep current: {current_email}): ").strip()
                if new_email:
                    if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
                        print("Invalid email format. Please enter a valid email address.")
                    else:
                        while len(contacts[selected_index]) <= 2:
                            contacts[selected_index].append("")
                        contacts[selected_index][2] = new_email
                        current_email = new_email
                        updated_any_field = True
                        print("Email updated in memory.")
                else:
                    print("Email not changed.")
            elif field_choice == "4":
                new_address = input(f"Enter new Address (leave blank to keep current: {current_address}): ").strip()
                if new_address:
                    while len(contacts[selected_index]) <= 3:
                        contacts[selected_index].append("")
                    contacts[selected_index][3] = new_address
                    current_address = new_address
                    updated_any_field = True
                    print("Address updated in memory.")
                else:
                    print("Address not changed.")
            elif field_choice == "5":
                if updated_any_field:
                    with open(contact_file, "w", newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerows(contacts)
                    print("Contact saved successfully!")
                else:
                    print("No changes were made to save.")
                input("Press Enter to continue...")
                return
            elif field_choice == "6":
                print("Changes discarded. Returning to Contact Book menu.")
                input("Press Enter to continue...")
                return
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
            time.sleep(0.5) 

    except FileNotFoundError:
        print("No contacts file found. Add contacts first.")
        input("Press Enter to continue...")
    except Exception as e:
        print(f"An unexpected error occurred during edit: {e}")
        input("Press Enter to continue...")


def delete_contact():
    clear_screen()
    print("\n--- Delete Contact ---")
    try:
        with open(contact_file, "r", encoding='utf-8') as file:
            reader = csv.reader(file)
            contacts = list(reader)

        if not contacts:
            print("No contacts to delete.")
            input("Press Enter to continue...")
            return

        print("\n--- Select Contact to Delete ---")
        for i, row in enumerate(contacts):
            name = row[0] if len(row) > 0 else "N/A"
            print(f"{i+1}. Name: {name}")
        print("------------------------------")

        while True:
            try:
                choice = input("Enter the number of the contact to delete (or '0' to cancel): ").strip()
                if choice == '0':
                    print("Delete cancelled.")
                    input("Press Enter to continue...")
                    return

                contact_index = int(choice) - 1
                if 0 <= contact_index < len(contacts):
                    deleted_contact_name = contacts[contact_index][0] if len(contacts[contact_index]) > 0 else "Unnamed Contact"
                    contacts.pop(contact_index) 

                    with open(contact_file, "w", newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerows(contacts)
                    print(f"Contact '{deleted_contact_name}' deleted successfully!")
                    input("Press Enter to continue...")
                    return
                else:
                    print("Invalid contact number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An unexpected error occurred during delete selection: {e}")
                input("Press Enter to continue...")
                return

    except FileNotFoundError:
        print("No contacts file found.")
        input("Press Enter to continue...")
    except Exception as e:
        print(f"An error occurred while preparing to delete contacts: {e}")
        input("Press Enter to continue...")


def contact_menu():
    while True:
        clear_screen()
        print("\n--- Contact Book ---")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Return to Main Menu")

        choice = input("Choose an option (1-6): ").strip()

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
            print("Returning to SCPMS Main Menu...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            time.sleep(1.5)


if __name__ == "__main__":
    contact_menu()
