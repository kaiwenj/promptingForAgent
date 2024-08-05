from anytree import Node, RenderTree

# Creating nodes
root = Node("World")
SchoolBuilding = Node("School Building", parent=root)

ClassRoom = Node("ClassRoom", parent=SchoolBuilding)
Whiteboard = Node("Whiteboard", parent=ClassRoom)
DryEraseMarker = Node("Dry Erase Marker", parent=Whiteboard)
DeskChair = Node("DeskChair", parent=ClassRoom)
TeacherDesk = Node("Teacher Desk", parent=ClassRoom)
Laptops = Node("Laptops", parent=DeskChair)
Projector = Node("Projector", parent=TeacherDesk)

ClassRoom2 = Node("ClassRoom2", parent=SchoolBuilding)
Whiteboard2 = Node("Whiteboard2", parent=ClassRoom2)
DryEraseMarker2 = Node("DryEraseMarker2", parent=Whiteboard2)
DeskChair2 = Node("DeskChair2", parent=ClassRoom2)
TeacherDesk2 = Node("TeacherDesk2", parent=ClassRoom2)
Laptops2 = Node("Laptops2", parent=DeskChair2)
Projector2 = Node("Projector2", parent=TeacherDesk2)

ClassRoom3 = Node("ClassRoom3", parent=SchoolBuilding)
Whiteboard3 = Node("Whiteboard3", parent=ClassRoom3)
DryEraseMarker3 = Node("DryEraseMarker3", parent=Whiteboard3)
DeskChair3 = Node("DeskChair3", parent=ClassRoom3)
TeacherDesk3 = Node("TeacherDesk3", parent=ClassRoom3)
Laptops3 = Node("Laptops3", parent=DeskChair3)
Projector3 = Node("Projector3", parent=TeacherDesk3)

Courtyard = Node("Courtyard", parent=SchoolBuilding)
LunchTable = Node("LunchTable", parent=Courtyard)
BasketballCourt = Node("BasketballCourt", parent=Courtyard)
Basketballs = Node("Basketballs", parent=BasketballCourt)
TennisCourt = Node("TennisCourt", parent=Courtyard)
TennisRackets = Node("TennisRackets", parent=TennisCourt)
TennisBalls = Node("TennisBalls", parent=TennisCourt)
TrackField = Node("TrackField", parent=Courtyard)
FootballField = Node("FootballField", parent=Courtyard)
Footballs = Node("Footballs", parent=FootballField)
Pool = Node("Pool", parent=Courtyard)
Garden = Node("Garden", parent=Courtyard)
TomatoePlant = Node("TomatoePlant", parent=Garden)
LemonTree = Node("LemonTree", parent=Garden)
xplant1 = Node("xplant1", parent=Garden)
xplant2 = Node("xplant2", parent=Garden)
xplant3 = Node("xplant3", parent=Garden)

# Displaying the tree
def display_tree(node):
    for pre, fill, node in RenderTree(node):
        print(f"{pre}{node.name}")

# Function to add a node
def add_node(parent_name, node_name, root):
    parent_node = next((n for n in root.descendants if n.name == parent_name), None)
    if parent_node:
        new_node = Node(node_name, parent=parent_node)
        print(f"Node '{node_name}' added under '{parent_name}'.")
    else:
        print(f"Parent node '{parent_name}' not found.")

# Function to delete a node
def delete_node(node_name, root):
    node_to_delete = next((n for n in root.descendants if n.name == node_name), None)
    if node_to_delete and node_to_delete != root:
        node_to_delete.parent = None
        print(f"Node '{node_name}' deleted.")
    else:
        print(f"Node '{node_name}' not found or it is the root node.")

# Function to modify a node
def modify_node(node_name, new_name, root):
    node = next((n for n in root.descendants if n.name == node_name), None)
    if node:
        node.name = new_name
        print(f"Node '{node_name}' modified to '{new_name}'.")
    else:
        print(f"Node '{node_name}' not found.")

# Interactive menu
def menu():
    print("\nMenu:")
    print("1. Display Tree")
    print("2. Add Node")
    print("3. Delete Node")
    print("4. Modify Node")
    print("5. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            print("\nTree Structure:")
            display_tree(root)
        elif choice == '2':
            parent_name = input("Enter the name of the parent node: ")
            node_name = input("Enter the name of the new node: ")
            add_node(parent_name, node_name, root)
        elif choice == '3':
            node_name = input("Enter the name of the node to delete: ")
            delete_node(node_name, root)
        elif choice == '4':
            node_name = input("Enter the name of the node to modify: ")
            new_name = input("Enter the new name of the node: ")
            modify_node(node_name, new_name, root)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
