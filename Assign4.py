"""
******************************
CS 1026 - Assignment 4: Flights
Code by: Tudor Filimon
Student ID: tfilimon
File created: November 24, 2024
Assignment Due: December 6, 2024
******************************
This file is the central file of the program. It imports the Flight.py and Airport.py files to use their classes and methods.
It handles all the tasks of the program in relation to airports, flights, duration, and much more.
"""


# You must create the Flight.py and Airport.py files.
from Flight import *
from Airport import *

# Define your collections for all_airports and all_flights here.
all_airports = []
all_flights = {}

def load_data(airport_file, flight_file):
    try:
        airport_data = open(airport_file, "r")

        #extract infor from lines of airport
        #remove whitespace from ends, as well as parts of the line
        #extract info from each line and create an airport object for each
        #then add the object to the all_airports container

        for line in airport_data:
            #turn the line into parts
            line = line.strip()
            parts = line.split("-")

            #strip for internal whitespace in the parts
            code = parts[0].strip()
            country = parts[1].strip()
            city = parts[2].strip()

            #create objects of the Airport class
            airport_obj = Airport(code, city, country)

            #add flight object to all_airports container (whose key value is their code)
            all_airports.append(airport_obj)

        airport_data.close()

        #data from flight data
        flight_data = open(flight_file, "r")

        #extract info from each line and create flight object
        #remove white space again
        # when adding to all_flights dictionary, the key must be the origin airport code, and the value must be a list of the flight object(s) that depart from this origin airport

        for line in flight_data:
            line = line.strip()
            parts = line.rsplit("-", 3)

            for element in line:
                element.replace(" ", "")
                element.replace("\t","")

            #strip whitespace and divide into parts
            flight_no = parts[0].strip()
            origin_code = parts[1].strip()
            destination_code = parts[2].strip()
            duration = parts[3].strip()

            #Find the origin Airport object
            origin_airport = None
            for airport in all_airports:
                if airport.get_code() == origin_code:
                    origin_airport = airport
                    break #exit once found

            #Find destination Airport object
            destination_airport = None
            for airport in all_airports:
                if airport.get_code() == destination_code:
                    destination_airport = airport
                    break #exit once found

            #Skip this flight is an airport is missing
            if origin_airport is None or destination_airport is None:
                continue

            #Create a flight object to append to dictionary
            try:
                duration = float(duration)
            except ValueError:
                continue #skip if duration is not a valid number

            flight = Flight(flight_no, origin_airport, destination_airport, duration)

            #If the code doesn't already exist within the dictionary, make a new list for it
            #Then append the flight
            if origin_code not in all_flights:
                all_flights[origin_code] = []
            all_flights[origin_code].append(flight)

        flight_data.close()
        return True

    except Exception as e:
        return False

def get_airport_by_code(code):
    for airport in all_airports:
        if airport.get_code().upper() == code.upper():
            return airport

    #If no match is found, raise value error
    raise ValueError(f"No airport with the given code: {code}")


def find_all_city_flights(city):
    #Reutns a list of all flight objects that involve a given city as either their origin or destination
    city_flights = []

    #Iterate through all_flights dictionary
    for code in all_flights.items():
        for flight in code[1]:
            #Check if the city matches either the origin or destination locations of the flight
            if flight.get_origin().get_city() == city or flight.get_destination().get_city() == city:
                city_flights.append(flight)

    return city_flights

def find_all_country_flights(country):
    #Returns a list that contains flight objects that involve the given country either as the origin or destination
    country_flights = []

    #Iterate through the all flights dictionary by items
    for code in all_flights.items():
        for flight in code[1]:
            if flight.get_origin().get_country() == country or flight.get_destination().get_country() == country:
                country_flights.append(flight)

    return country_flights


def find_flight_between(orig_airport, dest_airport):
    #Check if there is a direct flight from origin airport to destination airport
    #Returns a string in the format "Direct Flight: orig_airport_code to dest_airport_code

    #Check for direct flight
    origin_code = orig_airport.get_code()
    destination_code = dest_airport.get_code()

    #Inital check for direct
    if origin_code in all_flights:
        for flight in all_flights[origin_code]:
            if flight.get_destination().get_code() == destination_code:
                return f"Direct Flight: {origin_code} to {destination_code}"

    #Check for single hop
    connecting_airports = set()
    if origin_code in all_flights.keys(): #gets the value at the code, in the flight dict
        for flight in all_flights[origin_code]: #makes flight the reference to the object at the value
            connecting_airport = flight.get_destination()
            connecting_code = connecting_airport.get_code()

            #Check to see if the connecting code exists in the all_flights dictionary
            if connecting_code in all_flights.keys():
                for conn_flight in all_flights[connecting_code]:
                    #conn_flight is not the potential connecting flight object,
                    #check to see if flights associated with this connecting code go to the destination airport
                    if conn_flight.get_destination() == dest_airport:
                        connecting_airports.add(connecting_airport.get_code())

    if connecting_airports:
        return connecting_airports

    #otherwise
    raise ValueError(f"There are no direct or single-hop connecting flights from {origin_code} to {destination_code}")

def shortest_flight_from(orig_airport):
    #Check if there are flights from the origin airport
    origin_code = orig_airport.get_code()
    if origin_code not in all_flights or not all_flights[origin_code]:
        raise ValueError(f"No flights found from {origin_code}")

    #set a reference value for comparison; set it to the first flight from this code
    shortest_flight = all_flights[origin_code][0] #can be indexed as it is a list

    #Compare flights going out from this airport code
    for flight in all_flights[origin_code]:
        #compare flight objects by duration
        if flight.get_duration() < shortest_flight.get_duration():
            shortest_flight = flight

    return shortest_flight

def find_return_flight(first_flight):
    #Get origin and destination codes for comparison later on
    origin_code = first_flight.get_origin().get_code()
    destination_code = first_flight.get_destination().get_code()

    #First check that the flight is valid--that is--if the destination airport exists
    if destination_code in all_flights:
        #goes into the list of flights departing from the airport at the destination code
        for flight in all_flights[destination_code]:
            #checks if the destination code of the flights departing are equivalent to the origin code of the original flight
            if flight.get_destination().get_code() == origin_code:
                return flight

    raise ValueError(f"There is no flight from {destination_code} to {origin_code}")


if __name__ == "__main__":
    pass