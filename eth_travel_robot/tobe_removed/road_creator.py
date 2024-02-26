import xml.etree.ElementTree as ET

# Create the root element for the SDF document
root = ET.Element("sdf", version="1.6")

# Create the world element
world = ET.SubElement(root, "world", name="my_world")

# Function to create a road segment
def create_road_segment(segment_name, start_x, start_y, end_x, end_y):
    # Create the model element for the road segment
    model = ET.SubElement(world, "model", name=segment_name)

    # Create the link element for the road segment
    link = ET.SubElement(model, "link", name="road_link")

    # Create the collision element for the road segment
    collision = ET.SubElement(link, "collision", name="road_collision")
    collision_geometry = ET.SubElement(collision, "geometry")
    collision_box = ET.SubElement(collision_geometry, "box")
    collision_box_size = ET.SubElement(collision_box, "size")
    collision_box_size.text = "10 2 0.01"

    # Create the visual element for the road segment
    visual = ET.SubElement(link, "visual", name="road_visual")
    visual_geometry = ET.SubElement(visual, "geometry")
    visual_box = ET.SubElement(visual_geometry, "box")
    visual_box_size = ET.SubElement(visual_box, "size")
    visual_box_size.text = "10 2 0.01"

    # Create the material element for the road segment
    material = ET.SubElement(visual, "material")
    script = ET.SubElement(material, "script")
    uri = ET.SubElement(script, "uri")
    uri.text = "file://media/materials/scripts/gazebo.material"
    name = ET.SubElement(script, "name")
    name.text = "Gazebo/White"

    # Create the pose element for the road segment
    pose = ET.SubElement(visual, "pose")
    pose.text = f"{start_x} {start_y} 0 0 0 0"

    # Optional: Add lane markings, starting point, ending point, etc.

# Create road segments
create_road_segment("seg1", 0, 0, 10, 0)
create_road_segment("seg2", 10, 0, 10, 10)
create_road_segment("seg3", 10, 10, 0, 10)

# Create an ElementTree object and write it to a file
tree = ET.ElementTree(root)
tree.write("network_of_roads.sdf")
