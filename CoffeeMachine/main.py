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
money = 0
is_on = True


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def get_coins():
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies


def check_payment(drink, pay):
    if pay < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


def check_resources(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    if "milk" in MENU[drink]["ingredients"] and resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False
    if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True


def buy_coffee(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    if "milk" in MENU[drink]["ingredients"]:
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]


def get_change(drink, pay):
    return pay - MENU[drink]["cost"]


while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print_report()
    else:
        # Check coins is enough
        payment = get_coins()
        enough_payment = check_payment(user_input, payment)
        if not enough_payment:
            continue
        # Check resources
        enough_resources = check_resources(user_input)

        # Print success
        # Update resources + money
        if enough_resources:
            buy_coffee(user_input)
            money += MENU[user_input]["cost"]
            print(f"Here is ${get_change(user_input, payment)} in change.")
            print(f"Here is your {user_input}. Enjoy!")

