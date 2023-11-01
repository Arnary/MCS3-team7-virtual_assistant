from address_book import Field
from collections import UserDict
from errors import NoteBodyMaxError


class NoteTitle(Field):
    pass


class NoteBody(Field):
    max_len = 512

    def __init__(self, value):
        validated = self.validate(value)
        super().__init__(validated)

    def validate(self, value):
        if len(value) > NoteBody.max_len:
            raise NoteBodyMaxError(f"Note cannot be more than {NoteBody.max_len} characters")
        else:
            return value


class NoteRecord:
    def __init__(self, title):
        self.title = NoteTitle(title)
        self.body = None

    def __str__(self):
        result = "\n"+"~"*10+"\n"
        result += f"{self.title.value}\n{self.body}"
        result += "\n"+"~"*10
        return result
    
    def add_body(self, body):
        self.body = NoteBody(body)


class NoteBook(UserDict):
    def add_record(self, record):
        self.data[str(record.title)] = record

    def delete(self, title):
        del self.data[title]
