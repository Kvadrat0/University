contacts = {}

name = input('Введите имя контакта: ')
phone_number = input('Введите телефонный номер контакта: ')
contacts[name] = phone_number
name = input('Введите имя контакта: ')
phone_number = input('Введите телефонный номер контакта: ')
contacts[name] = phone_number
for contact, phone in contacts.items():
    print(contact, phone)
