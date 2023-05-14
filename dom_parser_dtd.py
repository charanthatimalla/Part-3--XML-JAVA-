

from xml.dom import minidom
from xml.dom.minidom import Node
from lxml import etree

# parse the XML document
doc = minidom.parse("person.xml")

# validate against the schema
schema_doc = minidom.parse("person.xsd")
schema = etree.XMLSchema(etree.fromstring(schema_doc.toxml()))

if not schema.validate(doc):
    print("Validation error")
    for error in schema.error_log:
        print(error)
else:
    print("Validation successful")

# get the person element
person = doc.getElementsByTagName("person")[0]

# get the name element
name = person.getElementsByTagName("name")[0]

# print the name value
print(name.firstChild.nodeValue)

# get the age element
age = person.getElementsByTagName("age")[0]

# print the age value
print(age.firstChild.nodeValue)

# get the address element
address = person.getElementsByTagName("address")[0]

# get the street element
street = address.getElementsByTagName("street")[0]

# print the street value
print(street.firstChild.nodeValue)

# get the city element
city = address.getElementsByTagName("city")[0]

# print the city value
print(city.firstChild.nodeValue)

# get the state element
state = address.getElementsByTagName("state")[0]

# print the state value
print(state.firstChild)


