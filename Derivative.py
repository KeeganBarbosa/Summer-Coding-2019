# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:10:28 2019

@author: Owner
"""
import numpy as np

import sympy as sy

import scipy.interpolate

import math

from scipy.misc import derivative

def f(x):
    return 1/((1-x)*(1-x**5)*(1-x**10)*(1-x**25)*(1-x**100 ))


def appf(x):
    return scipy.interpolate.approximate_taylor_polynomial(f,x,5,0.1,order=None)



ans = sy.diff(lambda x: (1/((1-x)*(1-(x**5))*(1-(x**10))*(1-(x**25))*(1-(x**100)))) ,0 )

print(ans)

