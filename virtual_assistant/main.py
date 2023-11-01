from address_book import AddressBook, SaveManager
from bot_book_commands import *


def main():
    book = AddressBook()
    saved_data = SaveManager.read_from_file()

    if saved_data:
        saved_book = saved_data["book"]
        # saved_notes = saved_data["notes"]
        book = AddressBook(saved_book)
        print("Address book has been loaded from file.")

    print("Welcome to the assistant bot! \nType help to see the available commands.")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            SaveManager.save_to_file({"book": book, "notes": None}) # TODO: save notes
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "delete-birthday":
            print(delete_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        elif command == "delete-contact":
            print(delete_contact(args, book))
        elif command == "delete-phone":
            print(phone_delete(args, book))
        elif command == "add-email":
            print(set_email(args, book))
        elif command == "delete-email":
            print(remove_email(args, book))
        elif command == "add-address":
            print(set_address(args, book))
        elif command == "delete-address":
            print(remove_address(args, book))
        elif command == "help":
            print(show_help())
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
