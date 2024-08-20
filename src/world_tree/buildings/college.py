import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from world_tree.base_classes import Location, Object



# Creating the College node directly under the world node
college = Location("College")

# College Buildings
admin_building = Location("Administrative Building", parent=college)
library = Location("Library", parent=college)
science_building = Location("Science Building", parent=college)
lecture_hall = Location("Lecture Hall", parent=college)
cafeteria = Location("Cafeteria", parent=college)
gym = Location("Gym", parent=college)

# Dorm Buildings
dorm_buildings = Location("Dorm Buildings", parent=college)
dorm_a = Location("Dorm A", parent=dorm_buildings)
dorm_b = Location("Dorm B", parent=dorm_buildings)
dorm_c = Location("Dorm C", parent=dorm_buildings)

# Rooms in Dorm A
room_101 = Location("Room 101", parent=dorm_a)
room_102 = Location("Room 102", parent=dorm_a)
room_103 = Location("Room 103", parent=dorm_a)

# Rooms in Dorm B
room_201 = Location("Room 201", parent=dorm_b)
room_202 = Location("Room 202", parent=dorm_b)
room_203 = Location("Room 203", parent=dorm_b)

# Rooms in Dorm C
room_301 = Location("Room 301", parent=dorm_c)
room_302 = Location("Room 302", parent=dorm_c)
room_303 = Location("Room 303", parent=dorm_c)

