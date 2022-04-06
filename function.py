def name (fname, lname):
    print("Top of the morning to you, " + fname + ' ' + lname + "!")

def email(fname, lname, domain):
    print(fname[0].lower() + '.' + lname.lower() + '@' + domain + '.com')

def user(fname, lname):
    print(fname[0:3].lower() + '_' + lname[0:5].lower())

def cac(fname, lname, domain):
    name(fname, lname)
    print("Email: ")
    email(fname, lname, domain)
    print("Username: ")
    user(fname, lname)






# email('Tyler', 'Johnson', 'Apple')


cac('Tyler', 'Johnson', 'StarkIndustries')

# user('tyler', 'johnson')
# user('john', 'smith')

# email("Tyler", "Johnson", "starkindustries")
# email('John', 'Smith', 'Apple')