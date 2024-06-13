# Data #

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  # slice
            "ham": 4,  # slice
            "cheese": 4,  # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  # slice
            "ham": 6,  # slice
            "cheese": 8,  # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  # slice
            "ham": 8,  # slice
            "cheese": 12,  # ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  # slice
    "ham": 18,  # slice
    "cheese": 24,  # ounces
}


# Complete functions #

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                return False, item
        return True, None

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        total = int(input("How many large dollars? ")) * 1.00
        total += int(input("How many half dollars? ")) * 0.50
        total += int(input("How many quarters? ")) * 0.25
        total += int(input("How many nickels? ")) * 0.05
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change. ")
            return True
        else:
            print("Sorry, that is not enough money.  Money refunded. ")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"Here is your {sandwich_size} sandwich. Bon appetit!")

# Make an instance of SandwichMachine class and write the rest of the codes #
def main():
    sandwich_machine = SandwichMachine(resources)
    machine_on = True

    while machine_on:
        choice = input("What would you like? (small/medium/large/off/report): ").strip().lower()
        if choice == "off":
            machine_on = False
        elif choice == "report":
            print(f"Bread: {sandwich_machine.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_machine.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_machine.machine_resources['cheese']} ounce(s)")
        elif choice in ["small", "medium", "large"]:
            sandwich_size = choice
            order = recipes[sandwich_size]
            can_make, missing_item = sandwich_machine.check_resources(order["ingredients"])
        if can_make:
            print("The cost is ${order['cost']}.")
            payment = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(payment, order["cost"]):
                sandwich_machine.make_sandwich(sandwich_size, order["ingredients"])
        else:
            print(f"Sorry, there is not engouh {missing_item}.")
    else:
        print("Invalid choice.  Please select again.")


if __name__ == "__main__":
    main()