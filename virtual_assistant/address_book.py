from collections import defaultdict, UserDict
from datetime import datetime
import re
import os
import pickle
from errors import ValueMinError, ValueMaxError


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if any((not value.isdigit(), len(value) != 10)):
            raise ValueError("Phone is in the wrong format.")
        super().__init__(value)


class Email(Field):
    def __init__(self, value):
        validated = self.validate(value)
        super().__init__(validated)

    def validate(self, value):
        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, value):
            return value
        else:
            raise ValueError("Email is in the wrong format.")


class Birthday(Field):
    def __init__(self, value):
        birthday_validation = r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$'
        if not re.match(birthday_validation, value):
            raise ValueError("Date is in the wrong format.")
        super().__init__(value)


class Address(Field):
    min_len = 3
    max_len = 512
     
    def __init__(self, value):
        validated = self.validate(value)
        super().__init__(validated)

    def validate(self, value):
        if len(value) > Address.min_len and len(value) < Address.max_len:
            return value
        elif len(value) < Address.min_len:
            raise ValueMinError(f"Address cannot be less than {Address.min_len} characters")
        elif len(value) > Address.max_len:
            raise ValueMaxError(f"Address cannot be more than {Address.max_len} characters")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.email = None

    def __str__(self):
        result = "\n"+"*"*10+"\n"
        result += f"Contact name: {self.name.value}"
        
        if len(self.phones):
            result += f"\nphones: {'; '.join(p.value for p in self.phones)}"

        if self.email is not None:
            result += f"\nemail: {self.email.value}"

        if self.address is not None:
            result += f"\naddress: {self.address.value}"

        if self.birthday is not None:
            result += f"\nbirthday: {self.birthday}"

        result += "\n"+"*"*10
        return result

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        for idx, abook_phone in enumerate(self.phones):
            if str(abook_phone) == phone:
                self.phones.pop(idx)
                break

    def edit_phone(self, old_phone, new_phone):
        for idx, phone in enumerate(self.phones):
            if str(phone) == old_phone:
                self.phones[idx] = Phone(new_phone)

    def find_phone(self, phone):
        for abook_phone in self.phones:
            if str(abook_phone) == phone:
                return phone
        return "Phone not found"

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
    
    def remove_birthday(self):
        self.birthday = None

    def set_email(self, email):
        try:
            self.email = Email(email)
            return "Email added successfully."
        except Exception as e:
            raise e

    def remove_email(self):
        try:
            if self.email.value is not None:
                self.email = None
                return "Email removed successfully."
        except Exception:
            return f"\"{self.name.value}\" does not have email"
    
    def set_address(self, value):
        try:
            self.address = Address(value)
            return "Address setted successfully"
        except Exception as e:
            raise e

    def remove_address(self):
        try:
            if self.address.value is not None:
                self.address = None
                return "Address removed successfully"
        except Exception:
            return f"\"{self.name.value}\" does not have address."


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[str(record.name)] = record
      
    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def get_next_birthdays(self, date_range):
        self.date_range = int(date_range)
        happy_days = defaultdict(list)
        current_day = datetime.today().date()
        for name, record in self.data.items():
            if record.birthday is None:
                continue
            user_Bday = datetime.strptime(str(record.birthday), '%d.%m.%Y')
            user_Bday = datetime.date(user_Bday)
            birthday_this_year = user_Bday.replace(year=current_day.year)

            if birthday_this_year < current_day:
                birthday_this_year = birthday_this_year.replace(
                    year=current_day.year+1)
            delta_days = (birthday_this_year - current_day).days

            if delta_days < self.date_range:
                birthday_date = birthday_this_year.strftime('%A, %B %d %Y')
                happy_days[birthday_date].append(name)
        happy_days = sorted(happy_days.items(), key=lambda x: datetime.strptime(
    x[0], '%A, %B %d %Y'))
        happy_days = dict(happy_days)

        return self.show_bd(happy_days)

    def show_bd(self, happy_days):
        if len(happy_days) == 0:
            return f"There are no birthdays for the next {self.date_range} days."
        result = list()
        for day, names in happy_days.items():
            weekday_and_names = str()
            weekday_and_names += day + ": "
            for name in names:
                weekday_and_names += name + ", " if name != names[-1] else name
            result.append(weekday_and_names)
        return "\n".join(result)
    
    def search(self, search_line):
        if len(search_line) < 2:
            return "Please enter more than two characters."
        
        result = ""
        names_set = set()
        bg_yellow = "\033[43m"
        bg_end = "\033[0m"
        border = "\n"+"*"*10+"\n"
        search_line = search_line.lower()

        for record in self.data.values():
            if record.name.value.lower().find(search_line) != -1:
                names_set.add(record.name.value)
            if record.email and record.email.value.lower().find(search_line) != -1:
                names_set.add(record.name.value)
            if record.address and record.address.value.lower().find(search_line) != -1:
                names_set.add(record.name.value)
            if record.birthday and record.birthday.value.lower().find(search_line) != -1:
                names_set.add(record.name.value)
            for phone in record.phones:
                if phone.value.find(search_line) != -1:
                    names_set.add(record.name.value)
                    break

        def color_text(text):
            matches = re.finditer(search_line, text, flags=re.IGNORECASE)
            start = 0
            color_text = ''
            for i in matches:
                i_start = i.start()
                i_end = i.end()
                color_text += text[start:i_start]
                color_text += bg_yellow + text[i_start:i_end] + bg_end
                start = i_end
            return color_text + text[start:]
        
        for name in names_set:
            record = self.find(name)
            result += border + 'Contact name: ' + color_text(record.name.value)
            if len(record.phones):
                result += f"\nphones: {'; '.join(color_text(p.value) for p in record.phones)}"
            if record.email:
                result += f"\nemail: {color_text(record.email.value)}"
            if record.address:
                result += f"\naddress: {color_text(record.address.value)}"
            if record.birthday:
                result += f"\nbirthday: {color_text(record.birthday.value)}"
            result += border
            
        if result == "":
            return f'No search results for the line "{search_line}"'
        return result


class SaveManager:
    path = os.path.realpath(os.path.dirname(__file__))
    filename = f'{path}/db.pkl'
    
    @staticmethod
    def save_to_file(data):
        with open(SaveManager.filename, "wb") as fh:
            pickle.dump(data, fh)

    @staticmethod
    def read_from_file():
        try:
            with open(SaveManager.filename, "rb") as fh:
                return pickle.load(fh)
        except (EOFError, FileNotFoundError):
            pass
