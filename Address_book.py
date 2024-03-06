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
            super().__init__(phone)
            print("Please enter a valid phone")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = ['0987654321', '1234567890']

    def add_phone(self, phone):
        self.phones.append(phone)
        return self.phones

    def edit_phone(self, phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i] == phone:
                self.phones[i] = new_phone
        return self.phones

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
            return self.phones

    def find_phone(self, phone):
        if phone in self.phones:
            string = f"{phone}"
            return string

    def __str__(self):
        string = f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"
        return string


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data.update({record.name.value: record})
        return self.data

    def find_record(self, name):
        for record in self.data:
            if name in record:
                return self.data[record]
        return "Not Found"

    def delete_record(self, name):

        for record in self.data:
            if name in record:
                del self.data[record]
                return self.data
        return "Unable to delete"


def handle_add(name, phone, book):
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    print(book)
    return book


def main():
    book = AddressBook()
    name = input("Please enter a name: ")
    phone = input("Please enter a phone: ")
    handle_add(name, phone, book)


if __name__ == '__main__':
    main()