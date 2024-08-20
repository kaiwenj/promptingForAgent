import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from world_tree.base_classes import Location, Object



# Creating the Park Area node directly under the world node
park_area = Location("Park Area")

# Park Features
playground = Location("Playground", parent=park_area)
slide = Object("Slide", status="None", parent=playground)
swing = Object("Swing", status="None", parent=playground)
sandbox = Object("Sandbox", status="None", parent=playground)

picnic_area = Location("Picnic Area", parent=park_area)
picnic_table = Object("Picnic Table", status="None", parent=picnic_area)
bbq_grill = Object("BBQ Grill", status="None", parent=picnic_area)

walking_trail = Location("Walking Trail", parent=park_area)
bench = Object("Bench", status="None", parent=walking_trail)
trash_can = Object("Trash Can", status="None", parent=walking_trail)

pond = Location("Pond", parent=park_area)
duck = Object("Duck", status="Swimming", parent=pond)
fish = Object("Fish", status="Swimming", parent=pond)

flower_garden = Location("Flower Garden", parent=park_area)
rose = Object("Rose", status="Blooming", parent=flower_garden)
tulip = Object("Tulip", status="Blooming", parent=flower_garden)
daffodil = Object("Daffodil", status="Blooming", parent=flower_garden)

