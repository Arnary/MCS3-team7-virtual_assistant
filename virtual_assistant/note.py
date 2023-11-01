from address_book import Field
from collections import UserDict
from errors import NoteBodyMaxError


class NoteTitle(Field):
    pass


class NoteBody(Field):
    max_len = 512

    def __init__(self, body):
        validated = self.validate(body)
        super().__init__(validated)
    def validate(self, body):
        if len(body) > NoteBody.max_len:
            raise NoteBodyMaxError(f"Note cannot be more than {NoteBody.max_len} characters")


class NoteRecord:
    def __init__(self, title):
        self.title = NoteTitle(title)
        self.body = None

    def __str__(self):
        return f"{self.title.value}\n{self.body}"
    
    def add_body(self, body):
        self.body = NoteBody(body)


class NoteStorage(UserDict):
    # def __init__(self):
        #super().__init__()
        # path = os.path.realpath(os.path.dirname(__file__))
        # self.filename = f'{path}/db.pkl'
        # self.read_from_file()

    def add_record(self, record):
        self.data[str(record.title)] = record
        # self.save_to_file()

    def delete(self, title):
        del self.data[title]
        # self.save_to_file()

    # def save_to_file(self):
    #     with open(self.filename, "wb") as file:
    #         pickle.dump(self.data, file)

    # def read_from_file(self):
    #     try:
    #         with open(self.filename, "rb") as file:
    #             self.data = pickle.load(file)
    #     except (EOFError, FileNotFoundError):
    #         self.data = {}
