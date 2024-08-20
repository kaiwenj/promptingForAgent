import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from world_tree.base_classes import Location, Object



# Creating the School Building node directly under the world node
school_building = Location("School Building")

# Classrooms in the school
classroom1 = Location("ClassRoom", parent=school_building)
whiteboard1 = Object("Whiteboard", status="Clean", parent=classroom1)
dry_erase_marker1 = Object("Dry Erase Marker", status="Capped", parent=whiteboard1)
desk_chair1 = Object("Desk Chair", status="Arranged", parent=classroom1)
teacher_desk1 = Object("Teacher Desk", status="Organized", parent=classroom1)
laptops1 = Object("Laptops", status="Charged", parent=desk_chair1)
projector1 = Object("Projector", status="Off", parent=teacher_desk1)

classroom2 = Location("ClassRoom2", parent=school_building)
whiteboard2 = Object("Whiteboard2", status="Clean", parent=classroom2)
dry_erase_marker2 = Object("Dry Erase Marker", status="Capped", parent=whiteboard2)
desk_chair2 = Object("Desk Chair", status="Arranged", parent=classroom2)
teacher_desk2 = Object("Teacher Desk", status="Organized", parent=classroom2)
laptops2 = Object("Laptops", status="Charged", parent=desk_chair2)
projector2 = Object("Projector", status="Off", parent=teacher_desk2)

classroom3 = Location("ClassRoom3", parent=school_building)
whiteboard3 = Object("Whiteboard3", status="Clean", parent=classroom3)
dry_erase_marker3 = Object("Dry Erase Marker", status="Capped", parent=whiteboard3)
desk_chair3 = Object("Desk Chair", status="Arranged", parent=classroom3)
teacher_desk3 = Object("Teacher Desk", status="Organized", parent=classroom3)
laptops3 = Object("Laptops", status="Charged", parent=desk_chair3)
projector3 = Object("Projector", status="Off", parent=teacher_desk3)

# Courtyard in the school
courtyard = Location("Courtyard", parent=school_building)
lunch_table = Object("Lunch Table", status="Clean", parent=courtyard)
basketball_court = Location("Basketball Court", parent=courtyard)
basketballs = Object("Basketballs", status="Available", parent=basketball_court)
tennis_court = Location("Tennis Court", parent=courtyard)
tennis_rackets = Object("Tennis Rackets", status="Available", parent=tennis_court)
tennis_balls = Object("Tennis Balls", status="Available", parent=tennis_court)
track_field = Location("Track Field", parent=courtyard)
football_field = Location("Football Field", parent=courtyard)
footballs = Object("Footballs", status="Available", parent=football_field)
pool = Location("Pool", parent=courtyard)
garden = Location("Garden", parent=courtyard)
tomato_plant = Object("Tomato Plant", status="Growing", parent=garden)
lemon_tree = Object("Lemon Tree", status="Bearing Fruit", parent=garden)

