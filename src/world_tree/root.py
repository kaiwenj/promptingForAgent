import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from anytree import RenderTree
from world_tree.base_classes import Location, Object



# Create the world root node
world = Location("World")

# Import the main building nodes from each building module
from world_tree.buildings.bar import bar_building
from world_tree.buildings.cafe import cafe_building
from world_tree.buildings.clothing_store import clothing_store
from world_tree.buildings.college import college
from world_tree.buildings.convenience_store import convenience_store
from world_tree.buildings.department_store import department_store
from world_tree.buildings.gardening_store import gardening_store
from world_tree.buildings.neighborhood import neighborhood
from world_tree.buildings.park import park_area
from world_tree.buildings.pharmacy import pharmacy
from world_tree.buildings.school import school_building

# Connect each building to the world root node
building_nodes = [
    bar_building,
    cafe_building,
    clothing_store,
    college,
    convenience_store,
    department_store,
    gardening_store,
    neighborhood,
    park_area,
    pharmacy,
    school_building
]

for building in building_nodes:
    building.parent = world  # Set the parent of each building to 'world'

# Optionally, render the entire tree to verify the structure
for pre, fill, node in RenderTree(world):
    print(f"{pre}{node.name} ({node.type} - {node.status if hasattr(node, 'status') else ''})")
