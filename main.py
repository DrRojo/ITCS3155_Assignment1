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

original_resources = {
    "bread": 100,  # slice
    "ham": 100,  # slice
    "cheese": 100,  # ounces
}

resources = original_resources.copy()

# Complete functions #

class SandwichMachine:

    def __init__(self, machine_resources, original_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources
        self.original_resources = original_resources
        self.total_sandwiches_sold = 0
        self.total_revenue = 0.0
        self.resupply_count = 0
        self.ingredient_usage = {key: 0 for key in machine_resources.keys()}
        self.transaction_history = []
        self.revenue_breakdown = {"small": 0.0, "medium": 0.0, "large": 0.0}
        self.customer_orders = {i: [] for i in range(1, 11)}  # Customer orders for customers 1 through 10

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
        total = float(input("How much money are you inserting? "))
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

    def make_sandwich(self, sandwich_size, order_ingredients, customer_id):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
            self.ingredient_usage[item] += order_ingredients[item]
        self.total_sandwiches_sold += 1
        self.revenue_breakdown[sandwich_size] += recipes[sandwich_size]["cost"]
        self.transaction_history.append((sandwich_size, recipes[sandwich_size]["cost"]))
        self.customer_orders[customer_id].append((sandwich_size, recipes[sandwich_size]["cost"]))
        print(f"Your {sandwich_size} sandwich is ready. Bon appetit!")

    def print_report(self):
        """Prints current resources on hand as well as the current revenue"""
        print(f"Sandwiches sold: {self.total_sandwiches_sold}")
        print(f"Total revenue: ${self.total_revenue:.2f}")
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} ounce(s)")
        print(f"Number of resupplies: {self.resupply_count}")
        print(f"Revenue breakdown: {self.revenue_breakdown}")
        print(f"Ingredient usage: {self.ingredient_usage}")
        if self.total_sandwiches_sold > 0:
            average_revenue = self.total_revenue / self.total_sandwiches_sold
            print(f"Average revenue per sandwich: ${average_revenue:.2f}")
        else:
            print("No sandwiches sold yet.")
        for item, amount in self.machine_resources.items():
            if amount <= 2:
                print(f"Warning: {item} is running low!")
        print("\nCustomer Order Breakdown:")
        for customer_id, orders in self.customer_orders.items():
            if orders:
                print(f"Customer {customer_id}:")
                for order in orders:
                    print(f"  {order[0]} sandwich, ${order[1]:.2f}")

    def reset_revenue(self):
        self.total_revenue = 0.0
        print("Total revenue has been reset to $0.00")

    def resupply_resources(self):
        """Resupply all resources to their original amounts and subtract $1 from total revenue"""
        self.machine_resources = self.original_resources.copy()
        self.total_revenue -= 1
        self.resupply_count += 1
        print(f"Resources have been resupplied to their original amounts. ")
        print(f"$1 admin fee has been deducted from total revenue.")

    def print_transaction_history(self):
        """Prints the transaction history"""
        for i, transaction in enumerate(self.transaction_history, 1):
            print(f"Transaction {i}: {transaction[0]} sandwich, ${transaction[1]:.2f}")

    def print_average_revenue_per_sandwich(self):
        """Prints the average revenue per sandwich sold"""
        if self.total_sandwiches_sold > 0:
            average_revenue = self.total_revenue / self.total_sandwiches_sold
            print(f"Average revenue per sandwich: ${average_revenue:.2f}")
        else:
            print("No sandwiches sold yet.")

def main():
    sandwich_machine = SandwichMachine(resources, original_resources)
    machine_on = True

    for item, amount in sandwich_machine.machine_resources.items():
        if amount <= 2:
            print(f"Warning: {item} is running low!")

    while machine_on:
        print(f"Welcome to Good Burger, home of the good burger!")
        customer_id = int(input("May I have your customer number (1-10): "))
        if customer_id not in range(1, 11):
            print("Invalid customer number. Please enter a number between 1 and 10.")
            continue

        order_complete = False
        total_cost = 0
        customer_order = []

        while not order_complete:
            choice = input("What would you like? (small/medium/large/complete): ").strip().lower()
            if choice in ["small", "medium", "large"]:
                sandwich_size = choice
                order = recipes[sandwich_size]
                can_make, missing_item = sandwich_machine.check_resources(order["ingredients"])
                if can_make:
                    total_cost += order["cost"]
                    customer_order.append((sandwich_size, order["ingredients"]))
                else:
                    print(f"Sorry, there is not enough {missing_item}.")
            elif choice == "complete":
                order_complete = True
            else:
                print("Invalid choice. Please select again.")

        if customer_order:
            print(f"The total cost is ${total_cost:.2f}.")
            payment = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(payment, total_cost):
                for sandwich_size, ingredients in customer_order:
                    sandwich_machine.make_sandwich(sandwich_size, ingredients, customer_id)

        next_action = input("What would you like to do next? (off/report/resupply/history/average/continue): ").strip().lower()
        if next_action == "off":
            sandwich_machine.reset_revenue()
            machine_on = False
        elif next_action == "report":
            sandwich_machine.print_report()
        elif next_action == "resupply":
            sandwich_machine.resupply_resources()
        elif next_action == "history":
            sandwich_machine.print_transaction_history()
        elif next_action == "average":
            sandwich_machine.print_average_revenue_per_sandwich()
        elif next_action == "continue":
            continue
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
