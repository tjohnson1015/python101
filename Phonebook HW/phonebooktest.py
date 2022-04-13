
def print_menu():
    choice = print(int(input(f'''
Electronic Phone Book
=====================
1. Set an entry
2. Look up an entry
3. Delete and entry
4. List all entries
5. Quit

What would you like to do? (1-5)? ''')))

phone_book = {
    'Name: ': '', 
    'Phone Number: ': '',
}

print_menu()

while print_menu != 5:
    if print_menu == 1:
        add_name = input('Name of contact: ')
        add_phone = input('Phone number of contact: ')
        phone_book['Name'] = add_name
        phone_book['Phone Number: '] = add_phone
