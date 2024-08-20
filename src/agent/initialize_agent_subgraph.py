import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tree_class import Object, Location
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

# Load the API key from the .env file
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# Dictionary of predefined locations in the world tree
predefined_locations = {
    "Bar Building": bar_building,
    "Cafe Building": cafe_building,
    "Clothing Store": clothing_store,
    "College": college,
    "Convenience Store": convenience_store,
    "Department Store": department_store,
    "Gardening Store": gardening_store,
    "Neighborhood": neighborhood,
    "Park Area": park_area,
    "Pharmacy": pharmacy,
    "School Building": school_building,
}

def normalize(text):
    """Normalize text by converting to lowercase and removing extra spaces."""
    return text.lower().strip()

def custom_parse_agent_description(agent_description):
    """
    Parses the agent description and maps relevant locations to predefined locations.
    
    Parameters:
    agent_description (str): A natural language description of the agent's environment.
    
    Returns:
    Node: The root of the initialized subgraph.
    """
    # Create the root node for the agent's environment
    world_node = Location("World")
    normalized_description = normalize(agent_description)

    # Manually identify locations in the description and match them to predefined locations
    for location_name, location_tree in predefined_locations.items():
        # Normalize the predefined location names for comparison
        normalized_location_name = normalize(location_name)

        # If the normalized location name or a keyword from the predefined location appears in the description
        if any(keyword in normalized_description for keyword in [normalized_location_name, location_name.split()[0].lower()]):
            location_node = Location(location_name, parent=world_node)
            for child in location_tree.children:
                child.parent = location_node

    return world_node

# Function to initialize an agent's environment subgraph based on their description
def initialize_agent_subgraph(agent_description):
    """
    Initializes an agent's environment subgraph based on a natural language description.
    
    Parameters:
    agent_description (str): A natural language description of the agent's environment.
    
    Returns:
    Node: The root of the initialized subgraph.
    """
    # Create the subgraph using the custom parser
    agent_subgraph = custom_parse_agent_description(agent_description)

    return agent_subgraph

# Example of agent description used to create an agent in the paper
example_agent_description = """Radhika is a student at the local college. She knows about her neighborhood and park.  
"""

if __name__ == "__main__":
    # Initialize the subgraph for the example agent description
    agent_subgraph = initialize_agent_subgraph(example_agent_description)
    
    # Optionally, print the tree structure to verify correctness
    from anytree import RenderTree

    for pre, fill, node in RenderTree(agent_subgraph):
        print(f"{pre}{node.name} ({node.type} - {node.status if hasattr(node, 'status') else ''})")
