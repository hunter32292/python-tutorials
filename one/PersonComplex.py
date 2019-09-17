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


    def full_name(self):
        return self._first_name + " " + self._last_name
