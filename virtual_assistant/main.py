from prompt_toolkit import prompt
from dynamic_completer import DynamicCompleter

from address_book import AddressBook, SaveManager
from note import NoteBook
from bot_book_commands import *
from bot_note_commands import *


def show_help(cmds):
    result = "\n"
    for item in cmds.values():
        if 'description' in item:
            result += f"# {item['description']}\n"
    return result

def main():
    book = AddressBook()
    notebook = NoteBook()
    saved_data = SaveManager.read_from_file()

    commands = {}
    for item in [commands_addressbook, commands_notes]:
        commands.update(item) 
    
    autocomplete_commands = list(commands.keys())

    if saved_data:
        saved_book = saved_data["book"]
        saved_notebook = saved_data["notebook"]
        book = AddressBook(saved_book)
        notebook = NoteBook(saved_notebook)
        print("Address book has been loaded from file.")
    
    print("Welcome to the assistant bot! \nType help to see the available commands.")

    while True:

        user_input = prompt("Enter a command: ", completer=DynamicCompleter(autocomplete_commands))
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            SaveManager.save_to_file({"book": book, "notebook": notebook})
            print("Good bye!")
            break
        elif command in commands_addressbook:
            print(commands[command]["action"](args, book))
        elif command in commands_notes:
            print(commands_notes[command]["action"](args, notebook))
        elif command == 'help':
            print(show_help(commands))
        else:
            print("Invalid command.")
        

if __name__ == "__main__":
    main()
