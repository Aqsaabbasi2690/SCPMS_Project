#  To-DO_List-Manager


# first task
def add_task():
    task = input("Enter your task:")
    priority = input("Enter Your Priority task(first priority / second priority / third priority):")
    with open("task.txt", "a")as file:
     file.write(f"{task} | {priority} | Pending\n")
     print ("Task added!")


# second task
def view_tasks():
   print("Your Pending Tasks:")
   found = False
   with open ("task.txt", "r")as file:
      for line in file:
         parts = line.strip().split("|")
         if len(parts) ==3 and parts[2] == "Pending":
          print(f"{parts[0]} [{parts[1]} Priority ]")
          found = True
          break 
   if not found:
    print ("no pending tasks found")


# third task 
def mark_complete():
 taskname = input("Enter complete task:")
 lines = []
 found = False
 with open("task.txt","r")as file:
  for line in file:
   parts = line.strip().split("|")
   if parts[0] == taskname and parts[2] == "Pending":
     lines.append(f"{parts[0]} | {parts[1]} | Completed\n")
     found = True
   else:
     lines.append(line)
 with open("task.txt","w")as file:
  file.writelines(lines)
 if found:
  print("Task done")
 else:
  ("Task not found")


# forth task
def delete_task():
 task = input("Enter Task to Delete:")
 lines = []
 found = False
 with open("taxk.txt","r")as file:
   for line in file:
     if  not lines.startwith(task + "|"):
      lines.append(line)
     else:
         found = True
   if found:
        with open("task.txt", "w") as file:
            file.writelines(lines)
        print("Note deleted")
   else:
        print("Note not found")


# main section
def menu():
  while True:
    print("\n==== To_Do_List Manager ====")
    print("1.Add Task")
    print("2.View Pending Tasks")
    print("3.Mark Your Task")
    print("4.Delete Tasks")
    print("5.Exit")
  

    choice = input("Choose one option 1-5:")
    
    if choice == "1":
      add_task()
    elif choice == "2":
      view_tasks()
    elif choice == "3":
      mark_complete
    elif choice == "4":
      delete_task()
    elif choice == "5":
      exit()
      break
    else:
      ("Invalid choice")
menu()
