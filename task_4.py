def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError as e:
        return f"Error adding contact: {e}"


def change_contact(args, contacts):
    try:
        name, phone = args
        if name not in contacts:
            raise ValueError("Contact not found.")
        contacts[name] = phone
        return 'Contact updated successfully'
    except ValueError as e:
        return f"Error adding contact: {e}"


def show_contact(args, contacts):
    try:
        name, _ = args
        return contacts[name]
    except ValueError as e:
        return f"Error adding contact: {e}"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "show":
            print(show_contact(args, contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
