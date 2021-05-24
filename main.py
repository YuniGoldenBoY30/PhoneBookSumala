from Models import PhoneBookModel

phone_book = []
try:
    file = open('Models/phonebook.txt', 'r')
    data_file = file.read()
    file.close()
    list_phone = data_file.split('\n')
    for contact in list_phone:
        if len(contact.split(' ')) != 1:
            normal_phone = contact.split(' ')[1]
            if PhoneBookModel.validate_data(normal_phone):
                phone_book.append({'name': contact.split(' ')[0].lower().strip(), 'phone': normal_phone, 'call': 0})
except Exception as exc:
    print("Please, find the file 'phonebook.txt' \n Exit application ...")

if phone_book.__len__() != 0:
    print('Choose one option')
    while True:
        print('1- Add a new pair')
        print('2- Delete a pair by name')
        print('3- Get a phone by name')
        print('4- Get all records sorted')
        print('5- Make call')
        print('6- Record calls')
        print('7- Exit')
        print('-----------------------')
        try:
            option = int(input())
            if option == 1:
                phone_new = PhoneBookModel.add_pair(phone_book)
                print(phone_new)

            elif option == 2:
                name = input('Insert the name of the contact to delete: ')
                question = input(f"Are you sure, that do you want deleted '{name}'? S/N ")
                if question.strip().lower().startswith('s'):
                    PhoneBookModel.delete_pair(name=name, phone_book=phone_book)
                else:
                    print('Contact saved !')
            elif option == 3:
                name = input('Insert the name of the contact to show: ')
                record = PhoneBookModel.select_phone(phone_book=phone_book, name=name)
                print(f"Name: {name.upper()} Phone: {record['phone']}")
            elif option == 4:
                records = PhoneBookModel.show_all_sorted(phone_book)
                print('-------- Phone Book ---------')
                print(f"|id| name       | phone number |")
                print('-----------------------------')
                if records != 0:
                    c = 1
                    for contact in records:
                        print(f"|{c} | {contact['name']}  | {contact['phone']}|")
                        c += 1
                    question = input('Do you want to make a call? s/n ')
                    if question.strip().lower().startswith('s'):
                        name = input('Please, enter the name: ')
                        PhoneBookModel.make_call(name=name, phone_book=phone_book)
                else:
                    print('No record to show')
                print('------------------------------')
            elif option == 5:
                name = input('Enter the contact: ')
                PhoneBookModel.make_call(name.strip().lower(), phone_book)
            elif option == 6:
                record_sort = PhoneBookModel.records_call(phone_book)
                print('--------Recently------------')
                if all(record['call'] == 0 for record in record_sort):
                    print("Empty call records")

                for record in record_sort:
                    if record['call'] != 0:
                        print(f"{record['name']}")
                        print(f"{record['phone']} ({record['call']})")
                        print('_____________________________')
            elif option < 1 or option > 6:
                print('Exiting...')
                break
        except ValueError:
            print('You must be enter a valid option')
