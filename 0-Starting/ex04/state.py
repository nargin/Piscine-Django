import sys

states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
}

capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

def state(capital):
    if capital in capital_cities:
        print(states[capital_cities[capital]])
    else:
        print("Unknown capital city")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        state(sys.argv[1])

