filename = "notes.txt"

while True:
    print("\n--- File Menu ---")
    print("1. Read file")
    print("2. Write to file")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            with open(filename, "r") as file:
                print("\n--- File Contents ---")
                print(file.read())
        except FileNotFoundError:
            print("File not found. Write something first.")

    elif choice == "2":
        text = input("Enter text to add: ")
        with open(filename, "a") as file:
            file.write(text + "\n")
        print("Text added.")

    elif choice == "3":
        break

    else:
        print("Invalid choice.")
