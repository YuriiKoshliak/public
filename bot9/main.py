CONTACTS = {}


def hello():
    return 'How can I help you?'


def add_contact(name_and_number):
    name_and_number = name_and_number.split(' ')
    if name_and_number[0] not in CONTACTS:
        CONTACTS[name_and_number[0]] = name_and_number[1]
        return f"Contact {name_and_number[0]} saved with phone number {name_and_number[1]}!"
    else:
        return f'Contact {name_and_number[0]} is already exist in your phone book, you can change it. Just write "change {name_and_number[0]} *new number*"'

def change_contact(name_and_number):
    name_and_number = name_and_number.split(' ')
    if name_and_number[0] in CONTACTS:
        CONTACTS[name_and_number[0]] = name_and_number[1]
        return f"Contact {name_and_number[0]} saved with phone number {name_and_number[1]}!"
    else:
        return f'Contact {name_and_number[0]} is not in your phone book' 


def show_number(name):
    return CONTACTS[name]


def show_all(contacts):
    for name, number in contacts.items():
        yield f'{name}: {number}'


def close():
    return "Good bye!"


def input_error(func):
    def inner():
        cycle = True
        while cycle:
            try:
                result = func()
                cycle = False
            except IndexError:
                print('Enter the name and phone number, please.')
            except ValueError:
                print('Please, try again.')
            except KeyError:
                print("Enter the name from contacts and I'll show you phone")
        return result
    return inner


@input_error
def main():
    running = True
    while running:
        command = input('Enter the command: ').lower()
        if command == 'hello':
            print(hello())
        elif command.startswith("add "):
            print(add_contact(command.removeprefix('add ')))
        elif command.startswith("change "):
            print(change_contact(command.removeprefix('change ')))
        elif command.startswith("phone "):
            print(show_number(command.removeprefix("phone ")))
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


if __name__ == '__main__':
    main()
