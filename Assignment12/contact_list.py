contacts = {}  # Dictionary to store contacts and their phone numbers

def add_contact(name,new_phone_number):
    contacts[name] =new_phone_number
    print("Contact added successfully!")

def edit_contact(name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        print("Contact edited successfully!")
    else:
        print("Contact not found!")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def display_contacts():
    if len(contacts) == 0:
        print("No contacts found!")
    else:
        print("Contact List:")
        for name, phone_number in contacts.items():
            print(f"{name}: {phone_number}")

while True:
    print("Contact List Program")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        add_contact(name, phone_number)
    elif choice == '2':
        name = input("Enter the name: ")
        new_phone_number = input("Enter the new phone number: ")
        edit_contact(name, new_phone_number)
    elif choice == '3':
        name = input("Enter the name: ")
        delete_contact(name)
    elif choice == '4':
        display_contacts()
    elif choice == '5':
        print("Thank you for using the Contact List program")
        break
