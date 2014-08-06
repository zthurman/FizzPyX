#!/usr/bin/env python
#  Eventually I'd like to create an application that provides a nice intuitive GUI that enables the user to #manipulate different models of differential equations to exhibit different behaviors given different input #parameters.

from __future__ import division
from scipy import *
import numpy as np
import pylab
import matplotlib as mp
from matplotlib import pyplot as plt  
import sys
import math as mt

# First we need to come up with a class that will be general enough to encompass all of the neuron models

class Neuron:
	params = []
	def model(eqns,params):
		

	def solver():

#  The following is an excerpt from HindmarshRose, something along these lines would be a nice and clean way to do the
# general neuron.

"""def generate(data_length, odes, state, parameters):
    data = np.zeros([state.shape[0], data_length])

    for i in xrange(1):
        state = rk4(odes, state, parameters)

    for i in xrange(data_length):
        state = rk4(odes, state, parameters)
        data[:, i] = state

    return data

def rk4(odes, state, parameters, dt=0.01):
    k1 = dt * odes(state, parameters)
    k2 = dt * odes(state + 0.5 * k1, parameters)
    k3 = dt * odes(state + 0.5 * k2, parameters)
    k4 = dt * odes(state + k3, parameters)
    return state + (k1 + 2 * k2 + 2 * k3 + k4) / 6

def HR_odes((x,y,z), (a, b, c, d, r, s, I, xnot)):
    return np.array([y - a*(x**3) + (b*(x**2)) - z + I, \
                        c - d*(x**2) - y, \
                        r*(s*(x - xnot) - z)])

def HR_generate(data_length):
    return generate(data_length, HR_odes, \
            np.array([3.0, 0, -1.2]), np.array([1.0, 3.0, 1.0, 5.0, 0.006, 4.0, 1.3, -1.5]))"""
