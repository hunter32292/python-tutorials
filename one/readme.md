# Working with data generated from a csv/json file

Create a new directory or workspace called: **exercise-one**

`mkdir exercise-one`

## Using Mockaroo Generated data

Go to https://www.mockaroo.com/ and generate a fake CSV and JSON file

#### Data Fields to use:
- id
- city
- last_name
- first_name
- gender
- ip_address

Save the files as **people.csv** and **people.json** in the directory you are working in.

## Example Data
CSV Data
```
id,city,last_name,first_name,gender,ip_address
1,Nyköping,Dahlman,Jennica,Female,35.225.50.109
2,El Galpón,Baress,Brock,Male,125.243.119.118
3,Kadudampit,Jacquemy,Eli,Male,115.107.136.184
4,Jingzhou,Hawlgarth,Cosetta,Female,121.141.6.95
5,Zlonice,Laraway,Gay,Male,71.19.84.25
```
JSON Data

```
[{
  "id": 1,
  "city": "Zhulan",
  "last_name": "Pepperell",
  "first_name": "Bette-ann",
  "gender": "Female",
  "ip_address": "224.46.58.251"
}, {
  "id": 2,
  "city": "Sapernoye",
  "last_name": "Gallacher",
  "first_name": "Alon",
  "gender": "Male",
  "ip_address": "88.4.151.23"
}, {
  "id": 3,
  "city": "Niwiska",
  "last_name": "Rolls",
  "first_name": "Alexei",
  "gender": "Male",
  "ip_address": "73.173.130.194"
}, {
  "id": 4,
  "city": "Kushar",
  "last_name": "Godney",
  "first_name": "Dorry",
  "gender": "Female",
  "ip_address": "98.111.97.25"
}, {
  "id": 5,
  "city": "Sumbersewu",
  "last_name": "Roglieri",
  "first_name": "Phedra",
  "gender": "Female",
  "ip_address": "21.106.20.235"
}]
```

### Creating a python script to work with this data

1. Create a class for people

```
class People(object):

    def __init__(self, id_num, city, last_name, first_name, gender, ip_address):
        self.id_num = id_num
        self.city = city
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.ip_address = ip_address

```
2. Open and iterate through the list of people
```
import json 

def work_on_file(file_name):
    lines = ""
    try:
        with open(file_name) as f_obj:
            lines = f_obj.readlines()
        if len(lines) <= 0:
            print("File is empty")
            return
    except FileNotFoundError:
        print("Cannot access file %s" % file_name)

    if ".json" in file_name:
        return json.load(open(file_name))

    if ".csv" in file_name:
        new_lines = []
        for line in lines:
            line = line.split(',')
            new_lines.append(line)
        return new_lines

    return lines


if __name__ == "__main__":
    work_on_file("people.csv")
    work_on_file("people.json")
```
3. Adding to the previous file. Create each of those people as a object from the data in the files we downloaded.
```
import json
# From "FILE" import "Object" 
from . import PersonSimple

.
.
.

if __name__ == "__main__":
    people = []
    lines = work_on_file("MOCK_DATA.csv")
    for line in lines:
        people.append(PersonSimple(line[0],line[1],line[2],line[3],line[4],line[5]))
    print("People: %s" % people)

    people = []
    lines = work_on_file("MOCK_DATA.json")
    for line in lines:
        people.append(PersonSimple(line['id'],line['city'],line['last_name'],line['first_name'],line['gender'],line['ip_address']))
    print("People: %s" % people)

```
4. Add validation to ensure the following
- No value is None
- Gender follows and Enum class of Male, Female, Other
- Ensure that IP address matches a Regex of three numbers max split by `.` 4 times
```
from enum import Enum
import operator
import re

# An Internal Python Class to the ComplexPeople Class
class Gender(Enum):
    male = 0
    female = 1
    other = 2

class ComplexPeople(object):

    def __init__(self, id_num, city, last_name, first_name, gender, ip_address):
        self.id_num = id_num
        self.city = city
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.ip_address = ip_address

    """
    Getters/Setters    
    """
    # THIS IS A GETTER
    id_num = property(operator.attrgetter('_id_num'))

    # THIS IS A SETTER
    @id_num.setter
    def id_num(self, id_num):
        if not id_num:
            raise Exception("ID Cannot be a Null Value")
        self._id = id_num

    city = property(operator.attrgetter('_city'))
    
    @city.setter
    def city(self, city):
        if not city:
            raise Exception("ID Cannot be a Null Value")
        self._id = city

    last_name = property(operator.attrgetter('_last_name'))
    
    @last_name.setter
    def last_name(self, last_name):
        if not last_name:
            raise Exception("ID Cannot be a Null Value")
        self._id = last_name

    first_name = property(operator.attrgetter('_first_name'))
    
    @first_name.setter
    def first_name(self, first_name):
        if not first_name:
            raise Exception("ID Cannot be a Null Value")
        self._id = first_name

    gender = property(operator.attrgetter('_gender'))
    
    @gender.setter
    def gender(self, gender):
        if gender.lower() in list(Gender):
            raise Exception("Gender has to match Male/Female/Other")

        if not gender:
            raise Exception("ID Cannot be a Null Value")
        self._gender = gender

    ip_address = property(operator.attrgetter('_ip_address'))
    
    @ip_address.setter
    def ip_address(self, ip_address):
        if not re.match(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",ip_address):
            print(ip_address)
            raise Exception("Must be a valid IP address format")
            
        if not ip_address:
            raise Exception("ID Cannot be a Null Value")
        self._id = ip_address
```
5. Create methods to combine the `first_name` and `last_name` of the people object into `full_name()` method 
```
.
.
.
    def full_name(self):
        return self._first_name + " " + self._last_name
```
