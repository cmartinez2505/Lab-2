"""
Program Name: Match Coins Game
Author: Chris Martinez
Purpose: This class represents a single coin that can be flipped.
Starter Code: N/A
Date: June 23, 2026
"""

import random

class Coin:
    def __init__(self):
        self.__sideup = "Heads"

    def toss(self):
        if random.randit(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"    

    def get_sideup(self):
        return self.__sideup
