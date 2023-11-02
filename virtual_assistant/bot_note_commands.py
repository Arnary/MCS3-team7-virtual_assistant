from errors import input_error
from note import NoteRecord


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_note(args, notebook):
    title = args[0]
    body = " ".join(args[1:])
    if title not in notebook.keys():
        record = NoteRecord(title)
        record.add_body(body)
        notebook.add_record(record)
    else:
        notebook[title].add_body(body)
    return "Note added."


@input_error
def show_notes(args, notebook): 
    if notebook == {}:
        raise IndexError
    return "".join([f"{note}\n" for note in notebook.values()])


@input_error
def delete_note(args, notebook):
    title, = args
    if title in notebook.keys():
        notebook.delete(title)
        return "Note deleted."
    else:
        raise KeyError


commands_notes = {
    "add-note": {
        "action": add_note,
        "description": "add-note ..."
    }, 
    "show-notes": {
        "action": show_notes,
        "description": "show-notes ..."
    }, 
    "delete-note": {
        "action": delete_note,
        "description": "delete-note ..."
    }
}