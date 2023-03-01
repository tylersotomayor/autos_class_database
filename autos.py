"""
Future program improvements:

Add a method for adding new car objects to the autos_list.
    This method should take in the attributes of a new car and create a new Autos object with those attributes.
Add a method for removing car objects from the autos_list.
    This method should take in a VIN number and remove the corresponding Autos object from the list.
Add a method for searching for car objects in the autos_list.
    This method should take in some search criteria (e.g. make, model, year) and return a list of Autos objects
    that match the criteria.
Add a method for persisting the autos_list to a file or database.
    This method should be called when the program exits to save any changes made to the autos_list.
    You could use a simple file format like CSV or JSON to store the data.
Add a method for loading the autos_list from a file or database when the program starts up.
    This method should be called at the beginning of the program to load any previously saved data.
Add more methods for manipulating and analyzing the autos_list, such as calculating average fuel economy or
    finding the most expensive car. Overall, your autos.py module is a good starting point for building a simple car
    database, but there is a lot more functionality that could be added to make it more useful.
"""


class Autos:
    autos_list = []

    def __init__(self, vin, make, model, year, fuel_economy, price):
        self.set_vin(vin)
        self.set_make(make)
        self.set_model(model)
        self.set_year(year)
        self.set_fuel_economy(fuel_economy)
        self.set_price(price)

        Autos.autos_list.append(self)

    def __str__(self):
        return f"VIN: {self.get_vin()}, Make: {self.get_make()}, Model: {self.get_model()}, Year: {self.get_year()}, " \
               f"Fuel Economy: {self.get_fuel_economy()} MPG, Price: {self.get_price()}"

    def set_vin(self, vin):
        if not isinstance(vin, str) or len(vin) != 17 or not vin.isalnum():
            raise ValueError("Invalid vin. It must be a 17 character alphanumeric string.")
        self._vin = vin

    def get_vin(self):
        return self._vin

    def set_make(self, make):
        if not isinstance(make, str):
            raise ValueError("Invalid make. It must be a string.")
        self._make = make

    def get_make(self):
        return self._make

    def set_model(self, model):
        if not isinstance(model, str):
            raise ValueError("Invalid model. It must be a string.")
        self._model = model

    def get_model(self):
        return self._model

    def set_year(self, year):
        if not isinstance(year, int):
            raise ValueError("Invalid year. It must be an integer.")
        self._year = year

    def get_year(self):
        return self._year

    def set_fuel_economy(self, fuel_economy):
        if not isinstance(fuel_economy, float):
            raise ValueError("Invalid fuel economy. It must be a float.")
        self._fuel_economy = fuel_economy

    def get_fuel_economy(self):
        return self._fuel_economy

    def set_price(self, price):
        if not isinstance(price, float):
            raise ValueError("Invalid price. It must be a float.")
        self._price = price

    def get_price(self):
        return self._price

    @classmethod
    def get_autos_list(cls):
        return cls.autos_list
