import sys

states = {
    "Oregon": "OR",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO"
}

capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

def get_state_by_capital(capital):
    for state_code, cap in capital_cities.items():
        if cap.lower() == capital.lower():
            for state, code in states.items():
                if code == state_code:
                    return state
    return None

def get_capital_by_state(state):
    for state_name, state_code in states.items():
        if state_name.lower() == state.lower():
            return capital_cities[state_code]
    return None

def all_in(arg):
    if not arg:
        return
    
    elements = [x.strip() for x in arg.split(",")]
    
    for element in elements:
        if not element:  # Skip empty elements
            continue
            
        capital = get_capital_by_state(element)
        if capital:
            print(f"{capital} is the capital of {element.title()}")
            continue
            
        state = get_state_by_capital(element)
        if state:
            print(f"{element.title()} is the capital of {state}")
            continue
            
        print(f"{element} is neither a capital city nor a state")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        all_in(sys.argv[1])
