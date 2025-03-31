from collections import UserDict

class Field:
    """
    Base class for record fields.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
  

class Name(Field):
    """
    Class for storing contact name. Required field.
    """
    pass


class Phone(Field):
    """
    Class for storing phone numbers. Has format validation (10 digits).
    """
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.value == other.value
        return False


class Record:
    """
    A class for storing contact information, including name and phone list.
    """
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number:str):
        """
        Add phones.
        """
        phone = Phone(phone_number)
        # Checking if such a number does not already exist
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            print(
                f"Phone {phone_number} already exists in "
                f"contact {self.name}."
            )

    def remove_phone(self, phone_number:str):
        """
        Delete phones.
        """
        phone = Phone(phone_number)
        if phone in self.phones:
            self.phones.remove(phone)
            print(
                f"Phone {phone_number} has been successfully removed "
                f"from contact {self.name}."
            )
        else:
            print(
                f"Phone {phone_number} has not been found " 
                f"in contact {self.name}."
            )

    def edit_phone(self, old_phone:str, new_phone:str):
        """
        Edit phones.
        """
        old_phone_obj = Phone(old_phone)
        new_phone_obj = Phone(new_phone)

        if old_phone_obj in self.phones:
            index = self.phones.index(old_phone_obj)
            self.phones[index] = new_phone_obj
            print(
                f"Phone {old_phone} has been successfully updated to "
                f"{new_phone} in contact {self.name}."
            )
        else:
            print(
                f"Phone {old_phone} has not been found "
                f"in contact {self.name}."
            )


    def find_phone(self, phone_number:str):
        """
        Search for a phone.
        """
        phone = Phone(phone_number)

        if phone in self.phones:
            return phone


class AddressBook(UserDict):
    """
    A class for storing and managing records
    """

    def add_record(self, record: Record):
        """
        Add records to self.data.
        """
        self.data[str(record.name)] = record
        print(f"Contact {record.name} has been added.")

    def find(self, name: str):
        """
        Search records by name.
        """
        record = self.data.get(name)
        if record:
            return record
        else:
            print(f"Contact {name} has not been found.")
            return None

    def delete(self, name: str):
        """
        Delete records by name.
        """
        if self.data.get(name) != None:
            del self.data[name]
            print(f"Contact {name} has been successfully deleted.")
        else:
            print(f"Contact {name} not found.")


# Usage.
if __name__ == "__main__":
    print("#Створення нової адресної книги")
    book = AddressBook()

    print("#Створення запису для John")
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    print("#Додавання запису John до адресної книги")
    book.add_record(john_record)

    print("#Створення та додавання нового запису для Jane")
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print("#Виведення всіх записів у книзі")
    for name, record in book.data.items():
        print(record)

    print("#Знаходження та редагування телефону для John")
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    print("#Пошук конкретного телефону у записі John")
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    print("#Пошук конкретного телефону у записі John")
    book.delete("Jane")