import beverages
import random

class CoffeeMachine:
    def __init__(self):
        self.count = 1

    def __str__(self):
        return f"Machine {self.count}"
    
    class EmptyCup(beverages.HotBeverage):
        price = 0.0
        name = "empty cup"

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This machine has to be repaired.")

    def repair(self):
        self.count = 1

    def serve(self, beverage):
        if self.count > 10:
            raise self.BrokenMachineException()
        self.count += 1
        return random.choice([beverage, self.EmptyCup()])

if __name__ == "__main__":
    hot_beverages = [beverages.Coffee(), beverages.Tea(), beverages.Chocolate(), beverages.Cappuccino()]
    machine = CoffeeMachine()
    for i in range(10):
        print(f"{i + 1} : {machine.serve(random.choice(hot_beverages))}")
    
    print("\nShould be broken:")
    print(machine.serve(beverages.Coffee()))
    print("It's working!") # Normaly never reached

    machine.repair()
    machine.serve(beverages.Coffee())