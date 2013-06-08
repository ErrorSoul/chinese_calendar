#This class contains all needed items and tools for manipulating and analyze chinese dates

from datetime import datetime


class Cycle(object):
    """Class make and contain dictionary for all possibly combination with
    heavenly stems and earth branches 
    Chinese date have  4 elements:
    -year 
    -month
    -day
    -hour 
    Each date element equal some combination heavenly stems and earth branches
    date in west world = 1.01.1901
    date in chinese world = (year)[heavenly stems][earth branch](month)......
    example year = yand wood rat
    ********

    Chinese horoscope involves 60 combination of h.stems and e.branches
    Every cycle of year/month/day/hours equal 60.

    """

    #len(heavenly_stems) = 12
    #len(earth_branches) = 10
    heavenly_stems = ("rat", "ox", "tiger", "rabbit", "dragon",
                      "snake", "horse", "sheep", "monkey", "rooster",
                      "dog", "pig")
    earth_branches = ("yang wood","ying wood","yang fire",
                      "ying fire","yang earth","ying earth",
                      "yang metal","ying metal","yang water","ying water")

    # method of Ppsckovskiy D.V.
    # moon status 
    table_year = {0: 27, 1: 8, 2: 19, 3: 0, 4: 11, 5: 22, 6: 3, 7: 14,
                  8: 25, 9: 6, 10: 17,11: 28, 12: 9,13: 20,14: 2,15: 13,
                  16: 24, 17: 5,18: 16}


    heavtocycle = heavenly_stems * 5
    earthtocycle = earth_branches * 6
    comb_dict = {x:y for x,y in enumerate(zip(heavtocycle,earthtocycle))}


class Date(datetime, Cycle):

    def __init__(self, *kwrgs):
        super(Date, self).__init__(*kwrgs)

        #new cycle of days started 17 dec 1923
        self.start_day = datetime(1923, 12, 17)

        #new cycle of year started in 1924
        self.start_year = 1924
        
        #new cycle of hours started in 16 dec 1923 23:00
        self.start_hour = datetime(1923,12,16, 23, 0)
        

    def convert_year(self):
        """ Return chinese representation of year """

        return self.comb_dict[(self.year - 1924) % 60]

    def convert_month(self):
        """ Return chinese representation of month """

        pass

    def convert_day(self):
        """ Return chinese representation of day """

        return self.comb_dict[(self - self.start_day).days % 60]

    def convert_hour(self):
        """ Return chinese representation of hour """

        delta = self - self.start_hour

        delta = int((delta / 3600) / 2) % 60

        return self.comb_dict[delta]
        
    def f(self):
        print self.convert_day(),self.convert_year()
        




        

        
    




        
