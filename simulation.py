import os
import json
import socket
import openai

'''replace with an import module for Actor class: e.g.  "import actor.py" '''
class Actor:
    def __init__( self, name, location, mem_stream ):
        self.name = name
        self.location = location
        self.mem_stream = mem_stream
    def add_mem( self, mem, time ):
        self.mem_stream.append((mem,time))
    def act( self ):
        return self.name + "moves to the Bedroom"

'''set up background information and actor objects before running simulation'''
#each cycle is 10 seconds
actors = [Actor("Lohit", (2,5), ["Lohit is a student working on LLM research"]), Actor("Professor Tao",(3,5), ["Professor Tao is conducting LLM research"]),
                Actor("Jan", (4,5), ["Jan is Lohit's friend and neighbor"])]
#server details
HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080
RECV_SIZE = 1024

'''helper functions for communicating via socket with Phaser'''
def start_connection( host, port ):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    return s
def accept_connection( s ):
    s.listen(1)
    conn, addr = s.accept()
    return conn,addr
def recieve_json( conn ):
    data = conn.recv(RECV_SIZE).decode('utf-8')
    print(data)
    data = json.loads(data)
    return data
def send_actions( conn, actions ):
    conn.sendall( json.dumps(actions).encode() )

'''helper functions for rest of simulation'''
def create_input_to_actor( house, actor ):
    for room in house["contents"]:
        if actor in room["actors"]:
            return room

'''given the name of an actor, actor, and a new_location to move to, new_location, removes the actor from its current location and moves
them to the new location'''
def move_actor( house, actor, new_location ):
    for room in house["contents"]:
        if room["name"] == new_location and actor not in room["actors"]:
            room["actors"].append(actor)
        elif actor in room["actors"]:
            if room["name"] != new_location:
                room["actors"].remove(actor)

'''recursive function that finds the object with a name that matches the "query" input string, and returns it '''
def search_tree( head, query ):
    if not head["contents"]:
        return None
    for branch in head["contents"]:
        if branch["name"] == query:
            return branch
        branch_search = search_tree( branch, query )
        if branch_search != None:
            return branch_search

def object_changes( house, actor, action ):
    action = actor + " is " + action
    API_KEY = "YOUR KEY HERE"
    client = openai.OpenAI( api_key = API_KEY )
    #this is the prompt for the llm to be able to parse an actor's actions into one of the three updates to the json that an actor can do
    system_input_message = """Your job is to determine if the given action by an actor in this virtual world requires an object to be updated, and what the updated
    status of that object should be. Attached you have a json formatted world, with objects identified as having an "object" type, and their name defined under the "name" attribute
    I will pass you an action, and you will output two parts: the name of the object and what you think the updated status of the object should be, seperated by the "|" symbol.
    For example, if the action is making coffee at the cafe, then the output will be Coffee Machine | Brewing Coffee. Make sure to preserve any important details
    about the object in the status if it is already there. If there are no objects
    that are affected, then output None. For example, the action going to the park would affect no objects. Here is the json formatted environment
    for reference: """ + json.dumps( house )
    action = "sits on the stool at the bar"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_input_message},
            {"role": "user", "content": action}
        ]
    ).choices[0].message.content
    if "none" in response.lower():
        return house
    if "|" not in response:
        return house
    response = response.split("|")
    obj_name = response[0].strip()
    obj_status = "|".join( response[1:] )

    obj = search_tree( house, obj_name )
    obj["status"] = obj_status

    return house

'''complete clock cycle'''
def run_cycle (prev_time, conn):
    time = prev_time + 1 

    #make new directories for new clock cycle
    os.mkdir(f"actor_log/{time}")
    os.mkdir(f"actor_log/{time}/env")
    os.mkdir(f"actor_log/{time}/actor")
    
    #load house from previous clock cycle
    f = open( f"actor_log/{prev_time}/env/house.json" )
    house = json.load(f)
    
    #pass in observations to each actor
    for actor in actors:
        observation_for_actor = create_input_to_actor( house, actor.name )
        '''needs to be changed based on final actor object'''
        actor.add_mem(observation_for_actor, time)
        print(actor.name, actor.mem_stream)

    #store each action object in list: actor_actions
    actor_dict = {}
    actor_actions = []
    for actor in actors:
        '''actor_action in json format: e.g. {"name" : "Tao", "action": "getting coffee", "location": "Kitchen"}'''
        actor_action = actor.act()
        actor_actions.append( actor_action )
        actor_dict[actor_action["name"]] = actor_action["action"]
    
    #send actions via the socket connection
    send_actions( conn, actor_status )

    #receive status for each actor by the end of the clock cycle, update the env and store their status in a json file
    '''format: list[ dict{ "name": "Tao", "place":"Bedroom", "x":10, "y":10, "plan_finished":False }, ... ]'''
    actor_status = recieve_json( conn )
    for status in actor_status:
        name = status["name"]
        move_actor( house, name, status["place"] )
        if status["plan_finished"] == True:
            house = object_changes( house, name, actor_actions[name] )
        with open (f"actor_log/{time}/actor/{name}.json","w") as outfile:
            json.dump(status, outfile )   

    #dump env json into new clock cycle folder
    with open(f"actor_log/{time}/env/house.json", "w") as outfile:
        json.dump(house, outfile)

    f.close()

#main loop
if __name__ == "__main__":
    #bind host and port
    s = start_connection( HOST, PORT )
    #accept socket connection
    conn, addr = accept_connection( s )
    for i in range(5):
        run_cycle(i, conn)
    s.close()