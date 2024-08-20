import sys
import os
from anytree import RenderTree

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from agent.nl_description_to_tree import nl_description_to_tree

# Example natural language description
nl_description = "The bar building has a table with a chair on it, a bar counter with a register and a bar stool, and a menu with drinks and snacks listed."

# Convert the NL description to a tree structure
tree = nl_description_to_tree(nl_description)

# Print the tree structure to verify correctness
for pre, fill, node in RenderTree(tree):
    print(f"{pre}{node.name} ({node.type} - {node.status if hasattr(node, 'status') else ''})")
