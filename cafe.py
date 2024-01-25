"""
Refer to the Pseudocode File (Task_12_Pseudocode.txt) for comprehensive details on the program's functionality
Task 12.1 Data Structures - Lists and Dictionaries file (cafe.py)
"""
# Initialise variables: Menu List
cafe_menu = ["Omelette", "Bacon Roll", "Full English Breakfast", "Pancakes", "Waffles", "Coffee", "Tea", "Orange Juice"]
total_stock_value = 0                 # Total stock variable cumulative total value count

#Create dictionaries: Stock (Quantity of covers in stock) and Price (Per item in GBP)
stock_dictionary = {
    "Omelette": 200,
    "Bacon Roll": 100,
    "Full English Breakfast": 75,
    "Pancakes": 150,
    "Waffles": 150,
    "Coffee": 250,
    "Tea": 300,
    "Orange Juice": 50
}

price_dictionary = {
    "Omelette": 5,
    "Bacon Roll": 7.50,
    "Full English Breakfast": 12.50,
    "Pancakes": 10,
    "Waffles": 10,
    "Coffee": 2.50,
    "Tea": 1.50,
    "Orange Juice": 4.50
}

# Calculate stock value using for loop and print this value
for items in cafe_menu:
    item_value = (stock_dictionary[items] * price_dictionary[items])                        # Calculating the stock value for each item on the menu
    total_stock_value += item_value                                                         # Add item_value to total_stock_value cumulative variable
print("Total stock value for items on the menu today: £{:.2f}".format(total_stock_value))   # Print total stock value formatted in GBP

# Additional menu information
print(f"\nMenu item covers in stock today:\n")
for i, s in stock_dictionary.items():
    print(f"{i} = {s}")                                 # Print out the menu items stock list
print(f"\nMenu item price per portion:\n")
for i, p in price_dictionary.items():
    print(f"{i}", "= £{:.2f}".format(p))                # Print out the menu items per item cost

# Program ends