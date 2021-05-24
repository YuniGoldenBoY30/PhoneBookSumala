class PhoneBookModel:
    @staticmethod
    def add_pair(phone_book):
        name = input('Contact name: ')
        normal_phone = input('Phone number: ')
        if PhoneBookModel.validate_data(normal_phone):
            phone_book.append({'name': name.lower().strip(), 'phone': normal_phone, 'call': 0})
            print("Contact added successfully !!")
        else:
            return "Error to added contact, phone number not valid"

        question = input('Do you want call it? s/n: ')
        if question.strip().lower().startswith('s'):
            PhoneBookModel.make_call(name.lower().strip(), phone_book)

    @staticmethod
    def delete_pair(name, phone_book):
        for contact in phone_book:
            if name.strip().lower() == contact.get('name'):
                phone_book.remove(contact)
                return print(f'{name} was deleted successfully!')
        else:
            return print("Record not found !")

    @staticmethod
    def select_phone(name, phone_book):
        for contact in phone_book:
            if name.strip().lower() == contact.get('name'):
                return contact

    @staticmethod
    def show_all_sorted(phone_book):
        if len(phone_book) != 0:
            list_sorted = sorted(phone_book, key=lambda p: (p['name']))
            return list_sorted
        else:
            return 0

    @staticmethod
    def validate_data(normal_phone):
        flag = False
        if normal_phone.startswith('+359'):
            dg1 = normal_phone.__getitem__(4)
            dg2 = normal_phone.__getitem__(5)
            operator = dg1 + dg2
            if operator in ['87', '88', '89']:
                digit = int(normal_phone.__getitem__(6))
                if digit >= 2 or digit <= 9:
                    flag = True
            return flag
        if normal_phone.startswith('00359'):
            dg1 = normal_phone.__getitem__(5)
            dg2 = normal_phone.__getitem__(6)
            operator = dg1 + dg2
            if operator in ['87', '88', '89']:
                digit = int(normal_phone.__getitem__(7))
                if digit >= 2 or digit <= 9:
                    flag = True
            return flag
        if normal_phone.startswith('0'):
            dg1 = normal_phone.__getitem__(1)
            dg2 = normal_phone.__getitem__(2)
            operator = dg1 + dg2
            if operator in ['87', '88', '89']:
                digit = int(normal_phone.__getitem__(3))
                if digit >= 2 or digit <= 9:
                    flag = True
            return flag

    @staticmethod
    def make_call(name, phone_book):
        flag = False
        for contact in phone_book:
            if name.strip().lower() == contact.get('name'):
                flag = True
                print(f"Calling {contact['name']}")
                print(f"{contact['phone']}")
                contact['call'] = contact['call'] + 1
                while True:
                    op = input('Press a key to call out: ')
                    if len(op) != 0:
                        print('Sorry, no responding, try later')
                        break
        if not flag:
            print('Sorry check the name and try again')

    @staticmethod
    def records_call(phone_book):
        return sorted(phone_book, key=lambda p: (p['call'], p['name']), reverse=True)
