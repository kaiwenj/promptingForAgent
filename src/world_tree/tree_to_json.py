import json
from anytree.exporter import DictExporter

def tree_to_json(root_node):
    """
    Converts an anytree structure to a JSON data structure.
    
    :param root_node: The root node of the anytree structure.
    :return: A JSON string representing the tree structure.
    """
    exporter = DictExporter()
    tree_dict = exporter.export(root_node)
    
    return json.dumps(tree_dict, indent=4)

def save_tree_to_json_file(root_node, file_path):
    """
    Converts an anytree structure to a JSON file.
    
    :param root_node: The root node of the anytree structure.
    :param file_path: The path where the JSON file will be saved.
    """
    json_data = tree_to_json(root_node)
    
    with open(file_path, 'w') as json_file:
        json_file.write(json_data)
    print(f"Tree structure saved to {file_path}")
