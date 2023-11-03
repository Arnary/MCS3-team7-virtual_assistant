from address_book import Field
from collections import UserDict
from errors import NoteBodyMaxError, NoteNotExistException


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
        self.tags = []

    def __str__(self):
        result = "\n"+"~"*10+"\n"
        result += f"Title: {self.title.value}\nBody: {self.body}"
        if len(self.tags) > 0:
            tags = [str(tag) for tag in self.tags]
            result += f"\nTags: [{', '.join(tags)}]"
        result += "\n"+"~"*10
        return result
    
    def add_body(self, body):
        self.body = NoteBody(body)

    def add_tags(self, tags):
        for tag in tags:
            self.tags.append(Tag(tag))

        return "Tags added."


class NoteBook(UserDict):
    def add_record(self, record):
        self.data[str(record.title)] = record

    def delete(self, title):
        del self.data[title]

    def find(self, title):
        record = self.data.get(title)

        if not record:
            raise NoteNotExistException

        return record

    def search_by_tag(self, search_tag):
        result = []

        for record in self.data.values():
            for tag in record.tags:
                if tag.value == search_tag:
                    result.append(record)

        return result 


class Tag(Field):
    def __init__(self, value):
        if value[0] == '#':
            value = value[1:]
        super().__init__(value)

    def __str__(self):
        return '\033[94m' + '#' + self.value + '\033[0m'
        
