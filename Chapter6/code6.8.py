import requests
from bs4 import BeautifulSoup

class Plant: # Create Plant Class
 def __init__(self, name, botanical, zone, light, price, availability):
     self.name = name
     self.botanical = botanical
     self.zone = zone
     self.light = light
     self.price = price
     self.availability = availability

 def __str__(self):
     return (
         f"Plant(Name: {self.name}, Botanical: {self.botanical},"
         f"Zone: {self.zone}, Light: {self.light},"
         f"Price: {self.price}, Availability: {self.availability})"
     )


# URL of the XML file
xml_url = "https://www.w3schools.com/xml/plant_catalog.xml"

# Making a request to the URL and getting the content
response = requests.get(xml_url)
xml_content = response.text

# Parsing the XML content with BeautifulSoup and lxml parser
soup = BeautifulSoup(xml_content, features="xml")

# Extracting information using Beautiful Soup and create Plant objects
plants = []
for plant_data in soup.find_all('PLANT'):
 name = plant_data.find('COMMON').text
 botanical = plant_data.find('BOTANICAL').text
 zone = plant_data.find('ZONE').text
 light = plant_data.find('LIGHT').text
 price = plant_data.find('PRICE').text
 availability = plant_data.find('AVAILABILITY').text

 plant = Plant(name, botanical, zone, light, price, availability)
 plants.append(plant)

# Printing Plant objects
print("Plant Information:")
for plant in plants:
 print(plant)
