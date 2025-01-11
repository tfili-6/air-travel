"""
******************************
CS 1026 - Assignment 4: Flights
Code by: Tudor Filimon
Student ID: tfilimon
File created: November 24, 2024
Assignment Due: December 6, 2024
******************************
This file is used to create the Flight class and all of its corresponding methods.
This file will then be imported to Assign4.py, the main file, to be used when running the program
"""


from Airport import *

class Flight:
    def __init__(self, flight_no, origin, dest, dur):
        #check if origin and destination are airport objects, otherwise use TypeError
        if not isinstance(origin, Airport) or not isinstance(dest, Airport):
            raise TypeError("The origin and destination must be Airport objects")

        #otherwise, proceed to initialization
        #initalization constructor: make these properties of the flight class for the object to reference
        self._flight_no = flight_no
        self._origin = origin
        self._destination = dest
        self._duration = dur

    def __str__(self):
        #return the string representation of the Flight containing the origin city, destination city,
        #duration (rounded to the nearest int), and an indication of whether the flight is domestic/international
        #following format: origin_city to dest_city (dur) [domestic/international]
        #ie: Toronto to Montreal (1h) [domestic]
        #ie: Toronto to Chicago (3h) [international]
        duration = round(self._duration)

        #Is domestic
        if self.is_domestic():
            return f"{self._origin.get_city()} to {self._destination.get_city()} ({duration}h) [domestic]"
        #Is international
        else:
            return f"{self._origin.get_city()} to {self._destination.get_city()} ({duration}h) [international]"

    def __eq__(self, other):
        #return true if self flight is considered the same as other
        #basically,if the origin and
        #destination are the same for both Flights. If "other" variable is not a Flight object,
        #it must also return False since Flight and non-Flight objects cannot be compared.

        if isinstance(other, Flight):
            if self._origin == other.get_origin() and self._destination == other.get_destination():
                return True
            else:
                return False
        else:
            return False

    def __add__(self, conn_flight):
        #Check if conn_flight is a Flight object. If it is not, raise a TypeError to indicate that
        # it cannot be added to a Flight. This exception should contain the text “The
        # connecting_flight must be a Flight object”.
        # o If it is a Flight object, then check if the destination of the 'self' Flight is the same
        # Airport as the origin of the 'conn_flight' Airport (i.e. one Flight ends and the next
        # Flight begins in the same Airport). If not, raise a ValueError with the text “These
        # flights cannot be combined” to indicate that these 2 Flight objects cannot be
        # combined.
        # o If they can be combined, then return a new Flight object with the origin set to
        # self._origin, the destination set to conn_flight._destination, the duration set to
        # the sum of the durations of both flights, and flight_no being equal to
        # self._flight_no.
        #check if the connecting flight is not a flight object
        if not isinstance(conn_flight, Flight):
            raise TypeError("The connecting_flight must be a Flight object")

        #if no error is raised, proceed
        if self._destination == conn_flight.get_origin():
            dur1 = self._duration
            dur2 = conn_flight.get_duration()

            dur_tot = dur1 + dur2

            combined_flight = Flight(self._flight_no, self._origin, conn_flight._destination, dur_tot)
            return combined_flight

        else:
            raise ValueError("These flights cannot be combined")

    def get_flight_no(self):
        #getter that returns the flight number code
        return self._flight_no

    def get_origin(self):
        #getter that returns the flight origin
        return self._origin

    def get_destination(self):
        #getter that returns the flight destination
        return self._destination

    def get_duration(self):
        #getter that returns the flight duration
        return self._duration

    def is_domestic(self):
        #method that returns true if the flight is domestic (origin and destination are in the same country)
        #returns false if the origin and destination are in different countries
        ori_country = self._origin.get_country()
        dest_country = self._destination.get_country()

        if ori_country == dest_country:
            return True
        else:
            return False

    def set_origin(self, origin):
        #setter that updates the flight origin
        self._origin = origin

    def set_destination(self, destination):
        #setter that sets/updates the Flight destination
        self._destination = destination








