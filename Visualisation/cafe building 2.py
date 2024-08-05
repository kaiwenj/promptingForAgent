from anytree import Node, RenderTree

# Creating nodes
root = Node("World")
CafeBuilding = Node("School Building", parent=root)

Table =  Node("Table", parent=CafeBuilding)
Chair = Node("Chair", parent=Table)
Register = Node("Register", parent=CafeBuilding)
CofeeMakingBar = Node("CofeeMakingBar", parent=CafeBuilding)
CofeeMaker = Node("CofeeMaker", parent=CofeeMakingBar)

CafeMenu = Node("Cafe Menu", parent=CafeBuilding)
Espresso = Node("Espresso", parent=CafeMenu)
CaféCubano = Node("Café Cubano", parent=CafeMenu)
Americano = Node("Americano", parent=CafeMenu)
Latte = Node("Latte", parent=CafeMenu)
Cappuccino = Node("Cappuccino", parent=CafeMenu)
Macchiato = Node("Macchiato", parent=CafeMenu)
Mocha = Node("Mocha", parent=CafeMenu)
FlatWhite = Node("Flat White", parent=CafeMenu)
Cortado = Node("Cortado", parent=CafeMenu)
Ristretto = Node("Ristretto", parent=CafeMenu)
Lungo = Node("Lungo", parent=CafeMenu)
Affogato = Node("Affogato", parent=CafeMenu)
RedEye = Node("Red Eye", parent=CafeMenu)
BlackEye = Node("Black Eye", parent=CafeMenu)
Doppio = Node("Doppio", parent=CafeMenu)
Café_au_Lait = Node("Café au Lait ", parent=CafeMenu)
IrishCoffee = Node("Irish Coffee", parent=CafeMenu)
TurkishCoffee = Node("Turkish Coffee", parent=CafeMenu)
ColdBrew = Node("Cold Brew", parent=CafeMenu)
NitroCoffee = Node("Nitro Coffee", parent=CafeMenu)
IcedCoffee = Node("Ice Coffee", parent=CafeMenu)
Frappe = Node("Frappe", parent=CafeMenu)
ViennaCoffee = Node("Vienna Coffee", parent=CafeMenu)
Breve = Node("Breve", parent=CafeMenu)
DripCoffee = Node("Drip Coffee", parent=CafeMenu)

BakedGoodsMenu = Node("Baked Goods Menu", parent=CafeBuilding)
ChocolateChipCookies = Node("Chocolate Chip Cookies", parent=BakedGoodsMenu)
OatmealRaisinCookies = Node("Oatmeal Raisin Cookies", parent=BakedGoodsMenu)
SugarCookies = Node("Sugar Cookies", parent=BakedGoodsMenu)
GingerbreadCookies = Node("Gingerbread Cookies", parent=BakedGoodsMenu)
Croissant = Node("Croissant", parent=BakedGoodsMenu)
Danish = Node("Danish", parent=BakedGoodsMenu)
PainauChocolat = Node("Pain au Chocolat", parent=BakedGoodsMenu)
Baguette = Node("Baguette", parent=BakedGoodsMenu)
BlueberryMuffins = Node("Blueberry Muffins", parent=BakedGoodsMenu)
BananaMuffins = Node("Banana Muffins", parent=BakedGoodsMenu)
ChocolateMuffins = Node("Chocolate Muffins", parent=BakedGoodsMenu)
VanillaCupcakes = Node("Vanilla Cupcakes", parent=BakedGoodsMenu)
RedVelvetCupcakes = Node("Red Velvet Cupcakes", parent=BakedGoodsMenu)
ApplePie = Node("Apple Pie", parent=BakedGoodsMenu)
PumpkinPie = Node("Pumpkin Pie", parent=BakedGoodsMenu)
GlazedDoughnuts = Node("Glaze Doughnuts", parent=BakedGoodsMenu)

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
