import openai
import json
from anytree import NodeMixin
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# Instantiate the OpenAI client
client = openai.OpenAI(api_key=openai_api_key)


def prompt_llm_to_generate_tree(nl_description):
    """
    Sends a prompt to the LLM to parse the NL description into a tree structure.
    """
    system_input_message = """
    You are an assistant that helps convert natural language descriptions into tree structures.
    Each node in the tree must include a 'name', a 'type' (either 'location' or 'object'), 
    and can have an optional 'status'. Sub-locations or sub-objects should be included in a 'children' list.
    Please format the output in a JSON-like structure as follows:

    {
        "type": "location",
        "name": "Location Name",
        "status": "optional status",
        "children": [
            {
                "type": "object",
                "name": "Object Name",
                "status": "optional status",
                "children": []
            }
        ]
    }
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_input_message},
            {"role": "user", "content": nl_description}
        ]
    )

    # Extract the response from the LLM
    return response.choices[0].message.content

def parse_llm_output_to_tree(llm_output):
    """
    Parses the LLM output into an anytree structure.
    """

    
    # Utilize the json_to_tree function here
    from world_tree.json_to_tree import json_to_tree
    
    return json_to_tree(llm_output)

def nl_description_to_tree(nl_description):
    """
    Converts a natural language description to a tree structure using LLM.
    """
    llm_output = prompt_llm_to_generate_tree(nl_description)

    
    # Assuming the LLM output is in JSON format; parse it as JSON
    llm_output_json = json.loads(llm_output)
    return parse_llm_output_to_tree(llm_output_json)
