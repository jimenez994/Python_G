from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome!")
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print("Welcome to the coffee machine 3000")

while True:
    user_input = input(f"What would you like? ({my_menu.get_items()}): ")
    coffee_selected = my_menu.find_drink(user_input)
    if user_input == "off":
        break
    elif user_input == "report":
        my_coffee_maker.report()
        money_machine.report()
    elif coffee_selected is not None:
        if my_coffee_maker.is_resource_sufficient(coffee_selected):
            made_payment = money_machine.make_payment(coffee_selected.cost)
            if made_payment:
                my_coffee_maker.make_coffee(coffee_selected)
            else:
                continue
        else:
            print("Sorry some resources are insufficient to make your coffee at this time.")
    else:
        print("invalid input")
        continue
