## Spiderman Hulk Thor
# def print_pokemon(poke):
#   print(f"""
#   Pokemon {poke["number"]}: {poke["name"]})
#   Type/s: {poke["types"]}
#   """)



# def print_avenger(avenge):
#     print(f"""
#     Avenger {avenge["number"]}: {avenge["alias"]}
#     Powers: {avenge["powers"]}
#     """)

def print_avenger(avenge):
    print(f"""
        Avenger: {avenge["alias"]}
        Real Name: {avenge["name"]}
        Number: {avenge["number"]}
        Powers: {avenge["powers"]}
    """)



avenger = [
    {
        "alias": "Spiderman",
        "name": "Peter Parker",
        "number": "001",
        "powers": ["Web crawler", "Super human strength"],
        "gender": "m",
        "blurb": "Bit by radioactive spider",
        "height": 17,
        "weight": 757,
    },
    {
        "alias": "Hulk",
        "name": "Bruce Banner",
        "number": "002",
        "powers": ["Super human strength", "Healing abilities"],
        "gender": "m",
        "blurb": "Exposed to gamma radiation",
        "height": 23,
        "weight": 5216,
    },
    {
        "alias": "Thor",
        "name": "Thor Odinson",
        "number": "003",
        "power": ["Super human strength", "Odin power"],
        "gender": "m",
        "blurb": "Asgardian, King of Asgard",
        "height": 118,
        "weight": 1293,
    },
    {
        "alias": "Black Widow",
        "name": "Natasha Romanoff",
        "number": "004",
        "power": ["Acrobatic", "Hand to hand combat"],
        "gender": "f",
        "blurb": "Super spy",
        "height": 17,
        "weight": 594,
    }
]

print_avenger(avenger[1])
