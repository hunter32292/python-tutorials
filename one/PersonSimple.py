class People(object):

    def __init__(self, id_num, city, last_name, first_name, gender, ip_address):
        self.id_num = id_num
        self.city = city
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.ip_address = ip_address

    def full_name(self):
        return self._first_name + " " + self._last_name