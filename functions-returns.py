def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
    return a / b

# def cakeulator(number_of_guest, pancakes_per_guest):
    # return (math.ceil(number_of_guest * pancakes_per_guest * 1.12))

try: 
    number_of_guests = int(input("How many guests? "))
    pancakes_per_guest = int(input("How many pancakes per guest "))
except:
    print("need and actual number dawg")
    exit()

total = multiply(number_of_guests, pancakes_per_guest)

print(total)

