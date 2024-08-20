import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from world_tree.buildings.bar import bar_building
from world_tree.tree_to_json import save_tree_to_json_file

# Test: Save the JSON representation of the bar building to a file
save_tree_to_json_file(bar_building, "bar_building.json")

# You can also add tests for other buildings or the entire world tree
from world_tree.root import world

# Test: Save the JSON representation of the entire world tree to a file
save_tree_to_json_file(world, "world_tree.json")
