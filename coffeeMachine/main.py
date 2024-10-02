from data import MENU
from data import resources
import random
report = {
    "Water": random.randint(250, 350),
    "Milk": random.randint(150, 250),
    "Coffee": random.randint(75, 125),
    "Money": 0,
}
coffee_cost = {
    "espresso": {"Water": 50, "Milk": 0, "Coffee": 18, "Money": 1.50},
    "latte": {"Water": 200, "Milk": 150, "Coffee": 24, "Money": 2.50},
    "cappuccino": {"Water": 250, "Milk": 100, "Coffee": 24, "Money": 3.0},
}

currency = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}


def check_resources(coffee_cost, report):
    """check if there is enough resources to make coffee"""
    all_okay = True
    if coffee_cost["Water"] > report["Water"]:
        print("Sorry there is not enough water.")
        all_okay = False
    elif coffee_cost["Milk"] > report["Milk"]:
        print("Sorry there is not enough milk.")
        all_okay = False
    elif coffee_cost["Coffee"] > report["Coffee"]:
        print("Sorry there is not enough coffee.")
        all_okay = False
    return all_okay


def reduce_resources(coffee_cost, report):
    """after brewing coffee, the resources available is reduced by cost of the coffee"""
    water = report["Water"] - coffee_cost["Water"]
    milk = report["Milk"] - coffee_cost["Milk"]
    coffee = report["Coffee"] - coffee_cost["Coffee"]
    money = report["Money"] + coffee_cost["Money"]
    resources_after_reduction = {
        "Water": water,
        "Milk": milk,
        "Coffee": coffee,
        "Money": money,
    }
    return resources_after_reduction


def money_total(payment_dictionary, currency):
    """calculating the amount of money given to the coffee machine"""
    total_quarters = payment_dictionary["quarters"] * currency["quarters"]
    total_dimes = payment_dictionary["dimes"] * currency["dimes"]
    total_nickles = payment_dictionary["nickels"] * currency["nickels"]
    total_pennies = payment_dictionary["pennies"] * currency["pennies"]
    total = total_quarters + total_dimes + total_nickles + total_pennies
    return total


def print_payment():
    """prints the input statements asking for payment and saves it in a dictionary"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickels = int(input("How many nickels?:"))
    pennies = int(input("How many pennies?:"))
    payment_dictionary = {
        "quarters": quarters,
        "dimes": dimes,
        "nickels": nickels,
        "pennies": pennies,
    }
    return payment_dictionary


while True:
    # prompt user by asking "What would you like?"
    coffee_choice = input("What would you like? (espresso/latte/cappuccino):")
    # turn off the coffee machine
    if coffee_choice.lower() == "off":
        break
    # print report showing available resources
    elif coffee_choice.lower() == "report":
        print(f"Water: {report["Water"]} ml")
        print(f"Milk: {report["Milk"]} ml")
        print(f"Coffee: {report["Coffee"]} g")
        print(f"Money: ${report["Money"]}")

    elif coffee_choice.lower() == "espresso" and check_resources(coffee_cost["espresso"], report):
        payment_dictionary = print_payment() # get dictionary with amount paid with different coins
        customer_money_available = money_total(payment_dictionary, currency) #calculate total money paid

        # if the calculated total is bigger that the cost of the coffee, the coffee is served, change is calculated
        # and printed and the resources used on brewing the coffee is taken from the total amount of resources
        if customer_money_available >= coffee_cost["espresso"]["Money"]:
            resources_after_reduction = reduce_resources(coffee_cost["espresso"], report)
            report = resources_after_reduction
            money_back = customer_money_available - coffee_cost["espresso"]["Money"]
            print(f"Your change: ${money_back}")
            print("Here is your espresso")
        else:
            print("Sorry, it is not enough money.")

    elif coffee_choice.lower() == "latte" and check_resources(coffee_cost["latte"], report):
        payment_dictionary = print_payment()
        customer_money_available = money_total(payment_dictionary, currency)

        if customer_money_available >= coffee_cost["latte"]["Money"]:
            resources_after_reduction = reduce_resources(coffee_cost["latte"], report)
            report = resources_after_reduction
            money_back = customer_money_available - coffee_cost["latte"]["Money"]
            print(f"Your change: {money_back}")
            print("Here is your latte")
        else:
            print("Sorry, it is not enough money.")


    elif coffee_choice.lower() == "cappuccino" and check_resources(coffee_cost["cappuccino"], report):
        payment_dictionary = print_payment()
        customer_money_available = money_total(payment_dictionary, currency)

        if customer_money_available >= coffee_cost["cappuccino"]["Money"]:
            resources_after_reduction = reduce_resources(coffee_cost["cappuccino"], report)
            report = resources_after_reduction
            money_back = customer_money_available - coffee_cost["cappuccino"]["Money"]
            print(f"Your change: {money_back}")
            print("Here is your cappuccino")
        else:
            print("Sorry, it is not enough money.")










