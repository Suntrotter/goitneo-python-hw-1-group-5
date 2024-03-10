from collections import UserDict
import datetime
from datetime import datetime


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


class Birthday(Field):
    def __init__(self, birthday):
        self.birthday = birthday


class Record:
    def __init__(self, name, birthday=10/10/1970):
        self.name = Name(name)
        self.birthday = Birthday(birthday)
        self.phones = []


    def add_birthday(self, birthday):
        try:
            birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y")   
            self.birthday = birthday 
        except:
            print("Incorrect date!") 

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
        string = f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}, birthday: {self.birthday.birthday}"
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
    

    def get_birthdays_per_week(users):
        today = datetime.today().date()
        birthdays = {}
        
        for user in users:
            name = user["name"]
            birthday = user["birthday"].date()  
            birthday_this_year = birthday.replace(year=today.year)
            
            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)
                
            delta_days = (birthday_this_year - today).days
            
            if delta_days < 7:
                day_of_the_week = birthday_this_year.strftime('%A')
                
                if day_of_the_week != "Sunday" and day_of_the_week != "Saturday":
                    if day_of_the_week in birthdays:
                        birthdays.setdefault(day_of_the_week).extend([name])
                    else:
                        birthdays[day_of_the_week] = [name]
                        
                else:
                    if "Monday" in birthdays:
                        birthdays.setdefault("Monday").extend([name])
                    else:
                        birthdays["Monday"] = [name]
                
        for key, value in birthdays.items():
            if len(value) > 1:
                value = ", ".join(str(element) for element in value)        
            print(f'{key}: {value}')
                
        return birthdays


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