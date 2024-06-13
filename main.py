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
        self.total_sandwiches_sold = 0
        self.total_revenue = 0.0

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                return False, item
        return True, None

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert your money -> ")
        total = int(input("How many dollars? ")) * 1.00
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
                print(f"Here is ${change:.2f} in change. ")
            self.total_revenue += cost
            return True
        else:
            print("Sorry, that is not enough money.  Your money has been returned. ")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        self.total_sandwiches_sold += 1
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    def print_report(self):
        """Prints current resources on hand as well as the current revenue"""
        print(f"Sandwiches sold: {self.total_sandwiches_sold}")
        print(f"Total revenue: ${self.total_revenue:.2f}")
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} ounce(s)")
        for item, amount in self.machine_resources.items():
            if amount <= 2:
                print(f"Warning: {item} is running low!")

    def reset_revenue(self):
        self.total_revenue = 0.0
        print("Total revenue has been reset to $0.00")


def main():
    sandwich_machine = SandwichMachine(resources)
    machine_on = True

    for item, amount in sandwich_machine.machine_resources.items():
        if amount <= 2:
            print(f"Warning: {item} is running low!")

    while machine_on:
        choice = input("What would you like? (small/medium/large/off/report): ").strip().lower()
        if choice == "off":
            sandwich_machine.reset_revenue()
            machine_on = False
        elif choice == "report":
            sandwich_machine.print_report()
        elif choice in ["small", "medium", "large"]:
            sandwich_size = choice
            order = recipes[sandwich_size]
            can_make, missing_item = sandwich_machine.check_resources(order["ingredients"])
            if can_make:
                print(f"The cost is ${order['cost']:.2f}.")
                payment = sandwich_machine.process_coins()
                if sandwich_machine.transaction_result(payment, order['cost']):
                    sandwich_machine.make_sandwich(sandwich_size, order["ingredients"])
            else:
                print(f"Sorry, there is not enough {missing_item}.")
                another_choice = input("Would you like something else (yes/no): ").strip().lower()
                if another_choice == "no":
                    print("Transaction Canceled.  Returning to the main menu")
        else:
            print("Invalid choice.  Please select again.")


if __name__ == "__main__":
    main()
