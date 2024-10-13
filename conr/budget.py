import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_total_cost(quantity, price_per_item):
    """
    قم بتمرير متغيرين اثنين للوظيفة:
    1- الكمية
    2- سعر القطعة 
    ستقوم الوظيفة بإرجاع حاصل ضرب الاثنين معا
    """
    return quantity * price_per_item

while True: 
    clear_terminal()  
    budget = float(input("Enter your spending budget: "))
    item_name = input("Enter the item you want to buy: ")
    quantity = int(input(f"How many {item_name}s do you want to buy? "))
    price_per_item = float(input(f"Enter the price per {item_name}: "))
    total_cost = calculate_total_cost(quantity, price_per_item)

    if total_cost > budget :
        print("Warning: Your purchase exceeds your daily budget!")
    else:
        print("Purchase successful! Enjoy your new item.")
    
    if input('Do you want to continue? (y/n) ') != 'y':
        break
    
