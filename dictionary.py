# # EXERCISES

phonebook_dict = {
'Alice': '703-493-1834',
'Bob': '857-384-1234',
'Elizabeth': '484-584-2923'
}

print(phonebook_dict['Elizabeth'])

phonebook_dict['Kareem'] = '968-345-2345'

print(phonebook_dict)

# del phonebook_dict['Alice']

# # print(phonebook_dict)

# phonebook_dict['Bob'] = '968-345-2345'

# print(phonebook_dict)


# ramit = {
#     'name': 'Ramit',
#     'email': 'ramit@gmail.com',
#     'interests': ['movies', 'tennis'],
#     'friends': [
#         { 'name': 'Jasmine', 'email': 'jasmine@yahoo.com', 'interests': ['photography', 'tennis'] },
#         { 'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': ['movies', 'tv'] }
#     ]
# }

# # print(ramit['email'])
# # print(ramit['interests'][0])
# # print(ramit['friends'][0]['email'])
# # print(ramit['friends'][0]['interests'][1])


#LETTER HISTOGRAM

# word = input('Please enter a word: ')

# for letters in word:
#     if letters not in word:
#         word[letters] = 0
#     else:
#         word[letters] += 1

#WORKING LETTER HISTOGRAM

# word = input('Please enter a word: ')
# cnt = {}

# for letter in word:
#     if letter not in cnt:
#         cnt[letter] = 0
#     cnt[letter] += 1
        
# print(cnt)

# WORD HISTOGRAM



# sentence = input('Please enter a sentence: ').split()

# cnt = {}

# for word in sentence:
#     if word not in cnt:
#         cnt[word] = 0
#     cnt[word] +=1

# print(cnt)










