#This class contains all needed items and tools for manipulating and analyze chinese dates

from datetime import datetime
from datetime import timedelta 

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
    example  = [[yand wood rat],[ox ying wood],
               [yang earth rooster],[yang fire tiger]]
    ********
    year                     [yand wood rat]

    ********
    month                    [ox ying wood]

    ********
    day                      [yang earth rooster]

    ********
    hour                     [yang fire tiger
    ********

    Chinese horoscope involves 60 combination of h.stems and e.branches
    Every cycle of year/month/day/hours equal 60.

    Cycle start with [yang wood rat]: yang wood is the first earthly
    branshes element. rat is the first heavenly stems element.
    second element in cycle eaual [heavenly_stems[1],earthly_branches[1]], etc

    """

    #len(earth_branches) = 10
    
    earth_branches = ("rat", "ox", "tiger", "rabbit", "dragon",
                      "snake", "horse", "sheep", "monkey", "rooster",
                      "dog", "pig")

   
    #len(heavenly_stems) = 12

    heavenly_stems = ("yang wood","ying wood","yang fire",
                      "ying fire","yang earth","ying earth",
                      "yang metal","ying metal","yang water","ying water")

    # method of Ppsckovskiy D.V.
    # moon status for date (B)
    # B = Bo + number of month + count of days
    # Bo = moon age  on 30Th November of last year
    # moon age of newmoon equal 0
    # {year in Methonic cycle : Bo}
    

    table_year = {0: 27, 1: 8, 2: 19, 3: 0, 4: 11, 5: 22, 6: 3, 7: 14,
                  8: 25, 9: 6, 10: 17,11: 28, 12: 9,13: 20,14: 2 ,15: 13,
                  16: 24, 17: 5,18: 16}

    #modify table contains 
    table_new = {0:"23:06 31/01/1919",  7 : "17:20 12/02/1926", 14 : "23:20 25/01/1933",
                 1:"21:34 19/02/1920",  8 : "08:54 2/02/1927",  15 : "00:43 14/02/1934",
                 2:"00:36 8/02/1921",   9 : "20:19 22/01/1928", 16 : "16:27 3/02/1935",
                 3:"23:48 27/01/1922", 10 : "17:55 9/02/1929",  17 : "07:18 24/01/1936",
                 4:"19:07 15/02/1923", 11 : "19:07 29/01/1930", 18 : "07:34 11/02/1937",
                 5:"01:38 5/02/1924",  12 : "13:10 17/02/1931",
                 6:"14:45 24/01/1925", 13 : "14:45 6/02/1932"}
                 
    
                

    
    heavtocycle = heavenly_stems * 6
    earthtocycle = earth_branches * 5
    comb_dict = {x:y for x,y in enumerate(zip(heavtocycle,earthtocycle))}


class Date(datetime, Cycle):

    def __init__(self, *kwrgs):
        super(Date, self).__init__(*kwrgs)

       

        #new cycle of year started in 1924
        self.start_year = 1924
        
        #new cycle of hours and days started in 16 dec 1923 23:00
        self.start_day = datetime(1923,12,16, 23, 0)
       

        #number of year in methonic cycle equal year % 19 
        self.methon = self.year % 19

        #moon age (B) by method of Ppsckovskiy D.V.
        #for every year in methonic cycle
        self.b = self.table_year[self.methon]

        self.wyear = datetime.strptime(self.table_new[self.methon], "%H:%M %d/%m/%Y")

        #very important thing timedelta for each cycle in methonic cycle
        
        self.delta = timedelta(0, 2952)

        #different between same years in methonic cycle 
        self.big_delta = timedelta(6939, 25368) 

    def __str__(self):
        a = (super(Date,self).__str__()).center(30)
        return "{0}\n{1:.<15}[{2}]\n{3:.<15}[{4}]\n{5:.<15}[{6}]\n{7:.<15}[{8}]\n".format(a,"year", self.convert_year(),"month",self.convert_month(),
                                                                           "day",self.convert_day(),"hour", self.convert_hour())
    
    def __repr__(self):
        if self.hour != 0  and self.minute != 0:
            
            lst = [self.convert_year(),self.convert_month(),
                   self.convert_day(), self.convert_hour()]
        else :
            lst = [self.convert_year(),self.convert_month(),
                   self.convert_day() ]
            
        lst = ["{0} {1}".format(x[0], x[1]) for x in lst ]
        a = super(Date,self).__repr__()

        return "{0}\n{1}".format(a,lst)
    
    def date_of_myear(self):
        """Return date of new moon year"""
        

        count_cycle = (self.year - self.wyear.year) / 19
       
        new_moon_year = self.wyear + count_cycle * (self.big_delta + self.delta)
        return new_moon_year
        
    def convert_year(self):
        """ Return chinese representation of year """

            

        if self.date_of_myear() <= self:
            num = (self.year - 1924) % 60
        else:
            num = ((self.year - 1924 -1) % 60) 
            
        

        return self.comb_dict[num]

    def num_of_index(self):
        """This function return the index of first moon month in self.comb_dict
           for a given year.For certain heavenly stems of year have certain index
           the first moon month
        """
        #heavenly stem of current year
        year = self.convert_year()[0]
        
        lst = [[(0,5),2],[(1,6),14],[(2,7), 26],
              [(3,8),38],[(4,9), 51]]
        for c in lst:
            if year == self.heavenly_stems[c[0][0]] or self.heavenly_stems[c[0][1]]:
                return c [1]
        """ 
            if year == self.heavenly_stems[0] or year == self.heavenly_stems[5]:
                indexa  = 2
            elif year  == self.heavenly_stems[1] or year == self.heavenly_stems[6]:
                indexa = 14
            elif year == self.heavenly_stems[2] or year == self.heavenly_stems[7]:
                indexa = 26
            elif year == self.heavenly_stems[3] or year == self.heavenly_stems[8]:
                indexa = 38
            elif year == self.heavenly_stems[4] or year == self.heavenly_stems[9]:
                indexa = 51
            return indexa
            """
             
    def convert_month(self):
        """ Return chinese representation of month """
        month_delta = timedelta(29.530588853)
         
        f = []
        for c in range(12):
            f.append(self.date_of_myear() + c * month_delta)
        
        
        month_index = filter(lambda x: self > x, f)
        
        
        if month_index :
            index = (self.num_of_index() + f.index(month_index[-1])) % 60
        else:
            index = (self.num_of_index() - 1) % 60
        
        return self.comb_dict[index]



    def convert_day(self):
        """ Return chinese representation of day """

        return self.comb_dict[(self - self.start_day).days % 60]

    def convert_hour(self):
        """ Return chinese representation of hour """

        delta = self - self.start_day

        delta = int((delta.total_seconds() / 3600) / 2) % 60

        return self.comb_dict[delta]
        







        
