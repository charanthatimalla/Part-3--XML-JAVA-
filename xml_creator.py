
import xml.etree.ElementTree as ET

# create the root element
root = ET.Element("students")

# create child elements with attributes and text
student1 = ET.SubElement(root, "student", {"id": "001"})
name1 = ET.SubElement(student1, "name")
name1.text = "Alice"
age1 = ET.SubElement(student1, "age")
age1.text = "20"

student2 = ET.SubElement(root, "student", {"id": "002"})
name2 = ET.SubElement(student2, "name")
name2.text = "Bob"
age2 = ET.SubElement(student2, "age")
age2.text = "22"

# create the tree from the root element and write to file
tree = ET.ElementTree(root)
tree.write("students.xml", encoding="UTF-8", xml_declaration=True)