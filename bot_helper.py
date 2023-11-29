def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Please write contact info in the correct format."
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Please write contact info in the correct format."
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "No such contact."


def get_phone(args, contacts):
    try:
        name = args[0]
    except ValueError:
        return "Please write contact info in the correct format."
    if name not in contacts:
        return "No such contact."
    return contacts[name]


def get_all_contacts(contacts):
    if contacts == {}:
        return "You have no contacts."
    all_contacts = ""
    for name, phone in contacts.items():
        all_contacts += f"{name}: {phone}\n"
    return all_contacts.strip()


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
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
