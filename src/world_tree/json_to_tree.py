import json
from world_tree.base_classes import Location, Object

def json_to_tree(json_data):
    """
    Recursively converts a JSON structure to an anytree structure.
    
    :param json_data: A JSON string or dictionary representing the tree structure.
    :return: The root node of the resulting anytree structure.
    """
    if isinstance(json_data, str):
        json_data = json.loads(json_data)
    
    def create_node(data, parent=None):
        node_type = data.get('type')
        if node_type == 'location':
            node = Location(name=data['name'], parent=parent)
        elif node_type == 'object':
            node = Object(name=data['name'], status=data.get('status', 'None'), parent=parent)
        else:
            raise ValueError(f"Unknown node type: {node_type}")
        
        # Recursively create children nodes
        for child in data.get('children', []):
            create_node(child, parent=node)
        
        return node
    
    return create_node(json_data)
