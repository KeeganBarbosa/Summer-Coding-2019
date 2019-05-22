# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 19:23:14 2018

@author: Keegan Dasilva Barbosa

Project Euler Problem 15
"""
def lattice_paths_of_n(n,m):
    list2 = []
    my_list = []
    for i in range(1, n+2):
        list2.append(i)
    for i in range(1, m+2):
        my_list.append(list2)
    for i in range(0,m+1):
        for f in range(0,n+1):
            if f == 0 or i == 0:
                my_list[i][f] = 1
            else:
                my_list[i][f] = my_list[i-1][f]+my_list[i][f-1]
    return my_list[m][n]

"""
Lines 8-13 serves to construct a set indexed with ordered pairs called my_list.

The indices are points on a m by n lattice.

Lines 14-17 sets an initial condition my_list[0][0]=1.

This corresponds to there only being one way to not move on the lattice.

Line 19 is the recursive condition. To get to a point (i,f) in a lattice,
one must have either came from (i-1,f) or (i,f-1).
So, there are mylist[i-1][f] + mylist[i][f-1] ways to arrive at (i,f). 

Line 20 returns the number of lattice paths to (m,n) from the origin. 
"""

print(lattice_paths_of_n(20,20))
