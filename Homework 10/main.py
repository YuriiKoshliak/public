from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    ...


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phone = Phone(phone)
        self.phones.append(self.phone)

    def remove_phone(self, phone):
        if Phone(phone) in self.phones:
            self.phones.remove(Phone(phone))
        else:
            raise ValueError

    def edit_phone(self, old_phone, new_phone):
        if old_phone not in self.phones:
            raise ValueError
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break
        

    def find_phone(self, phone):
        if Phone(phone) in self.phones:
            return phone
        else:
            return None
         

    

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data.keys():
            return self.data[name]
        else:
            return None
        
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            return None  



