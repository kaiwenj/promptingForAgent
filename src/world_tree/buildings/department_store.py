import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from world_tree.base_classes import Location, Object


# Creating the Department Store node directly under the world node
department_store = Location("Department Store")

# Sections in the department store
clothing_section = Location("Clothing Section", parent=department_store)
electronics_section = Location("Electronics Section", parent=department_store)
home_goods_section = Location("Home Goods Section", parent=department_store)
personal_care_section = Location("Personal Care Section", parent=department_store)

# Items in Clothing Section
men_clothing = Location("Men's Clothing", parent=clothing_section)
shirts = Object("Shirts", status="Available", parent=men_clothing)
pants = Object("Pants", status="Available", parent=men_clothing)
suits = Object("Suits", status="Available", parent=men_clothing)

women_clothing = Location("Women's Clothing", parent=clothing_section)
dresses = Object("Dresses", status="Available", parent=women_clothing)
blouses = Object("Blouses", status="Available", parent=women_clothing)
skirts = Object("Skirts", status="Available", parent=women_clothing)

kids_clothing = Location("Kids' Clothing", parent=clothing_section)
t_shirts = Object("T-Shirts", status="Available", parent=kids_clothing)
shorts = Object("Shorts", status="Available", parent=kids_clothing)
jackets = Object("Jackets", status="Available", parent=kids_clothing)

# Items in Electronics Section
computers = Location("Computers", parent=electronics_section)
laptops = Object("Laptops", status="Available", parent=computers)
desktops = Object("Desktops", status="Available", parent=computers)
tablets = Object("Tablets", status="Available", parent=computers)

home_entertainment = Location("Home Entertainment", parent=electronics_section)
televisions = Object("Televisions", status="Available", parent=home_entertainment)
sound_systems = Object("Sound Systems", status="Available", parent=home_entertainment)
streaming_devices = Object("Streaming Devices", status="Available", parent=home_entertainment)

appliances = Location("Appliances", parent=electronics_section)
refrigerators = Object("Refrigerators", status="Available", parent=appliances)
microwaves = Object("Microwaves", status="Available", parent=appliances)
washers = Object("Washers", status="Available", parent=appliances)

# Items in Home Goods Section
furniture = Location("Furniture", parent=home_goods_section)
sofas = Object("Sofas", status="Available", parent=furniture)
beds = Object("Beds", status="Available", parent=furniture)
dining_tables = Object("Dining Tables", status="Available", parent=furniture)

kitchenware = Location("Kitchenware", parent=home_goods_section)
cookware = Object("Cookware", status="Available", parent=kitchenware)
cutlery = Object("Cutlery", status="Available", parent=kitchenware)
dinnerware = Object("Dinnerware", status="Available", parent=kitchenware)

decor = Location("Decor", parent=home_goods_section)
rugs = Object("Rugs", status="Available", parent=decor)
lamps = Object("Lamps", status="Available", parent=decor)
wall_art = Object("Wall Art", status="Available", parent=decor)

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

