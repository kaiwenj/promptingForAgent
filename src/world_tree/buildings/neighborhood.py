import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from world_tree.base_classes import Location, Object



# Creating the Neighborhood node directly under the world node
neighborhood = Location("Neighborhood")

# Houses in the Neighborhood
house1 = Location("House 1", parent=neighborhood)
house2 = Location("House 2", parent=neighborhood)
house3 = Location("House 3", parent=neighborhood)
house4 = Location("House 4", parent=neighborhood)

# Rooms and objects in House 1
kitchen1 = Location("Kitchen", parent=house1)
living_room1 = Location("Living Room", parent=house1)
bedroom1_1 = Location("Bedroom 1", parent=house1)
bed1_1_1 = Object("Bed", parent=bedroom1_1)
bedroom1_2 = Location("Bedroom 2", parent=house1)
bed1_2_1 = Object("Bed", parent=bedroom1_2)
bedroom1_3 = Location("Bedroom 3", parent=house1)
bed1_3_1 = Object("Bed", parent=bedroom1_3)

# Rooms and objects in House 2
kitchen2 = Location("Kitchen", parent=house2)
living_room2 = Location("Living Room", parent=house2)
bedroom2_1 = Location("Bedroom 1", parent=house2)
bed2_1_1 = Object("Bed", parent=bedroom2_1)
bedroom2_2 = Location("Bedroom 2", parent=house2)
bed2_2_1 = Object("Bed", parent=bedroom2_2)
bedroom2_3 = Location("Bedroom 3", parent=house2)
bed2_3_1 = Object("Bed", parent=bedroom2_3)

# Rooms and objects in House 3
kitchen3 = Location("Kitchen", parent=house3)
living_room3 = Location("Living Room", parent=house3)
garden3 = Location("Garden", parent=house3)
bedroom3_1 = Location("Bedroom 1", parent=house3)
bed3_1_1 = Object("Bed", parent=bedroom3_1)
bedroom3_2 = Location("Bedroom 2", parent=house3)
bed3_2_1 = Object("Bed", parent=bedroom3_2)
bedroom3_3 = Location("Bedroom 3", parent=house3)
bed3_3_1 = Object("Bed", parent=bedroom3_3)

# Rooms and objects in House 4
kitchen4 = Location("Kitchen", parent=house4)
living_room4 = Location("Living Room", parent=house4)
garden4 = Location("Garden", parent=house4)
bedroom4_1 = Location("Bedroom 1", parent=house4)
bed4_1_1 = Object("Bed", parent=bedroom4_1)
bedroom4_2 = Location("Bedroom 2", parent=house4)
bed4_2_1 = Object("Bed", parent=bedroom4_2)
bedroom4_3 = Location("Bedroom 3", parent=house4)
bed4_3_1 = Object("Bed", parent=bedroom4_3)


  