from datetime import datetime as dt
from Address_book import *
import re


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
            return "Contact added."
        else:
            phone = input("Please enter a valid phone: ")
    


@input_error
def change_username_phone(args, book):
    name, old_phone, new_phone = args
    if len(str(old_phone)) == 10 and len(str(new_phone)) == 10:        
        rec=book.find_record(name)  
        rec.edit_phone(old_phone, new_phone)
        return "Contact's phone changed."
    elif len(str(old_phone)) != 10 and len(str(new_phone)) != 10: 
        print("Invalid data")
    else:
        raise KeyError
    
  
@input_error
def phone_username(args, book):
    name = args[0]
    Rec = book.find_record(name)
    if Rec:
        return f'{name}: {Rec.phones}'
    else:
        return "Invalid name"

@input_error
def show_birthday(args, book):
    name = args[0]
    Rec = book.find_record(name)
    if Rec:
        return f'{name}: {Rec.birthday.birthday}'
    else:
        return "Invalid name"

    
@input_error
def add_birthday(args, book):
    name, new_birthday = args
    pattern_str = r'^\d{2}/\d{2}/\d{4}$'
    if re.match(pattern_str, new_birthday): 
        Rec = book.find_record(name)
        if Rec:    
            Rec.add_birthday(new_birthday) 
            return "Birthday added"          
        else:
            return "Invalid name"
    else:
        return "Invalid birthday date"
    

@input_error
def print_all(book):
    for item in book:
        Rec=book.find_record(item)
        print(Rec)
    return "Contacts printed"


@input_error
def birthdays(book):
    users = []
    for item in book:
        Rec=book.find_record(item)
        it={}
        it['name']=str(Rec.name)
        tempstr=str(Rec.birthday.birthday)              
        a = dt(int(tempstr[:4]),int(tempstr[5:7]),int(tempstr[8:10]))
        it['birthday'] = a
        users.append(it)        
    AddressBook.get_birthdays_per_week(users)    
    return "Birthdays printed"



def main():
    book = AddressBook()
    #
    #Rec=Record("Mary")
    #Rec.add_phone("1234567890")
    #Rec.add_birthday("13/02/2011")
    #book.add_record(Rec)
    #Rec=Record("John")
    #Rec.add_phone("0987654321")
    #Rec.add_birthday("11/03/2011")
    #book.add_record(Rec)
    #
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
        elif command == "show_birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()