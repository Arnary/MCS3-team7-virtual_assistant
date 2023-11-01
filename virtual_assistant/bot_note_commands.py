from errors import input_error


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_note(args, ):
    pass


# def delete_note(args, ):
#     title, = args
#     if title in book.keys():
#         book.delete(title)
#         return "Note deleted."
#     # else:
#     #     raise KeyError