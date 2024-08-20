import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from world_tree.base_classes import Location, Object


# Creating the Gardening Store node directly under the world node
gardening_store = Location("Gardening Store")

# Sections in the gardening store
plants_section = Location("Plants Section", parent=gardening_store)
tools_section = Location("Gardening Tools Section", parent=gardening_store)
fertilizers_section = Location("Fertilizers Section", parent=gardening_store)

# Items in Plants Section
indoor_plants = Location("Indoor Plants", parent=plants_section)
fern = Object("Fern", status="Healthy", parent=indoor_plants)
succulent = Object("Succulent", status="Healthy", parent=indoor_plants)
snake_plant = Object("Snake Plant", status="Healthy", parent=indoor_plants)

outdoor_plants = Location("Outdoor Plants", parent=plants_section)
rose = Object("Rose", status="Blooming", parent=outdoor_plants)
lavender = Object("Lavender", status="Fragrant", parent=outdoor_plants)
tulip = Object("Tulip", status="Blooming", parent=outdoor_plants)

# Items in Gardening Tools Section
hand_tools = Location("Hand Tools", parent=tools_section)
trowel = Object("Trowel", status="New", parent=hand_tools)
hand_rake = Object("Hand Rake", status="New", parent=hand_tools)
pruning_shears = Object("Pruning Shears", status="Used", parent=hand_tools)

power_tools = Location("Power Tools", parent=tools_section)
lawn_mower = Object("Lawn Mower", status="Operational", parent=power_tools)
leaf_blower = Object("Leaf Blower", status="Operational", parent=power_tools)
hedge_trimmer = Object("Hedge Trimmer", status="Operational", parent=power_tools)

# Items in Fertilizers Section
organic_fertilizers = Location("Organic Fertilizers", parent=fertilizers_section)
compost = Object("Compost", status="Fresh", parent=organic_fertilizers)
manure = Object("Manure", status="Fresh", parent=organic_fertilizers)
bone_meal = Object("Bone Meal", status="Available", parent=organic_fertilizers)

chemical_fertilizers = Location("Chemical Fertilizers", parent=fertilizers_section)
npk_fertilizer = Object("NPK Fertilizer", status="Available", parent=chemical_fertilizers)
urea = Object("Urea", status="Available", parent=chemical_fertilizers)
ammonium_nitrate = Object("Ammonium Nitrate", status="Available", parent=chemical_fertilizers)

