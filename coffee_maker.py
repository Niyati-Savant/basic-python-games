# Data
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
money = 0.0


# Functions
def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money: Rs {money}")


def sufficient_resources(wr, mr, cr):
    wa = resources['water']
    ma = resources['milk']
    ca = resources['coffee']
    if wa < wr:
        return "Sorry there is not enough water"
    elif ma < mr:
        return "Sorry there is not enough milk"
    elif ca < cr:
        return "Sorry there is not enough coffee"
    else:
        return "All set"


def make_coffee(wr, mr, cr):
    resources['water'] -= wr
    resources['milk'] -= mr
    resources['coffee'] -= cr


# Code

machine_status = True

logo = """
 ____  ____  ____  ____  ____  ____     __  __   ____   __  __  ____ _____ 
/ (__`/ () \| ===|| ===|| ===|| ===|   |  \/  | / () \ |  |/  /| ===|| () )
\____)\____/|__|  |__|  |____||____|   |_|\/|_|/__/\__\|__|\__\|____||_|\_\
"""

print(logo)

while machine_status:
    print("We serve latte,cappuccino,espresso")
    coffee_type = input("What would you like to order?").lower()
    if coffee_type == 'report':
        print_resources()
    elif coffee_type == 'off':
        machine_status = False
    else:
        water_req = MENU[coffee_type]['ingredients']['water']
        milk_req = MENU[coffee_type]['ingredients']['milk']
        coffee_req = MENU[coffee_type]['ingredients']['coffee']
        money_req = MENU[coffee_type]['cost']
        response = sufficient_resources(water_req, milk_req, coffee_req)
        if response == 'All set':
            print(f"It will cost you {money_req} .Insert coins")
            quarters = int(input("How many quarters?"))
            dimes = int(input("How many dimes?"))
            nickles = int(input("How many nickles?"))
            pennies = int(input("How many pennies?"))
            user_inserted = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            print(f"You have inserted {user_inserted}")
            if user_inserted < money_req:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money += money_req
                if user_inserted > money_req:
                    change_amt = round(user_inserted - money_req,2)
                    print(f"Here is ${change_amt} dollars in change.")

                # updating resources
                make_coffee(water_req, milk_req, coffee_req)
                print(f"Here is your {coffee_type}.Enjoy!!")
        else:
            print(response)
