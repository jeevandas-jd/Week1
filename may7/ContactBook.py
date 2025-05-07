class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.file_path = "may7/contactBook.txt"

    def load_contacts(self):
        self.contacts.clear()
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    if ',' in line:
                        name, number = line.strip().split(",", 1)
                        self.contacts[name] = number
        except FileNotFoundError:
            open(self.file_path, "a").close()  # create file if it doesn't exist
        return self.contacts

    def add_contact(self):
        name = input("Name: ").strip()
        number = input("Phone Number: ").strip()
        self.contacts[name] = number
        with open(self.file_path, "a") as file:
            file.write(f"{name},{number}\n")
        print("Contact added!")

    def search_contact(self):
        name = input("Search name: ").strip()
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
        else:
            print("Contact not found.")


def main():
    book = ContactBook()
    print("Welcome to Simple Contact Book!")

    while True:
        print("\nChoose an option:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. List All Contacts")
        print("4. Exit")

        choice = input("Enter 1-4: ").strip()

        if choice == "1":
            book.add_contact()
        elif choice == "2":
            book.load_contacts()
            book.search_contact()
        elif choice == "3":
            contacts = book.load_contacts()
            if contacts:
                print("\nYour Contacts:")
                for name, number in contacts.items():
                    print(f"- {name}: {number}")
            else:
                print("No contacts yet.")
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
