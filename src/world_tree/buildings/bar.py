import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from world_tree.base_classes import Location, Object



# Creating the Bar Building node directly under the world node
bar_building = Location("Bar Building")

# Furniture and objects directly under Bar Building
table = Object("Table", status="Clean", parent=bar_building)
chair = Object("Chair", status="Available", parent=table)

bar_counter = Object("Bar Counter", status="Wiped", parent=bar_building)
register = Object("Register", status="Functional", parent=bar_counter)
bar_stool = Object("Bar Stool", status="Available", parent=bar_counter)

# Drink Menu
drink_menu = Object("Drink Menu", status="Not in use, [description of menu items] Drinks: Beer, Wine, Whiskey, Vodka, Rum, Tequila, Gin | Cocktails: Margarita, Mojito, Martini, Old Fashioned, Daiquiri, Manhattan", parent=bar_building)
beer = Object("Beer", status="Chilled", parent=drink_menu)
wine = Object("Wine", status="Chilled", parent=drink_menu)
whiskey = Object("Whiskey", status="Room Temperature", parent=drink_menu)
vodka = Object("Vodka", status="Chilled", parent=drink_menu)
rum = Object("Rum", status="Room Temperature", parent=drink_menu)
tequila = Object("Tequila", status="Chilled", parent=drink_menu)
gin = Object("Gin", status="Chilled", parent=drink_menu)

cocktails = Object("Cocktails", status="Ready to Mix", parent=drink_menu)
margarita = Object("Margarita", status="Not Prepared", parent=cocktails)
mojito = Object("Mojito", status="Not Prepared", parent=cocktails)
martini = Object("Martini", status="Not Prepared", parent=cocktails)
old_fashioned = Object("Old Fashioned", status="Not Prepared", parent=cocktails)
daiquiri = Object("Daiquiri", status="Not Prepared", parent=cocktails)
manhattan = Object("Manhattan", status="Not Prepared", parent=cocktails)

# Snacks Menu
snacks_menu = Object("Snacks Menu", status="Not in use, [description of snacks] Peanuts, Chips, Pretzels, Popcorn, Nachos, Buffalo Wings, Onion Rings", parent=bar_building)
peanuts = Object("Peanuts", status="Fresh", parent=snacks_menu)
chips = Object("Chips", status="Fresh", parent=snacks_menu)
pretzels = Object("Pretzels", status="Fresh", parent=snacks_menu)
popcorn = Object("Popcorn", status="Fresh", parent=snacks_menu)
nachos = Object("Nachos", status="Fresh", parent=snacks_menu)
buffalo_wings = Object("Buffalo Wings", status="Fresh", parent=snacks_menu)
onion_rings = Object("Onion Rings", status="Fresh", parent=snacks_menu)

