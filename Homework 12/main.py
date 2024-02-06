from folder import AddressBook, Record, Birthday, Phone, Name
from ast import literal_eval
import pickle


# Створюємо записник
CONTACTS = AddressBook()
FILE_NAME = 'data.bin'

# Зберігаємо записник
def save_contacts():
    try:
        with open (FILE_NAME, "wb") as file:
            pickle.dump(CONTACTS.data, file)
    except IOError as E:
        print(E)

def load_contacts():
    try:
        with open (FILE_NAME, "rb") as file:
            CONTACTS.data = pickle.load(file)
        print("Data was loaded from save")
    except IOError as E:
        print(E)

# Декоратор для відстежування помилок під час введення.
def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except (IndexError, ValueError, KeyError, SyntaxError) as E:
            return E
    return inner

# Привітання
def hello():
    return ("You can use 'add', 'change', 'set' 'show me', 'show all', 'find', 'exit'")

# Додаємо новий контакт до записника
@input_error
def add_contact(name_and_number):
    name_and_number = name_and_number.split(' ')
    if len(name_and_number) == 2:
        name = name_and_number[0]
        number = name_and_number[1]
        if name not in CONTACTS:
            record = Record(name)
            record.add_phone(number)
            CONTACTS.add_record(record)
            return f"Contact {name} saved with phone number {number}"
        else:
            CONTACTS[name].add_phone(number)
            return f'Contact {name} is already exist in your phone book, new phone number {number} was added'
        
    else:
        return 'Enter the name and phone number, please.'

# Змінюємо номер телефону контакта
@input_error
def change_contact(name_and_number):
    name_and_number = name_and_number.split(' ')
    if len (name_and_number) != 3:
        return 'Enter the name, old phone number and new phone number, please.'
    name = name_and_number[0]
    old_number = name_and_number[1]
    new_number = name_and_number[2]
    record = CONTACTS.data.get(name)
    if not record:
        return f'Contact {name} is not in your phone book'
    for phone in record.phones:
        if phone.value == old_number:
            phone.value = new_number
            return f"Contact {name} saved with new phone number {new_number}, old number {old_number} was deleted!"
    return f'Can’t find that number: {old_number}'

# Вказуємо дату народження
@input_error
def set_bithday(name_and_birthday):
    name_and_birthday = name_and_birthday.split(' ')
    if len (name_and_birthday) != 2:
        return 'Enter the name and the date of birthday, please. Example: set Bob 1990,1,5'
    name = name_and_birthday[0]
    birthday = literal_eval(name_and_birthday[1])
    record = CONTACTS.data.get(name)
    if not record:
        return f'Contact {name} is not in your phone book'
    record.add_birthday(birthday)
    return f'Congratulations, contact {name} has a new date of birthday {birthday}'



# Показуємо контакт
@input_error
def show_number(name):
    if name in CONTACTS.keys():
        return CONTACTS[name]
    else:
        return "Can't find that name"

# Показуємо всю книгу
@input_error
def show_all(contacts):
    for name, number in contacts.items():
        yield f'{name}: {number}'

# Пошук по записнику
@input_error
def find(something):
    result = []
    for name, record in CONTACTS.items():
        if something in name and record not in result:
            result.append(record)
        else:
            for phone in record.phones:
                if something in phone.value and record not in result:
                    result.append(record)
    if not result:
        result.append("No matches, try to find something else")
    return result


def close():
    return "Good bye!"


def main():
    running = True
    load_contacts()
    while running:
        command = input('Enter the command: ').lower()
        if command == 'hello':
            print(hello())
        elif command.startswith("add "):
            print(add_contact(command.removeprefix('add ')))
        elif command.startswith("set "):
            print(set_bithday(command.removeprefix('set ')))
        elif command.startswith("change "):
            print(change_contact(command.removeprefix('change ')))
        elif command.startswith("show me "):
            print(show_number(command.removeprefix("show me ")))
        elif command.startswith("find "):
            for item in (find(command.removeprefix("find "))):
                print (item)
        elif command == "show all":
            if CONTACTS:
                for contact in show_all(CONTACTS):
                    print(contact)
            else:
                print('Your phone book is empty.')
        elif command in ("good bye", "close", "exit"):
            print(close())            
            running = False
        else:
            print("Enter correct command, please.")
        save_contacts()


if __name__ == '__main__':
    main()
