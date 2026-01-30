tasks = []

def menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Completed")
    print("4. Delete Task")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print("Task added")

    elif choice == "2":
        for i, t in enumerate(tasks):
            status = "Done" if t["done"] else "Pending"
            print(f"{i+1}. {t['task']} - {status}")

    elif choice == "3":
        num = int(input("Task number: ")) - 1
        tasks[num]["done"] = True
        print("Marked as completed")

    elif choice == "4":
        num = int(input("Task number: ")) - 1
        tasks.pop(num)
        print("Task deleted")

    elif choice == "5":
        break