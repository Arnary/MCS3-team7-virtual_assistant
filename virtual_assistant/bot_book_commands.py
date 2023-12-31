from errors import input_error, ValueMaxError
from address_book import Record


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book): 
    name, phone = args
    if name not in book.keys():
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
    else:
        if book[name].find_phone(phone) == phone:
            return "This phone number already exist."
        else:
            book[name].add_phone(phone)

    return "Contact added."


@input_error
def change_contact(args, book):  
    name, old_phone, new_phone = args
    if name in book.keys():
        book[name].edit_phone(old_phone, new_phone)
        book.add_record(book[name])
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, book):  
    name, = args
    if name in book.keys():
        phones = [str(phone) for phone in book[name].phones]
        return "\n".join(phones)
    else:
        raise KeyError


@input_error
def show_all(args, book):
    if book == {}:
        raise IndexError
    return "".join([f"{contact}\n" for contact in book.values()])


@input_error
def phone_delete(args, book): 
    name, phone = args
    if name in book.keys():
        book[name].remove_phone(phone)
        book.add_record(book[name])
        return "Phone deleted."
    else:
        raise KeyError


@input_error
def set_email(args, book):
    name, email = args
    record = book.find(name)
    if record is not None:
        result = record.set_email(email)
        if result:
            book.add_record(record)
        return result
    else:
        raise KeyError


@input_error
def remove_email(args, book):
    name, = args
    record = book.find(name)
    if record is not None:
        result = record.remove_email()
        if result:
            book.add_record(record)
        return result
    else:
        raise KeyError


@input_error
def set_address(args, book):
        if len(args) < 2:
            raise ValueError

        name = args[0]
        address = " ".join(args[1:])
        record = book.find(name)
        if record is not None:
            result = record.set_address(address)
            if result:
                book.add_record(record)
            return result
        else:
            raise KeyError


@input_error    
def remove_address(args, book):
    name, = args
    record = book.find(name)

    if record is not None:
        result = record.remove_address()
        if result:
            book.add_record(record)
        return result
    raise KeyError


@input_error
def add_birthday(args, book): 
    name, birthday = args
    if name in book.keys():
        book[name].add_birthday(birthday)
        book.add_record(book[name])
        return "Birthday added to contact."
    else:
        raise KeyError

        
@input_error
def delete_birthday(args, book):
    name, = args
    if name in book.keys() and book[name].birthday is None:
        return f"\"{name}\" doesn't have birthday."
    elif name in book.keys() and book[name].birthday is not None:
        book[name].remove_birthday()
        book.add_record(book[name])
        return "Birthday was deleted."
    else:
        raise ValueError

        
@input_error
def show_birthday(args, book):
    name, = args
    if name in book.keys() and book[name].birthday is None:
        return "There is no birthday record for this contact."
    elif name in book.keys():
        return book[name].birthday
    else:
        raise KeyError


@input_error
def birthdays(args, book):
    if len(args) < 1:
        raise ValueError
    
    date_range = int(args[0])
    if not 0 < date_range < 365:
        raise ValueMaxError
    if book == {}:
        raise IndexError
    else:
        return book.get_next_birthdays(date_range)


@input_error
def delete_contact(args, book):
    name, = args
    if name in book.keys():
        book.delete(name)
        return "Contact deleted."
    else:
        raise KeyError
    

@input_error
def search(args, book):
    search_line, = args
    return book.search(search_line)


def greating(*args):
    return "How can I help you?"


commands_addressbook = {
    "hello": {
        "action": greating,
        "description": "hello"
    },
    "add": {
        "action": add_contact,
        "description": "add 'name' 'phone number'"
    },
    "change": {
        "action": change_contact,
        "description": "change 'name' 'old phone number' 'new phone number'"
    },
    "delete-contact": {
        "action": delete_contact,
        "description": "delete-contact 'name'"
    },
    "all": {
        "action": show_all,
        "description": "all"
    },
    "phone": {
        "action": show_phone,
        "description": "phone 'name'"
    },
    "delete-phone": {
        "action": phone_delete,
        "description": "delete-phone 'name' 'phone number'"
    },
    "add-birthday": {
        "action": add_birthday,
        "description": "add-birthday 'name' 'birthday in format DD.MM.YYYY'"
    },
    "delete-birthday": {
        "action": delete_birthday,
        "description": "delete-birthday 'name'"
    },
    "show-birthday": {
        "action": show_birthday,
        "description": "show-birthday 'name'"
    },
    "birthdays": {
        "action": birthdays,
        "description": "birthdadys 'number of days'"
    },
    "add-email": {
        "action": set_email,
        "description": "add-email 'name' 'email'"
    },
    "delete-email": {
        "action": remove_email,
        "description": "delete-email 'name'"
    },
    "add-address": {
        "action": set_address,
        "description": "add-address 'name' 'address'"
    },
    "delete-address": {
        "action": remove_address,
        "description": "remove_address 'name'"
    },
    "search": {
        "action": search,
        "description": "search 'two or more characters to search for'"
    }
}
