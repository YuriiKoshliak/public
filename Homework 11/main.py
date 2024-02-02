from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    def _validator(self, value):
        ...

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._validator(new_value)
        self._value = new_value


    def __str__(self):
        return str(self._value)

class Name(Field):
    ...

class Phone(Field):
    def _validator(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Invalid phone number")
        super()._validator(value)
        
class Birthday(Field):

    def _validator(self, value):
        if not isinstance(value, tuple) or len(value) != 3 or not all(isinstance(x, int) for x in value):
            raise ValueError("Invalid date format. It's must be a tuple of three integers")
        super()._validator(value)
    # def __init__(self, value):
    #     if value:
    #         self.value = value
    #     else:
    #         return None

    def date_object(self):
        year = self.value[0]
        month = self.value[1]
        day = self.value[2]
        return datetime(year, month, day)

class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.birthday = Birthday(birthday) if birthday else None
        self.phones = []

    def days_to_birthday(self):
        if self.birthday:
            birth = self.birthday.date_object()
            today = datetime.today()
            day_of_birth = datetime(today.year, birth.month, birth.day)
            if day_of_birth < today:
                day_of_birth = day_of_birth.replace(year = today.year + 1)
            days_until_birthday = (day_of_birth - today).days
            return days_until_birthday
        else:
            ...

    def add_phone(self, phone):
        self.phone = Phone(phone)
        self.phones.append(self.phone)

    def remove_phone(self, phone):
        if phone in [p.value for p in self.phones]:
            for p in self.phones:
                if p.value == phone:
                    self.phones.remove(p)
                    break
        else:
            raise ValueError

    def edit_phone(self, old_phone, new_phone):
        if str(old_phone) not in [p.value for p in self.phones]:
            raise ValueError
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break
        
    def find_phone(self, phone):
        phone = str(phone)
        if phone in [p.value for p in self.phones]:
            return Phone(phone)
        else:
            return None
         
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value}"

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
        
    def iterator(self, n):
        if isinstance(n, int) and n > 0:
            keys = list(self.data.keys())
            for i in range(0, len(keys), n):
                yield [self.data[key] for key in keys[i:i+n]]


