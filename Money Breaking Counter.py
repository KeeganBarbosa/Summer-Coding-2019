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
    if x<0:
        return 0
    if not CoinType:
        return 0
    else:
        y=max(CoinType)
        init = how_to_split_a(x,[c for c in CoinType if c<y])+ how_to_split_a(x-y,CoinType)
    return init


"""
This recursive code counts how many ways to give x change with CoinType coint types

The technique is to utilize recursion. 

The collection of all payment sets is in

a one to one correspondents with a strictly decreasing sequence gotten by ordering the set. This algorithm counts ordered sets.

The initial conditions are quite natural and are needed for the recursive process. 

The code works by first asking (for x>0) "is the largest coin in the sequence?", where it's weight is y. 

If yes, it suffices to count the descending sequences for x-y with the same coin list (i.e assume we already paid y).

If no, then throw that coin out of the list and restart the process with the new list of coins.

As this is a clear perfect partition, we can guarantee the accuracy of our results. 

"""

print(how_to_split_a(200,[1,2,5,10,20,50,100,200]))

