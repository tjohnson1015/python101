## ALMOST COMPLETE ###

# from random import choice


# from ast import Name

phone_book = {}


while True:
    user_input = int(input(f'''
Electronic Phone Book
=====================
1. Set an entry
2. Look up an entry
3. Delete and entry
4. List all entries
5. Quit

What would you like to do? (1-5)? '''))

    if user_input == 1:
        new_name = input('What is the name of new entry? ')
        new_number = input('What is the number of the new entry? ')
        phone_book[new_name] = new_number
        # new_contact = {'Name': new_name, 'Number': new_number}
        # phone_book.append(new_contact)
    elif user_input == 2:
        contact_look = input("Who's number are you looking for? ")
        for contact in phone_book:
            if contact_look in phone_book:
                print("Their phone number is: ", phone_book[contact_look])
            else:
                print("Couldn't find that number.")
            # else:
            #     print('Sorry thats not a contact you have.')
    elif user_input == 3:
        contact_del = input("Who's number would you like to delete? ")
        if contact_del in phone_book:
            del phone_book[contact_del]
            print('Contact has been removed.')
        else:
            print("Contact Deleted")
    elif user_input == 4:
        print(phone_book)
    elif user_input == 5:
        print('Leaving Phonebook')
        quit()



