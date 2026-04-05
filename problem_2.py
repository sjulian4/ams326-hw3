# r = sin2theta
# (x^2 + y^2)^3 = 4x^2y^2

# Please write a program to enable you to place a rectangular cutter (as shown) of sides 1 × 1/√2
# to cut the most area of the rose. You are suggested to start from a random spot for the cuts.


# the rose is fully contained in a box
# [-1,1] for x and [-1,1] for y

# rose has symmetry 4-fold, rectangular cutter has 2-fold symmetry
# consider rotation angles in [0, pi/2]

# want to maximize area cut out - same as minimizing -area

import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.optimize import fsolve # make sure to install scipy


time1 = time.time()

n_tot = 12000 # number of iterations
sqrt2 = np.sqrt(2.0)

def E(x,y, a): # a function for the area cut by the cutting rectangle
    ns = np.array([np.sin(a), np.cos(a)]) # short side direction vector
    nl = np.array([ns[1], -ns[0]]) # long side direction vector
    # determine area inside both rose and cutter
    # divide cutter into a grid of many small rectangles and see if
    # the center of each square is inside the rose
    center = np.array([x,y])
    vertex1 = -0.5*nl + (-0.5/sqrt2)*ns + center

    num_points = 200
    nl_range = np.linspace(0.0, 1.0, num_points + 1)
    ns_range = np.linspace(0.0, 1.0/sqrt2, num_points + 1)
    step_size_long = abs(nl_range[1] - nl_range[0])
    step_size_short = abs(ns_range[1] - ns_range[0])
    area = 0.0
    for i in range(num_points):
        for j in range(num_points):
            point = vertex1 + (-0.5*step_size_short*ns + 0.5*step_size_long*nl) - i*step_size_short*ns + j*step_size_long*nl
            if np.sqrt(point[0]**2 + point[1]**2) < np.sin(2.0*np.arctan(abs(point[1]/point[0]))): # if point is in rose

                area += step_size_long*step_size_short # add area if center is in rose
    return -area

# x0 = np.random.uniform(0.0, 1.0) # initial center of rect
# y0 = np.random.uniform(0.0, 1.0)
# a0 = np.random.uniform(0.0, np.pi/2) # initial angle of rotation of cutter

x0 = -0.012865667563016294 # initial center of rect
y0 = 0.7265934431767387
a0 = -0.07714424868270725 # initial angle of rotation of cutter

T = 0.003591041788252627 # Temperature, from problem_2_calculations.py

for n in range(n_tot):
    # propose new state
    x1 = x0 + np.random.uniform(-0.01, 0.01)
    y1 = y0 + np.random.uniform(-0.01, 0.01)
    a1 = a0 + np.random.uniform(-0.01, 0.01)
    if(n == 0):
        E_old = E(x0,y0,a0)
    E_new = E(x1,y1,a1)
    prob = min(np.exp(-(E_new - E_old)/T), 1.0) # acceptance probability
    random_number = np.random.uniform(0.0, 1.0)
    if(random_number < prob): # accept new state with probability
        x0 = x1
        y0 = y1
        a0 = a1
        E_old = E_new

time2 = time.time()

print("The optimal set of parameters is: x = ", x0, " y = ", y0, " a = ", a0)
print("The maximum area cut out is: ", -E(x0,y0,a0))
print("Time taken: ", time2 - time1, " seconds")

print(-E(0.1,0,0))
print(-E(0.0,0.0,0.0))

# Output after first run replacing the random generated T with the calculated T from problem_2_calculations.py:
# The optimal set of parameters is: x =  -0.012865667563016294  y =  0.7265934431767387  a =  -0.07714424868270725
# The maximum area cut out  is:  0.5840878789293876
# Time taken:  1619.6811063289642  seconds
# 0.24312098904153265
# 0.24168909780962894
# Now, I will replace the randomly generated x y and a initial values with those found above.

# After running with those replacements: 
# The optimal set of parameters is: x =  0.17078966171868137  y =  0.6942535877704037  a =  0.20424918479565352
# The maximum area cut out  is:  0.5773880421776512
# Time taken:  1619.467227935791  seconds
# 0.24312098904153265
# 0.24168909780962894
# This max area is smaller. 

# Trying more iterations:

