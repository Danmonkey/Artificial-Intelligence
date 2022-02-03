"""Project 1 is the first project for the Artificial Intelligence class. It is intended to garner and demonstrate a
familiarity with the Python language. It parses a variety of data with respect to various states and CoViD-19.
Utilizing this data, it performs a variety of sorts and searches.


Author: James "Dan" O'Conner
Version: 2/4/2022
Email: n01058671@unf.edu
"""


class State:
    """
    State: A class that represents a State's collected data as a whole. A variety of parameters are included,
    each of which individually represents a specific data point. Contains a getter and setter for each parameter:
    Name, Capitol, Region, # of US House Seats, Population, # of Covid Cases, # of Covid deaths, vaccination rate,
    median household income, and violent crime rate. Also contains a greater than operator overload (for comparing by
    name) and a Str overload for returning the object as a string representation.
    """

    def __init__(self, countries):
        self.name = countries[0]
        self.cap = countries[1]
        self.reg = countries[2]
        self.seats = countries[3]
        self.pop = countries[4]
        self.ccases = countries[5]
        self.cdeaths = countries[6]
        self.fvr = countries[7]
        self.mhi = countries[8]
        self.vcr = countries[9]

    def get_name(self):
        return self.name

    def get_cap(self):
        return self.cap

    def get_reg(self):
        return self.reg

    def get_seats(self):
        return self.seats

    def get_pop(self):
        return self.pop

    def get_ccases(self):
        return self.ccases

    def get_cdeaths(self):
        return self.cdeaths

    def get_fvr(self):
        return self.fvr

    def get_mhi(self):
        return self.mhi

    def get_vcr(self):
        return self.vcr

    def set_name(self, name):
        self.name = name

    def set_cap(self, name):
        self.name = name

    def set_reg(self, name):
        self.name = name

    def set_seats(self, name):
        self.name = name

    def set_pop(self, name):
        self.name = name

    def set_ccases(self, name):
        self.name = name

    def set_cdeaths(self, name):
        self.name = name

    def set_fvr(self, name):
        self.name = name

    def set_mhi(self, name):
        self.name = name

    def set_vcr(self, name):
        self.name = name

    def __gt__(self, other):
        return self.get_name() > other.get_name()

    def __str__(self):
        return self.name + "    " + self.cap + "    " + self.reg + "    " + self.seats + "    " + self.pop + "    " + self.ccases + "    " + self.cdeaths + "    " + self.fvr + "    " + self.mhi + "    " + self.vcr


def sortbyname(countries):
    pass


def sortbycfr(countries):
    pass


def searchforname(countries, target, inorder):
    """
    Searches for a name among the State list using Binary Search if countries is sorted, or Sequential Search if it
    isn't.
    :param countries: A List containing State objects
    :param target: A String containing the name of the State we're looking for
    :param inorder: A Boolean which informs whether or not countries is sorted.
    :return: Returns the State object we're looking for, or None if we can't find it.
    """
    if inorder:
        high = countries.len() - 1
        low = 0
        mid = (high / 2)
        if countries[mid].get_name() == target:
            return countries[mid]
        while high > low:
            if countries[mid].get_name() == target:
                return countries[mid]
            elif countries[mid].get_name() > target:
                high = mid - 1
                mid = (high + low) / 2
            else:
                low = mid + 1
                mid = (high + low) / 2
        if countries[mid].get_name() == target:
            return countries[mid]
        else:
            return None
    else:
        for country in countries:
            if country.get_name() == target:
                return country
        return None


reader = open("States.csv", "r")
header = reader.readline().split()
Global = []
for x in reader:
    Global.append(State(x.split(",")))
issorted = False
