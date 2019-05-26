# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:56:40 2019

@author: Keegan Dasilva Barbosa

Project Euler Question 31
"""

def how_to_split_a(x,CoinType):
    init=0
    if x == 0:
        return 1
    else:
        for c in [c for c in CoinType if c<=x]:
            init =init+ how_to_split_a(x-c,CoinType)
    return init


"""
This recursive code counts how many ways to give x change with CoinType coint types

Note, order matters for this code. That is, paying with a quarter and a dime is different from paying with a dime and a quarter.
"""

print(how_to_split_a(25,[1,5,10,25,100]))
