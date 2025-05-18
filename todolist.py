from turtledemo.penrose import start

tasks = []
index = 1


while True:
    print("Choose your action")
    choice = input("Type '1' To add a new task \n Type '2' if you want to delete a task \n Type '3' if you want to view all the tasks \n Type '4' To Mark task as completed")
    if choice == '1':
        task = input("Enter your task: ")
        tasks.append({"task": task, "done": False})
    elif choice == '2':
        num = int(input("Enter the task number you want to delete"))
        deleted_task = tasks.pop(num)
        print(f"Task number {num} is successfully deleted")

    elif choice == '3':
        for x in tasks:
            print(x)

    elif choice == '4':
       if not tasks:
           print("No Tasks are available")
       else:
           print("Your Tasks: \n")
           for index , task in enumerate(tasks, start = 0):
               status = '✔️' if task["done"] else '❌'
               print(f"{index}.[{status}] {task['task']}")

           sure = input("\nDo you still want to mark a task as completed? (y/n): ").lower()
           if sure == 'y':
               try:
                   comp = int(input("Enter the task number you want to mark as completed"))

                   if 0 <= comp <= len(tasks):
                       tasks[comp]["done"] = True
                       print(f"Task{comp} mark as completed")

                   else:
                       print("Enter a valid task number")

               except ValueError:
                   print("Enter a valid number")

    else:
        print("You chose not to mark any task as completed")
        break


    qui = input('You want to quit y/n')
    if qui == 'y':
        break