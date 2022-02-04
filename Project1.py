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
        self.caserate = float(self.ccases)/float(self.pop)*100000
        self.deathrate = float(self.cdeaths)/float(self.pop)*100000
        self.cfr = float(self.cdeaths)/float(self.ccases)

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

    def widereport(self):
        print(f'{self.name:20}{self.mhi:10}{self.vcr:10.2}{round(self.cfr, 7):<.7}{self.caserate:^25.2f}{self.deathrate:13.2f}{self.fvr:>12}')

    def __gt__(self, other):
        return self.get_name() > other.get_name()

    def __str__(self):
        return f'{self.name:15}    {self.cap:20}    {self.reg:20}    {self.seats:15}    {self.pop:10}    {self.ccases:10}    {self.cdeaths:10}    {self.fvr:5}    {self.mhi:5}    {self.vcr:5}'


def sortbyname(countries, low, high):
    """
    The abstract part of quicksort. Sorts by repeatedly partioning, ascending alphabetically (I.E. lexically first
    names come first.)

    :param countries: A List that contains all the State objects.
    :param low: The bottom index. 0 from the outside.
    :param high: The top index. Len(countries)-1 from the outside.
    :return: None. All work is done directly on the List.
    """
    if low < high:
        part = partition(countries, low, high)
        sortbyname(countries, low, part - 1)
        sortbyname(countries, part + 1, high)


def sortbycfr(countries):
    pass


def partition(countries, low, high):
    """
    Partition sub-function for Quicksort. I copied this from my Data Structures project for quicksort and modified it
    :return Returns the partition point
    :type countries: List
    :param countries: List that contains the State objects
    :param low: the low value of the area to be partitioned
    :param high: the high value of the area to be partitioned
    """
    piv = countries[high]
    k = low - 1

    for j in range(low, high):
        if piv > countries[j]:
            k += 1
            temp = countries[k]
            countries[k] = countries[j]
            countries[j] = temp
    temp = countries[k+1]
    countries[k+1] = countries[high]
    countries[high] = temp
    return k + 1


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
        high = len(countries) - 1
        low = 0
        mid = int((high / 2))
        if countries[mid].get_name() == target:
            return countries[mid]
        while high > low:
            if countries[mid].get_name() == target:
                return countries[mid]
            elif countries[mid].get_name() > target:
                high = mid - 1
                mid = int((high + low) / 2)
            else:
                low = mid + 1
                mid = int((high + low) / 2)
        if countries[mid].get_name() == target:
            return countries[mid]
        else:
            return None
    else:
        for country in countries:
            if country.get_name() == target:
                return country
        return None


def wideprint(countries):
    """
    Prints the header, and then the rest of the list for the "option 1" report.
    :param countries: A List containing State objects.
    :return: None, as it prints directly to the console.
    """
    print(f'{"Name":20}{"MHI":10}{"VCR":10}{"CFR":13}{"Case Rate":^15}{"Death Rate":15}{"FVR"}')
    for f in countries:
        f.widereport()


reader = open("States.csv", "r")
reader.readline()
Countries = []
for x in reader:
    Countries.append(State(x.split(",")))
issorted = False
sortbyname(Countries, 0, len(Countries)-1)
wideprint(Countries)
