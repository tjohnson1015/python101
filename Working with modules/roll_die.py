import random 

def roll_dies():
    sides = int(input('Enter number of sides for die: '))
    print('You rolled a', random.randint(1, sides))

