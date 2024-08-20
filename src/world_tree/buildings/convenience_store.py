import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from world_tree.base_classes import Location, Object

# Creating the Convenience Store node directly under the world node
convenience_store = Location("Convenience Store")

# Sections in the convenience store
snacks_section = Location("Snacks Section", parent=convenience_store)
beverages_section = Location("Beverages Section", parent=convenience_store)
household_items_section = Location("Household Items Section", parent=convenience_store)
personal_care_section = Location("Personal Care Section", parent=convenience_store)

# Items in Snacks Section
chips = Location("Chips", parent=snacks_section)
potato_chips = Object("Potato Chips", status="Available", parent=chips)
corn_chips = Object("Corn Chips", status="Available", parent=chips)
pretzels = Object("Pretzels", status="Available", parent=chips)

candy = Location("Candy", parent=snacks_section)
chocolate = Object("Chocolate", status="Available", parent=candy)
gummies = Object("Gummies", status="Available", parent=candy)
hard_candy = Object("Hard Candy", status="Available", parent=candy)

# Items in Beverages Section
soft_drinks = Location("Soft Drinks", parent=beverages_section)
cola = Object("Cola", status="Available", parent=soft_drinks)
lemonade = Object("Lemonade", status="Available", parent=soft_drinks)
orange_soda = Object("Orange Soda", status="Available", parent=soft_drinks)

juices = Location("Juices", parent=beverages_section)
apple_juice = Object("Apple Juice", status="Available", parent=juices)
orange_juice = Object("Orange Juice", status="Available", parent=juices)
grape_juice = Object("Grape Juice", status="Available", parent=juices)

water = Location("Water", parent=beverages_section)
still_water = Object("Still Water", status="Available", parent=water)
sparkling_water = Object("Sparkling Water", status="Available", parent=water)

# Items in Household Items Section
cleaning_supplies = Location("Cleaning Supplies", parent=household_items_section)
detergent = Object("Detergent", status="Available", parent=cleaning_supplies)
bleach = Object("Bleach", status="Available", parent=cleaning_supplies)
disinfectant_wipes = Object("Disinfectant Wipes", status="Available", parent=cleaning_supplies)

paper_products = Location("Paper Products", parent=household_items_section)
toilet_paper = Object("Toilet Paper", status="Available", parent=paper_products)
paper_towels = Object("Paper Towels", status="Available", parent=paper_products)
napkins = Object("Napkins", status="Available", parent=paper_products)

# Items in Personal Care Section
skincare = Location("Skincare", parent=personal_care_section)
moisturizer = Object("Moisturizer", status="Available", parent=skincare)
sunscreen = Object("Sunscreen", status="Available", parent=skincare)
cleanser = Object("Cleanser", status="Available", parent=skincare)

haircare = Location("Haircare", parent=personal_care_section)
shampoo = Object("Shampoo", status="Available", parent=haircare)
conditioner = Object("Conditioner", status="Available", parent=haircare)
hair_oil = Object("Hair Oil", status="Available", parent=haircare)

oral_care = Location("Oral Care", parent=personal_care_section)
toothpaste = Object("Toothpaste", status="Available", parent=oral_care)
mouthwash = Object("Mouthwash", status="Available", parent=oral_care)
toothbrush = Object("Toothbrush", status="Available", parent=oral_care)

