from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        if len(phone) == 10:
            super().__init__(phone)
        else:
            print("Please enter a valid phone: ")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def edit_phone(self, new_phone):
        for phone in self.phones:
            if phone.value == new_phone:
                phone = new_phone
                return self.phones

    def remove_phone(self, phone):
        for phone in self.phones:
            if phone.value == phone:
                self.phones.remove(phone)
                return self.phones

    def find_phone(self, phone):
        for phone in self.phones:
            if phone.value == phone:
                return f"{name}: {phone}"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def handle_add(name, phone, book):
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return book

    def add_record(self, record):
        self.data.update(record)
        return self.data

    def find_record(self, name):
        for record in self.data:
            if record.name.value == name:
                return record
        return "Not Found"

    def delete_record(self, name):
        for record in self.data:
            if record.name.value == name:
                self.data.remove(record)
            else:
                return "Unable to delete"


def main():
    book = AddressBook()
    name = input("Please enter a name: ")
    phone = input("Please enter a phone: ")
    AddressBook.handle_add(name, phone, book)


if __name__ == '__main__':
    main()
