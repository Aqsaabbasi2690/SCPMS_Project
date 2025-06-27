# option 1
def add():
    date = input("Enter date to add note: ")
    note = input("Write your note: ")
    with open("notes.txt", "a") as file:
        file.write(date + ":" + note + "\n")
    print("Note added")



# option 2
def view():
    date = input("Enter date to view notes: ")
    found = False
    with open("notes.txt", "r") as file:
        for line in file:
            if line.startswith(date + ":"):
                print("Note:",  line.strip().split(":")[1])
                found = True
                break
    if not found:
        print("Note not found")



# option 3
def edit():
    date = input("Enter date to edit note: ")
    new_note = input("Enter new note: ")
    lines = []
    found = False
    with open("notes.txt", "r") as file:
        for line in file:
            if line.startswith(date + ":"):
                lines.append(date + ":" + new_note + "\n")
                found = True
            else:
                lines.append(line)
    if found:
        with open("notes.txt", "w") as file:
            file.writelines(lines)
        print("Note updated")
    else:
        print("Note not found")



#  option 4 
def delete():
    date = input("Enter date to delete note: ")
    lines = []
    found = False
    with open("notes.txt", "r") as file:
        for line in file:
            if not line.startswith(date + ":"):
                lines.append(line)
            else:
                found = True
    if found:
        with open("notes.txt", "w") as file:
            file.writelines(lines)
        print("Note deleted")
    else:
        print("Note not found")


        
# main part
while True:
    print("1.Add Note")
    print("2.View Note")
    print("3.Edit Note")
    print("4.Delete Note")
    print("5.Exit")
    choice = input("Choose an option 1-5 : ")

    match choice:
        case "1":
            add()
        case "2":
            view()
        case "3":
            edit()
        case "4":
            delete()
        case "5":
            exit()
            break
        case _:
            print("Invalid choice")
