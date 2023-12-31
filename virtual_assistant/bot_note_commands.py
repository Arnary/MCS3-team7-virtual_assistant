from collections import Counter
from errors import TagsArgsException, input_error
from note import NoteRecord


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_note(args, notebook):
    if len(args) < 2:
            raise ValueError
    
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
def add_tags(args, notebook):
    if len(args) < 2:
        raise ValueError
    title = args[0]
    tags = args[1:]

    if len(tags) == 0:
        raise TagsArgsException

    record = notebook.find(title)

    return record.add_tags(tags)


@input_error
def search_by_tag(args, notebook):
    if len(args) == 0:
        raise TagsArgsException
    
    matched_notes = []

    for tag in args:
        notes = notebook.search_by_tag(tag)
        matched_notes.extend(notes)

    matched_notes_counts = Counter(matched_notes)  

    if len(matched_notes_counts) == 0:
        return f"No search results for the tag '{tag}.'" 

    return "".join([f"{note}\n" for note in matched_notes_counts.keys()])


@input_error
def delete_note(args, notebook):
    title, = args
    if title in notebook.keys():
        notebook.delete(title)
        return "Note deleted."
    else:
        raise KeyError


@input_error
def search_note(args, notebook):
    search_line, = args
    return notebook.search_note(search_line)


commands_notes = {
    "add-note": {
        "action": add_note,
        "description": "add-note 'title in one word' 'body of your note'"
    }, 
    "show-notes": {
        "action": show_notes,
        "description": "show-notes"
    }, 
    "delete-note": {
        "action": delete_note,
        "description": "delete-note 'title'"
    }, 
    "search-note": {
        "action": search_note,
        "description": "search-note 'two or more characters to search for'" 
    }, 
    "add-tags": {
        "action": add_tags,
        "description": "add-tags 'title' 'tag' - second and further tags are optional" 
    }, 
    "search-by-tag": {
        "action": search_by_tag,
        "description": "search_by_tag 'tag' - second and further tags are optional" 
    }
}
