#6. contact book
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'Phone': phone, 'Email': email}
        print(f'Contact {name} added successfully.')

    def display_contacts(self):
        print('Contacts:')
        for name, info in self.contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}, Phone: {self.contacts[name]['Phone']}, Email: {self.contacts[name]['Email']}")
        else:
            print(f'Contact {name} not found.')

# Example usage:
contact_book = ContactBook()

contact_book.add_contact('John Doe', '123-456-7890', 'john.doe@email.com')
contact_book.add_contact('Jane Smith', '987-654-3210', 'jane.smith@email.com')

contact_book.display_contacts()

contact_book.search_contact('John Doe')
contact_book.search_contact('Alice Johnson')
