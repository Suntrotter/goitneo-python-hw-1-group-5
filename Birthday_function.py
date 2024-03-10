from datetime import datetime
#import datetime

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
             

#users = [{"name": "Bill Gates", "birthday": datetime(1955, 3, 13)},
#         {"name": "Bill Dates", "birthday": datetime(1975, 3, 21)}]
users = [{'name': 'Mary', 'birthday': datetime.datetime(2011, 2, 13, 0, 0)}, {'name': 'John', 'birthday': datetime.datetime(2011, 3, 11, 0, 0)}]
get_birthdays_per_week(users)



