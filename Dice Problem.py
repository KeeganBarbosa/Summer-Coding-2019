# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:14:45 2019

@author: Keegan Dasilva Barbosa

Project Euler Question 205
"""

import numpy as np


def f(x):
    if x<1:
        return 0
    if x>4:
        return 0
    else:
        return 0.25
    

def g(x):
    if x<1:
        return 0
    if x>6:
        return 0
    else:
        return 1/6

f_1=[]
g_1=[]
for i in range(1,5):
    f_1.append(f(i))
for i in range(1,7):    
    g_1.append(g(i))
    

"""
We start by defining the probability distribution function for each die. Then, we construct an array for the support of the variables.

As the support is finite, we need not worry about approximations, we can compute the array explicitely.

In comment, we refer to the random variables for 6 6-dice rolls as Y and 9 4-dice rolls is X.
"""


f_2= np.convolve(f_1,f_1)


f_4= np.convolve(f_2,f_2)

f_8= np.convolve(f_4,f_4)

f_9= np.convolve(f_8,f_1)

g_2= np.convolve(g_1,g_1)

g_4 = np.convolve(g_2,g_2)

g_6 = np.convolve(g_4,g_2)

final= np.convolve(g_6,f_9)


"""
We then compute the distribution for 9 dice rolls and 6 dice rolls. The distribution for the sum of two random variables is
simply the convolution. Hence, we can compute the probability distribution for 9 4-dice rolls and 6 6-dice rolls.

Since the distributions are symmetric, the distribution for the negative 6 6-dicerolls is the same as the positive distribution.

Hence, the distribution for X-Y is final.
"""

init=0

for i in range(0,30):
    init += final[i]
    
 
"""
One can chech that final is an array with length 58. To get the probability X-Y >= 1, it suffices to add the first 29 terms i.e 
integrate the distribution over -infty to 1 (recall we want the negative bit as we did not factor in the negative).

"""    
    
print(init)