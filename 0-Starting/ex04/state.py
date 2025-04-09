import sys

states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
}

capital_cities = {
    "AL": "Montgomery",
    "OR": "Salem",
    "CO": "Denver",
    "NJ": "Trenton"
}

def state(capital):
    if capital in capital_cities.values():
        combined_dict = {
            capital_cities[state_abbr]: state_name
                for state_name, state_abbr in states.items()
                    if state_abbr in capital_cities
        }
        print(combined_dict[capital])
    else:
        print("Unknown capital city")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        state(sys.argv[1])

