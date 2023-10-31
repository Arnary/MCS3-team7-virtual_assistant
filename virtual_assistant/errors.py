class ValueMinError(Exception):
    """ Value less than min """
class ValueMaxError(Exception):
    """ Value more than max """


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
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

            return "Invalid command."
        except IndexError:
            if func.__name__ == "set_address": 
                return "Give me name and address please."
            return "You don't have any contacts yet."
        except (ValueMinError, ValueMaxError) as e:
            return e

    return inner
