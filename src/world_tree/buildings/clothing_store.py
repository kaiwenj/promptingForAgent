import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from world_tree.base_classes import Location, Object


# Creating the Clothing Store node directly under the world node
clothing_store = Location("Clothing Store")

# Sections in the clothing store
mens_section = Location("Men's Section", parent=clothing_store)
womens_section = Location("Women's Section", parent=clothing_store)
childrens_section = Location("Children's Section", parent=clothing_store)

# Items in Men's Section
mens_tops = Location("Tops", parent=mens_section)
mens_shirt = Object("Shirt", status="Available", parent=mens_tops)
mens_tshirt = Object("T-Shirt", status="Available", parent=mens_tops)
mens_sweater = Object("Sweater", status="Available", parent=mens_tops)

mens_bottoms = Location("Bottoms", parent=mens_section)
mens_jeans = Object("Jeans", status="Available", parent=mens_bottoms)
mens_shorts = Object("Shorts", status="Available", parent=mens_bottoms)
mens_trousers = Object("Trousers", status="Available", parent=mens_bottoms)

mens_footwear = Location("Footwear", parent=mens_section)
mens_sneakers = Object("Sneakers", status="Available", parent=mens_footwear)
mens_boots = Object("Boots", status="Available", parent=mens_footwear)
mens_sandals = Object("Sandals", status="Available", parent=mens_footwear)

# Items in Women's Section
womens_tops = Location("Tops", parent=womens_section)
womens_blouse = Object("Blouse", status="Available", parent=womens_tops)
womens_tshirt = Object("T-Shirt", status="Available", parent=womens_tops)
womens_sweater = Object("Sweater", status="Available", parent=womens_tops)

womens_bottoms = Location("Bottoms", parent=womens_section)
womens_jeans = Object("Jeans", status="Available", parent=womens_bottoms)
womens_shorts = Object("Shorts", status="Available", parent=womens_bottoms)
womens_skirt = Object("Skirt", status="Available", parent=womens_bottoms)

womens_footwear = Location("Footwear", parent=womens_section)
womens_sneakers = Object("Sneakers", status="Available", parent=womens_footwear)
womens_boots = Object("Boots", status="Available", parent=womens_footwear)
womens_heels = Object("Heels", status="Available", parent=womens_footwear)

# Items in Children's Section
childrens_tops = Location("Tops", parent=childrens_section)
childrens_shirt = Object("Shirt", status="Available", parent=childrens_tops)
childrens_tshirt = Object("T-Shirt", status="Available", parent=childrens_tops)
childrens_sweater = Object("Sweater", status="Available", parent=childrens_tops)

childrens_bottoms = Location("Bottoms", parent=childrens_section)
childrens_jeans = Object("Jeans", status="Available", parent=childrens_bottoms)
childrens_shorts = Object("Shorts", status="Available", parent=childrens_bottoms)
childrens_trousers = Object("Trousers", status="Available", parent=childrens_bottoms)

childrens_footwear = Location("Footwear", parent=childrens_section)
childrens_sneakers = Object("Sneakers", status="Available", parent=childrens_footwear)
childrens_boots = Object("Boots", status="Available", parent=childrens_footwear)
childrens_sandals = Object("Sandals", status="Available", parent=childrens_footwear)

