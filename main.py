from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    drink = input("What would you like? (espresso/latte/cappuccino/frappe): ").lower()
    if drink == "off":
        break
    elif drink == "report":
        coffee_maker.report()
    else:
        order = coffee_menu.find_drink(drink)
        if order not in coffee_menu.menu:
            print("That is not something on the menu. Please enter your order again.")
            continue

        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
                print(f"Here is your {drink}. Enjoy!")
