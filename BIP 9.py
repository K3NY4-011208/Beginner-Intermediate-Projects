filename = "todo.txt"

def load_tasks():
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(filename, "w") as file:
        for t in tasks:
            file.write(t + "\n")

tasks = load_tasks()

while True:
    print("\n--- To-Do Menu ---")
    print("1. Add")
    print("2. View")
    print("3. Remove")
    print("4. Quit")

    choice = input("Choice: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Added.")

    elif choice == "2":
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

    elif choice == "3":
        num = int(input("Task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            save_tasks(tasks)
            print("Removed.")
        else:
            print("Invalid number.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
