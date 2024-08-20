import sys
import os
import json
from anytree import RenderTree

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from world_tree.json_to_tree import json_to_tree
from world_tree.tree_to_json import tree_to_json

# Example JSON structure (could also load from a file)
json_data = '''
{
    "name": "Bar Building",
    "type": "location",
    "contents": [],
    "actors": [],
    "children": [
        {
            "name": "Table",
            "type": "object",
            "status": "Clean",
            "contents": [],
            "children": [
                {
                    "name": "Chair",
                    "type": "object",
                    "status": "Available",
                    "contents": []
                }
            ]
        },
        {
            "name": "Bar Counter",
            "type": "object",
            "status": "Wiped",
            "contents": [],
            "children": [
                {
                    "name": "Register",
                    "type": "object",
                    "status": "Functional",
                    "contents": []
                },
                {
                    "name": "Bar Stool",
                    "type": "object",
                    "status": "Available",
                    "contents": []
                }
            ]
        },
        {
            "name": "Drink Menu",
            "type": "object",
            "status": "Not in use, [description of menu items] Drinks: Beer, Wine, Whiskey, Vodka, Rum, Tequila, Gin | Cocktails: Margarita, Mojito, Martini, Old Fashioned, Daiquiri, Manhattan",
            "contents": [],
            "children": [
                {
                    "name": "Beer",
                    "type": "object",
                    "status": "Chilled",
                    "contents": []
                },
                {
                    "name": "Wine",
                    "type": "object",
                    "status": "Chilled",
                    "contents": []
                },
                {
                    "name": "Whiskey",
                    "type": "object",
                    "status": "Room Temperature",
                    "contents": []
                },
                {
                    "name": "Vodka",
                    "type": "object",
                    "status": "Chilled",
                    "contents": []
                },
                {
                    "name": "Rum",
                    "type": "object",
                    "status": "Room Temperature",
                    "contents": []
                },
                {
                    "name": "Tequila",
                    "type": "object",
                    "status": "Chilled",
                    "contents": []
                },
                {
                    "name": "Gin",
                    "type": "object",
                    "status": "Chilled",
                    "contents": []
                },
                {
                    "name": "Cocktails",
                    "type": "object",
                    "status": "Ready to Mix",
                    "contents": [],
                    "children": [
                        {
                            "name": "Margarita",
                            "type": "object",
                            "status": "Not Prepared",
                            "contents": []
                        },
                        {
                            "name": "Mojito",
                            "type": "object",
                            "status": "Not Prepared",
                            "contents": []
                        },
                        {
                            "name": "Martini",
                            "type": "object",
                            "status": "Not Prepared",
                            "contents": []
                        },
                        {
                            "name": "Old Fashioned",
                            "type": "object",
                            "status": "Not Prepared",
                            "contents": []
                        },
                        {
                            "name": "Daiquiri",
                            "type": "object",
                            "status": "Not Prepared",
                            "contents": []
                        },
                        {
                            "name": "Manhattan",
                            "type": "object",
                            "status": "Not Prepared",
                            "contents": []
                        }
                    ]
                }
            ]
        },
        {
            "name": "Snacks Menu",
            "type": "object",
            "status": "Not in use, [description of snacks] Peanuts, Chips, Pretzels, Popcorn, Nachos, Buffalo Wings, Onion Rings",
            "contents": [],
            "children": [
                {
                    "name": "Peanuts",
                    "type": "object",
                    "status": "Fresh",
                    "contents": []
                },
                {
                    "name": "Chips",
                    "type": "object",
                    "status": "Fresh",
                    "contents": []
                },
                {
                    "name": "Pretzels",
                    "type": "object",
                    "status": "Fresh",
                    "contents": []
                },
                {
                    "name": "Popcorn",
                    "type": "object",
                    "status": "Fresh",
                    "contents": []
                },
                {
                    "name": "Nachos",
                    "type": "object",
                    "status": "Fresh",
                    "contents": []
                },
                {
                    "name": "Buffalo Wings",
                    "type": "object",
                    "status": "Fresh",
                    "contents": []
                },
                {
                    "name": "Onion Rings",
                    "type": "object",
                    "status": "Fresh",
                    "contents": []
                }
            ]
        }
    ]
}
'''

# Convert JSON to Tree
root_node = json_to_tree(json.loads(json_data))

# Print the tree structure to verify correctness
for pre, fill, node in RenderTree(root_node):
    print(f"{pre}{node.name} ({node.type} - {node.status if hasattr(node, 'status') else ''})")

# Optional: Convert back to JSON and compare to ensure round-trip consistency
#reconverted_json = tree_to_json(root_node)
#print(reconverted_json)
