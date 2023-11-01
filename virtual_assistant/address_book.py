from collections import UserDict
from collections import defaultdict
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
        rez = "\n"+"*"*10+"\n"
        rez += f"Contact name: {self.name.value}\nphones: {'; '.join(p.value for p in self.phones)}"

        if self.email is not None:
            rez += f"\nemail: {self.email.value}"

        if self.address is not None:
            rez += f"\naddress: {self.address.value}"

        if self.birthday is not None:
            rez += f"\nbirthday: {self.birthday}"

        rez += "\n"+"*"*10
        return rez

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
        except Exception as e:
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
    def __init__(self):
        super().__init__()
        path = os.path.realpath(os.path.dirname(__file__))
        self.filename = f'{path}/db.pkl'
        self.read_from_file()

    def add_record(self, record):
        self.data[str(record.name)] = record
        self.save_to_file()

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]
        self.save_to_file()

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.data, file)

    def read_from_file(self):
        try:
            with open(self.filename, "rb") as file:
                self.data = pickle.load(file)
        except (EOFError, FileNotFoundError):
            self.data = {}

    def get_birthdays_per_week(self):
        happy_days = defaultdict(list)
        current_day = datetime.today().date()
        for name, record in self.data.items():
            if str(record.birthday) == "":
                continue
            user_Bday = datetime.strptime(str(record.birthday), '%d.%m.%Y')
            user_Bday = datetime.date(user_Bday)
            birthday_this_year = user_Bday.replace(year=current_day.year)

            if birthday_this_year < current_day:
                birthday_this_year = birthday_this_year.replace(
                    year=current_day.year+1)
            delta_days = (birthday_this_year - current_day).days

            if delta_days < 7:
                day_of_the_week = birthday_this_year.strftime("%A")
                current_week_day = current_day.strftime("%A")
                if day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
                    if (current_week_day == "Sunday" or current_week_day == "Monday") and birthday_this_year > current_day:
                        continue

                    happy_days["Monday"].append(name)
                    continue
                happy_days[day_of_the_week].append(name)

        return self.show_bd(happy_days)

    def show_bd(self, happy_days):
        if len(happy_days) == 0:
            return "There are no birthdays for the next 7 days."
        result = list()
        for day, names in happy_days.items():
            weekday_and_names = str()
            weekday_and_names += day + ": "
            for name in names:
                weekday_and_names += name + ", " if name != names[-1] else name
            result.append(weekday_and_names)
        return "\n".join(result)
