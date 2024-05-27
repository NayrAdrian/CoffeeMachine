MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}

machine_money = 0
money = 0
machine_on = True


def check_money(number_of_quarters, number_of_dimes, number_of_nickles, number_of_pennies):
    """"Calculates the total coins inserted and assigns it to 'money'"""
    global money
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01

    money = ((quarter * number_of_quarters) + (dime * number_of_dimes) + (nickel * number_of_nickles) +
             (penny * number_of_pennies))
    return money


def report(resource_dict, units_dict, cash):
    """Prints the remaining ingredients as well as the total money the machine collected"""
    for key, value in resource_dict.items():
        unit = units_dict.get(key, "")
        print(f"{key.capitalize()}: {value}{unit}")
    print(f"Money: ${cash}")


def turn_off():
    """Close the program, changes the machine_on to False"""
    global machine_on
    machine_on = False


def can_buy(order_type):
    """"Checks the total money inserted by the customer to if enough to buy"""
    global money
    global machine_money
    required_money = MENU[order_type]["cost"]
    if money >= required_money:
        change = money - required_money
        machine_money += required_money
        print(f"Here is your change ${change}.")
        print(f"Here is your {order_type} ☕ Enjoy!")
        return True
    else:
        print("Sorry, not enough money. Money refunded")
        return False


def can_make_order(order_type):
    # Check if the order type exists in the MENU
    if order_type not in MENU:
        return False, "Order type not found."

    # Get the ingredients required for the order
    required_ingredients = MENU[order_type]["ingredients"]

    # Check if there are enough resources for each ingredient using if-else statements
    for ingredient, required_amount in required_ingredients.items():
        if resources[ingredient] < required_amount:
            return False, f"Sorry there is not enough {ingredient}."

    # If all ingredients are sufficient, return True
    return True, ""


def main():
    global money
    order_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order_type in ["espresso", "latte", "cappuccino", "report", "off"]:
        if order_type == "report":
            report(resources, units, machine_money)
        elif order_type == "off":
            turn_off()
        else:
            can_make, message = can_make_order(order_type)  # Checks if ingredients are sufficient
            if can_make:
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickels = int(input("How many nickels? "))
                pennies = int(input("How many pennies? "))
                money = check_money(quarters, dimes, nickels, pennies)
                if can_buy(order_type):
                    for ingredient, amount in MENU[order_type]["ingredients"].items():
                        resources[ingredient] -= amount
            else:
                print(message)
    else:
        print("Invalid selection. Please choose from espresso, latte, cappuccino, report, or off.")


while machine_on is True:
    if __name__ == "__main__":
        main()
