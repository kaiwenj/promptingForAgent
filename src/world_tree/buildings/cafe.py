import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from world_tree.base_classes import Location, Object



# Creating the Cafe Building node directly under the world node
cafe_building = Location("Cafe Building")

# Furniture and objects directly under Cafe Building
table = Object("Table", status="Clean", parent=cafe_building)
chair = Object("Chair", status="Available", parent=table)

register = Object("Register", status="Functional", parent=cafe_building)

coffee_making_bar = Object("Coffee Making Bar", status="Ready", parent=cafe_building)
coffee_maker = Object("Coffee Maker", status="Off", parent=coffee_making_bar)

# Cafe Menu
cafe_menu = Object("Cafe Menu", status="Not in use, [description of menu items] Coffee: Espresso, Cafe Cubano, Americano, Latte, Cappuccino, Macchiato, Mocha, Flat White, Cortado, Ristretto, Lungo, Affogato, Red Eye, Black Eye, Doppio, Cafe au Lait, Irish Coffee, Turkish Coffee, Cold Brew, Nitro Coffee, Iced Coffee, Frappe, Vienna Coffee, Breve, Drip Coffee", parent=cafe_building)
espresso = Object("Espresso", status="Available", parent=cafe_menu)
cafe_cubano = Object("Café Cubano", status="Available", parent=cafe_menu)
americano = Object("Americano", status="Available", parent=cafe_menu)
latte = Object("Latte", status="Available", parent=cafe_menu)
cappuccino = Object("Cappuccino", status="Available", parent=cafe_menu)
macchiato = Object("Macchiato", status="Available", parent=cafe_menu)
mocha = Object("Mocha", status="Available", parent=cafe_menu)
flat_white = Object("Flat White", status="Available", parent=cafe_menu)
cortado = Object("Cortado", status="Available", parent=cafe_menu)
ristretto = Object("Ristretto", status="Available", parent=cafe_menu)
lungo = Object("Lungo", status="Available", parent=cafe_menu)
affogato = Object("Affogato", status="Available", parent=cafe_menu)
red_eye = Object("Red Eye", status="Available", parent=cafe_menu)
black_eye = Object("Black Eye", status="Available", parent=cafe_menu)
doppio = Object("Doppio", status="Available", parent=cafe_menu)
cafe_au_lait = Object("Café au Lait", status="Available", parent=cafe_menu)
irish_coffee = Object("Irish Coffee", status="Available", parent=cafe_menu)
turkish_coffee = Object("Turkish Coffee", status="Available", parent=cafe_menu)
cold_brew = Object("Cold Brew", status="Available", parent=cafe_menu)
nitro_coffee = Object("Nitro Coffee", status="Available", parent=cafe_menu)
iced_coffee = Object("Iced Coffee", status="Available", parent=cafe_menu)
frappe = Object("Frappe", status="Available", parent=cafe_menu)
vienna_coffee = Object("Vienna Coffee", status="Available", parent=cafe_menu)
breve = Object("Breve", status="Available", parent=cafe_menu)
drip_coffee = Object("Drip Coffee", status="Available", parent=cafe_menu)

# Baked Goods Menu
baked_goods_menu = Object("Baked Goods Menu", status="Not in use, [description of baked goods] Chocolate Chip Cookies, Oatmeal Raisin Cookies, Sugar Cookies, Gingerbread Cookies, Croissant, Danish, Pain au Chocolat, Baguette, Blueberry Muffins, Banana Muffins, Chocolate Muffins, Vanilla Cupcakes, Red Velvet Cupcakes, Apple Pie, Pumpkin Pie, Glazed Doughnuts", parent=cafe_building)
chocolate_chip_cookies = Object("Chocolate Chip Cookies", status="Fresh", parent=baked_goods_menu)
oatmeal_raisin_cookies = Object("Oatmeal Raisin Cookies", status="Fresh", parent=baked_goods_menu)
sugar_cookies = Object("Sugar Cookies", status="Fresh", parent=baked_goods_menu)
gingerbread_cookies = Object("Gingerbread Cookies", status="Fresh", parent=baked_goods_menu)
croissant = Object("Croissant", status="Fresh", parent=baked_goods_menu)
danish = Object("Danish", status="Fresh", parent=baked_goods_menu)
pain_au_chocolat = Object("Pain au Chocolat", status="Fresh", parent=baked_goods_menu)
baguette = Object("Baguette", status="Fresh", parent=baked_goods_menu)
blueberry_muffins = Object("Blueberry Muffins", status="Fresh", parent=baked_goods_menu)
banana_muffins = Object("Banana Muffins", status="Fresh", parent=baked_goods_menu)
chocolate_muffins = Object("Chocolate Muffins", status="Fresh", parent=baked_goods_menu)
vanilla_cupcakes = Object("Vanilla Cupcakes", status="Fresh", parent=baked_goods_menu)
red_velvet_cupcakes = Object("Red Velvet Cupcakes", status="Fresh", parent=baked_goods_menu)
apple_pie = Object("Apple Pie", status="Fresh", parent=baked_goods_menu)
pumpkin_pie = Object("Pumpkin Pie", status="Fresh", parent=baked_goods_menu)
glazed_doughnuts = Object("Glazed Doughnuts", status="Fresh", parent=baked_goods_menu)

