
#IM ALMOST POSITIVE THERE IS BETTER WAY TO DO THIS BUT IT DOES WORK. ONE THING ID LIKE TO TOUCH ON IS FIGURING
# OUT A WAY TO ROUND THE TOTAL TO 2 DECIMAL POfloatS ONLY. Sometimes it prints 1, sometimes 2, and sometimes 3+

# def percentage_plus(total, tip):
#     return total * (tip / 100) + total

def percentage_plus(total, tip):
    return total * tip / 100 + total

def tip_calculator():
    total = float(input("What is the bill total? "))
    tip = float(input("What percentage would you like to tip? ")) 
    print("The bill total with tip is " + str(percentage_plus(total, tip)))


def group_tip_calculator():
    total = float(input("What is the bill total? $"))
    tip = float(input("What percentage would you like to tip? "))
    people = float(input("How many people are in your group? "))
    print("The bill total with tip is $" + str(percentage_plus(total, tip)))
    print("Each person should pay $" + str(percentage_plus(total, tip)/people))

group_tip_calculator()