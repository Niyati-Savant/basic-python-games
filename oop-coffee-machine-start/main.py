from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_status = True

logo = """
 ____  ____  ____  ____  ____  ____     __  __   ____   __  __  ____ _____ 
/ (__`/ () \| ===|| ===|| ===|| ===|   |  \/  | / () \ |  |/  /| ===|| () )
\____)\____/|__|  |__|  |____||____|   |_|\/|_|/__/\__\|__|\__\|____||_|\_\
"""

print(logo)
coffee_maker = CoffeeMaker()
# menu_item = MenuItem()
menu = Menu()
money_machine = MoneyMachine()

while machine_status:
    options = menu.get_items()
    print(options)
    user_choice = input("What would you like to order?").lower()

    if user_choice == 'report':
        coffee_maker.report()
        money_machine.report()

    elif user_choice == 'off':
        machine_status = False
    else:
        coffee_type=menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(coffee_type):
            print(f"It will cost you {coffee_type.cost} .")
            if money_machine.make_payment(coffee_type.cost):
                coffee_maker.make_coffee(coffee_type)


