import data

resources = {
    "water": 600,
    "milk": 400,
    "coffee": 200,
}

coins = {
    "quarters": .25,
    "dimes": .10,
    "nickles": .05,
    "pennies": .01
}

MENU = data.MENU


def check_ingredients(coffe_selected):
    is_good = True
    for ingredient in coffe_selected["ingredients"]:
        if coffe_selected["ingredients"][ingredient] >= resources[ingredient]:
            is_good = False
            print(f"Sorry there is not enough {ingredient}.")
        else:
            resources[ingredient] -= coffe_selected["ingredients"][ingredient]
    return is_good


def calculate_coins(user_coins):
    # print(cost)
    # print(user_coins)
    amount = 0
    for key, value in coins.items():
        amount += (value * (1 * int(user_coins[key])))
    return amount


def process_coins():
    # user insert coins
    print("Please insert coins.")
    user_coins = {
        "quarters": (input("how many quarters?: ")),
        "dimes": input("how many dimes?: "),
        "nickles": input("how many nickles?: "),
        "pennies": input("how many pennies?: ")
    }
    return user_coins


def calculate_purchase(user_total_coins, coffee_selected):
    result = {
        "change": 0,
        "message": "fail",
        "profit": 0
    }
    # calculate change
    if user_total_coins > coffee_selected["cost"]:
        result["change"] = user_total_coins - coffee_selected["cost"]
        result["message"] = "success"
        result["profit"] = coffee_selected["cost"]
        return result
    return result


def game():
    # Welcome
    profit = 0

    print("Welcome! Choice your coffee")
    while True:
        coffee_selected = input("What would you like? (espresso/latte/cappuccino): ")
        # coffee purchase logic
        if coffee_selected in MENU:
            coffee_selected_name = coffee_selected
            coffee_selected = MENU[coffee_selected]
            good_in_ingredients = check_ingredients(coffee_selected)
            if not good_in_ingredients:
                continue

            # insert coins
            user_coins = process_coins()

            # calculate coins
            user_total_coins = calculate_coins(user_coins)

            # calculate purchase
            result = calculate_purchase(user_total_coins, coffee_selected)
            if result["message"] == "success":
                change = result["change"]
                profit += result["profit"]

                print(f"Here is ${change} in change")
                print(f"Here is your {coffee_selected_name} *&*. Enjoy!")

        elif coffee_selected == "off":
            break
        elif coffee_selected == "report":
            print(f'Water: {resources["water"]}ml')
            print(f'milk: {resources["water"]}ml')
            print(f'coffee: {resources["water"]}g')
            print(f"Profit: ${profit}")

        else:
            print("Sorry invalid option, please try again")
            continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game()
