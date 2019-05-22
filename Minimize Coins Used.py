# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:56:40 2019

@author: Owner
"""

def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

"""
This code was gotten from https://interactivepython.org/courselib/static/pythonds/Recursion/DynamicProgramming.html

It solves the coin problem via dynamic programming and lowers the number of calls the recursive process needs to make. 

The basic component of the algorithm is to first check if the amount of change can already be paid for with a single coin.

If not, it runs the process again, this time checking for what happens if we have already paid with a coin of each type from coinValueList

KnownResults keeps track of all payment methods possible thus far and stops the search for payment methods that are already suboptimal.
"""

print(recDC([1,5,10,25], 63, [0]*64))