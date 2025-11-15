contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Phone number: ")
        contacts[name] = number
        print("Contact added.")

    elif choice == "2":
        for name, number in contacts.items():
            print(f"{name}: {number}")

    elif choice == "3":
        name = input("Name to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Not found.")

    elif choice == "4":
        name = input("Name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Deleted.")
        else:
            print("Not found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
