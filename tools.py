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
    example year = yand wood
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

    heavtocycle = heavenly_stems * 5
    earthtocycle = earth_branches * 6
    comb_dict = {x:y for x,y in enumerate(zip(heavtocycle,earthtocycle))}

class A(datetime):
    pass
