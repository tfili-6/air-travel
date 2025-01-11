"""
******************************
CS 1026 - Assignment 4: Flights
Code by: Tudor Filimon
Student ID: tfilimon
File created: November 24, 2024
Assignment Due: December 6, 2024
******************************
This file is used to create the Airport class and all of its corresponding methods.
This file will then be imported to Assign4.py and Flight.py to be used when running the program.
"""


class Airport:
    def __init__(self, code, city, country):
        #initialize instance attributes _code, _city, _country,
        #based on corresponding parameters in the constructor
        self._code = code
        self._city = city
        self._country = country

    def __str__(self):
        #return the string representation in the airport in the following
        #format: code(city country) ie: YYZ(Toronto, Canada)
        return f"{self._code} ({self._city}, {self._country})"

    def __eq__(self, other):
        #Return true if self and other are considered the same airport
        #basically, if the 3 letter code is the same for both airports
        if not isinstance(other, Airport):
            return False
        else:
            return self._code == other.get_code()
        #if other variable is not an Airport object, it must also return false since
        #since airport and non-airport objects cannot be compared
        #hint: use isinstance operator

    def get_code(self):
        #getter function that returns the airport code
        return self._code

    def get_city(self):
        #gettter function that returns the airport city
        return self._city

    def get_country(self):
        #return the country of the Airport
        return self._country

    def set_city(self, city):
        #setter that sets (updates) the Airport city
        self._city = city

    def set_country(self, country):
        #setter that sets (updates) the Airport country
        self._country = country

