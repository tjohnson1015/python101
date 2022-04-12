# answer = ""
# while answer != 'bye':
#     print('hello?')
#     answer = input('')

#COUNT TO X

# user_number = int(input('Enter and number: '))
# count = 1

# while count <= user_number:
#     print(count)
#     count += 1

#COUNT N TO M

# user_number_1 = int(input('Enter and number: '))
# user_number2 = int(input('Enter another number: '))
# count = user_number_1

# while count >= user_number_1 and count <= user_number2:
#     print(count)
#     count += 1

# #COUNT ODD N TO M

# user_number_1 = int(input('Enter and number: '))
# user_number2 = int(input('Enter another number: '))
# count = user_number_1

# while count >= user_number_1 and count <= user_number2:
#     if count % 2 != 0:
#         print(count)
#     count += 1

#FIZZBUZZ

# user_number = int(input('Enter a number: '))
# count = 1

# while count <= user_number:
#     if count % 3 == 0 and count % 5 == 0:
#         print('fizzbuzz')
#     elif count % 3 == 0:
#         print('fizz')
#     elif count % 5 == 0:
#         print('buzz')
#     else: 
#         print(count)
#     count += 1

#GRANDMA CLI


gma_response_1 = "SPEAK UP, SONNY!"
gma_response_2 = "NO, NOT SINCE 1938!"

while True:
    user_input = input('Say something to your grandma ')
    if user_input == "BYE":
        break
    elif user_input == user_input.upper():
        print(gma_response_2)
    else:
        print(gma_response_1)

print('Bye gson')


















