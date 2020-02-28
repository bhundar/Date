import numpy

class Date(object):
    """
    This is a class for mathematical operations on calendar dates 
    (from the Gregorian calendar).
    """
    jdn = 0
    # These methods go back and forth between day/month/year and Julian Day Number
    # note the use of integer division //
    @staticmethod
    def JulianDate(day, month, year):
        """
        Converts a date expressed as day, month, year 
        into a Julian day number
        
        Args:
            day (int): day numbered 1-31
            month (int): month 1-12
            year (int): year
        
        Returns:
            int: Julian Day Number
        """

        a = (14 - month) // 12
        y = year + 4800 - a
        m = month + 12 * a - 3
        return (day + (153 * m + 2) // 5 + 365 * y + (y // 4) - (y // 100) + (
            y // 400) - 32045)

    @staticmethod
    def CalendarDate(JDN):

        a = JDN + 32044
        b = (4 * a + 3) // 146097
        c = a - (146097 * b) // 4
        d = (4 * c + 3) // 1461
        e = c - (1461 * d) // 4
        m = (5 * e + 2) // 153
        day = e - ((153 * m + 2) // 5) + 1
        month = m + 3 - 12 * (m // 10)
        year = 100 * b + d - 4800 + (m // 10)
        
        return day, month, year
    
    # class variables that you will need below
    month_names = [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
        ]
    
    day_names = [
            "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday"
        ]

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.jdn = self.JulianDate(self.day, self.month, self.year)
        
    def __str__(self):
        # Convert date to Julian Date first
        jdn = self.JulianDate(self.day, self.month, self.year)
        # Calculate weekday
        weekDay = numpy.mod(jdn+1,7)
        return self.day_names[weekDay] + ' ' + str(self.day) + ' ' + self.month_names[self.month - 1] + ' ' + str(self.year)
        
    def __add__(self, other):
        day1 = self.JulianDate(self.day, self.month, self.year)
        newDay1 = self.CalendarDate(day1+other)
        return Date(newDay1[0], newDay1[1], newDay1[2])
        
    def __sub__(self, other):
        # Convert both Date objects to Julian Date and then subtract
        date1 = self.JulianDate(self.day, self.month, self.year)
        date2 = other.JulianDate(other.day, other.month, other.year)
        return numpy.abs(date1-date2)

today = Date(22,1,2020)
print("Today,",today,"has Julian Day number", today.jdn)

tomorrow = today + 1
print("Tomorrow will be",str(tomorrow)+".")
print("There is",tomorrow-today,"day between tomorrow and today.")

leafs_cup=Date(2,5,1967)
print("The Toronto Maple Leafs last won the Stanley Cup on", leafs_cup,".")
print("It has been", today-leafs_cup,"days since then ....")


birthDate = Date(19,9,1996)
print("I am",birthDate-today, "days old today.")

# Set up up initial counter to 1000 and have it iterate till it reaches 30000
counter = 1000
while (counter <= 30000):
    print(birthDate + counter)
    # Increment counter by 1000
    counter += 1000

class AmericanDate(Date):
    """
    This is a derived class of the Date class.
    """
    def ___init__(self, day, month, year):
        super().__init__(day, month, year)
    
    def __str__(self):
        jdn = self.JulianDate(self.day, self.month, self.year)
        weekDay = numpy.mod(jdn+1,7)
        return self.day_names[weekDay] + ' ' + self.month_names[self.month - 1] + ' '+ str(self.day) + ', ' + str(self.year)

independence_day = AmericanDate(4,7,1776)
print(independence_day)