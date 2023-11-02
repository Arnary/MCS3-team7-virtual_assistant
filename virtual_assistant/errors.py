class ValueMinError(Exception):
    """ Value less than min """
class ValueMaxError(Exception):
    """ Value more than max """
class NoteBodyMaxError(Exception):
    """ Body more than max """

class NoteNotExistException(Exception):
    pass

class TagsArgsException(Exception):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            if func.__name__ == "delete_note": 
                return "Note does not exist."
            return "Contact not found."
        except ValueError as ex:
            if str(ex) == "Phone is in the wrong format.":
                return "Phone is in the wrong format."
            elif str(ex) == "Date is in the wrong format.":
                return "Date is in the wrong format."
            elif str(ex) == "Email is in the wrong format.":
                return "Email is in the wrong format."
            elif func.__name__ == "add_contact" or func.__name__ == "phone_delete":
                return "Give me name and phone please."
            elif func.__name__ == "change_contact":
                return "Give me name, old phone and new phone please."
            elif func.__name__ == "add_birthday":
                return "Give me name and birthday please."
            elif func.__name__ == "show_phone" or func.__name__ == "show_birthday" or func.__name__ == "delete_contact" or func.__name__ == "remove_address":
                return "Give me name please."
            elif func.__name__ == "set_email" or func.__name__ == "remove_email":
                return "Give me name and email please."
            elif func.__name__ == "birthdays":
                return "Give me date range please."
            elif func.__name__ == "set_address": 
                return "Give me name and address please."
            elif func.__name__ == "add_note":
                return "Give me title and note's text please."
            elif func.__name__ == "delete_note":
                return "Give me title please."
            elif func.__name__ == "add_tags":
                return "Give me title and tags please."

            return "Invalid command."  
        except IndexError:
            if func.__name__ == "show_notes":
                return "You don't have any notes yet."
            return "You don't have any contacts yet.
        except (ValueMinError, ValueMaxError, NoteBodyMaxError) as e:
            if func.__name__ == "birthdays":
                return "Date range should be more than 0 and less than 365"
            return e
        except NoteNotExistException:
            return "Note does not exists." 
        except TagsArgsException:
            return "Please provide tags."

    return inner
