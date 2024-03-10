
from Address_book import *


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Please enter a valid key"
        except IndexError:
            return "Your index is out of range"

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args



@input_error
def add_username_phone(args, book):
    name, phone = args
    while True:
        if len(phone) == 10:
            Rec=Record(name)
            Rec.add_phone(phone)
            book.add_record(Rec)
            print(book)
            return "Contact added."
        else:
            phone = input("Please enter a valid phone: ")
    


@input_error
def change_username_phone(args, book):
    name, old_phone, new_phone = args
    rec=book.find_record(name)  
    rec.edit_phone(old_phone, new_phone)
    print(rec)
    print(book)
    
    return "Contact's phone changed."

    #while True:
        #if name in book and len(new_phone) == 10:
            #book[name] = new_phone
            #print(book)
            #return "Contact's phone changed."
        #elif name in book and len(new_phone) != 10:
            #new_phone = input("Please enter a valid phone: ")
        #else:
            #raise KeyError

@input_error
def phone_username(args, book):
    name = args[0]    
    return book[name]

@input_error
def show_birthday(name, book):
    for contact in book:
        if contact.key() == name:
            birthday = contact['birthday']
            print(book)
            return f'{name}: {birthday}'
        

@input_error
def add_birthday(args, book):
    name, new_birthday = args
    Rec = book.find_record(name)
    print(Rec)
    Rec.add_birthday(new_birthday)    
    print(Rec)
    return "Birthday added"

@input_error
def print_all(book):
    for item in book:
        Rec=book.find_record(item)
        print(Rec)
    return "Contacts printed"


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_username_phone(args, book))
        elif command == "change":
            print(change_username_phone(args, book))
        elif command == "phone":
            print(phone_username(args, book))
        elif command == "all":
            print(print_all(book))
        elif command == "add_birthday":
            print(add_birthday(args, book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()