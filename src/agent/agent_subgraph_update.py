import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tree_class import Object, Location
from anytree import findall_by_attr
from initialize_agent_subgraph import initialize_agent_subgraph
from nl_description_to_tree import nl_description_to_tree
import openai
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# Predefined locations
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

def query_llm_for_status_change(action_description, object_name):
    """
    Queries the LLM to determine the status change based on the action description.
    
    Parameters:
    action_description (str): A description of the action being performed.
    object_name (str): The name of the object involved in the action.
    
    Returns:
    str: The determined status of the object.
    """
    # Prepare the prompt for the LLM
    prompt = f"Given the following action: '{action_description}', what is the new status of the object '{object_name}'?"

    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7
    )

    return response.choices[0].text.strip()

def update_agent_subgraph(agent_subgraph, json_update):
    """
    Updates the agent's environment subgraph based on new JSON data.
    
    Parameters:
    agent_subgraph (Node): The root of the agent's current subgraph.
    json_update (dict): A JSON object containing the latest information about the agent's environment.
    
    Returns:
    Node: The updated subgraph.
    """
    # Extract information from the JSON update
    new_location = json_update.get("current_location")
    action_description = json_update.get("action", "")
    sandbox_item = json_update.get("sandbox_item", {})

    # Check if the agent has moved to a new location
    if new_location:
        location_node = findall_by_attr(agent_subgraph, new_location, maxlevel=2)
        if not location_node:
            # If the new location is not in the subgraph, check if it's a predefined location
            if new_location in predefined_locations:
                # Add the entire predefined location subtree
                predefined_location_tree = predefined_locations[new_location]
                predefined_location_tree.parent = agent_subgraph
            else:
                # Otherwise, just add a new location node
                new_location_node = Location(new_location, parent=agent_subgraph)

    # Update or add the sandbox item in the current location
    if sandbox_item:
        object_name = sandbox_item.get("name")
        new_status = sandbox_item.get("status", "None")
        object_node = findall_by_attr(agent_subgraph, object_name)

        if object_node:
            # Update the status if the object is found
            if object_node[0].status != new_status:
                object_node[0].status = new_status
        else:
            # If the object is not found, add it to the current location
            parent_location_node = findall_by_attr(agent_subgraph, new_location)
            if parent_location_node:
                new_object_node = Object(object_name, status=new_status, parent=parent_location_node[0])

    # Optionally, use the natural language to tree function or LLM to add or update objects based on actions
    if action_description:
        new_tree_part = nl_description_to_tree(action_description)
        # Assuming new_tree_part returns a root node that includes the context of the action
        if new_tree_part:
            for node in new_tree_part.children:
                matching_nodes = findall_by_attr(agent_subgraph, node.name)
                if matching_nodes:
                    # Use LLM to determine status if action is ambiguous
                    if node.status == "Unknown":
                        new_status = query_llm_for_status_change(action_description, node.name)
                        matching_nodes[0].status = new_status
                    else:
                        # Update the existing node
                        matching_nodes[0].status = node.status
                else:
                    # Add the new node
                    node.parent = agent_subgraph

    return agent_subgraph

# Example JSON update for testing with Radhika
example_json_update_radhika = {
    "current_location": "Cafe Building",
    "action": "Radhika moved to the Cafe Counter and ordered a cappuccino and a danish.",
    "sandbox_item": {"name": "Cafe Counter", "status": "In Use"}
}

if __name__ == "__main__":
    # Initialize the agent's subgraph for Radhika
    radhika_subgraph = initialize_agent_subgraph("""
    Radhika is a student at the local college. She knows about her neighborhood and park.
    """)

    # Update the agent's subgraph based on the new JSON update
    updated_subgraph = update_agent_subgraph(radhika_subgraph, example_json_update_radhika)

    # Optionally, print the updated tree structure to verify correctness
    from anytree import RenderTree

    for pre, fill, node in RenderTree(updated_subgraph):
        print(f"{pre}{node.name} ({node.type} - {node.status if hasattr(node, 'status') else ''})")
