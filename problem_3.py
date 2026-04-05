# A flying plane at (a, 0) approaches an airport whose coordinates are (0, 0),
# which means the plan is a miles east to the airport. A steady south wind of speed w blows from south
# to north. While approaching the airport, the plane maintains a constant speed v0 relative to the wind
# and always maintains its heading directly toward the airport. It is interesting to construct the DE and
# find its solution as the plane’s trajectory.

# The plane’s velocity components relative to the airport tower are
# dx/dt = -v0 cos (alpha) = -v0 x/sqrt(x^2 + y^2)
# dy/dt = -v0 sin (alpha) = -v0 y/sqrt(x^2 + y^2) + w

# which is a system of two DEs with x and y are dependent variables and t independent variable. We are
# not interested in time so we may eliminate explicit dependence on time and build the following DE
# between x and y:
# dy/dx = y/x - k sqrt(1 + (y/x)^2) 
# y(x = a) = 0
# where k = w/v0

# Now, you are given the values a = 99.99, w = 44.44, and v0 = 88.88. Please use any one of the
# solution methods including the Euler’s methods and the Runge-Kutta methods to compute the plane’s
# trajectory until it lands at the airport.



# Notes: (1) A trajectory is an assembly of points in the xy-plane, or a function F(x, y) = 0, or a curve (as
# shown above). (2) You may express the trajectory in a table or in a more-preferred curve. 


# todo delete: difference is a is 99.99 
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.optimize import fsolve # make sure to install scipy

time1 = time.time()

v0=88.88
w=44.44
a=99.99
k = w/v0
h = -.01 # going from x = a > 0 to (x,y) = (0,0) so we take steps in the -x direction
x0 = a
y0 = 0.0
def f(x,y):
    return (y/x - k*np.sqrt(1 + (y/x)**2))

# forward euler method
x_list = [x0]
y_list = [y0]
while(x0>0.0):
    y0 = y0 + h*f(x0,y0)
    x0 = x0 + h
    if abs(y0) < 30.0: # prevent fivergence from x0 being small
        x_list.append(x0)
        y_list.append(y0)

plt.title("Trajectory of plane with Forward Euler method")
plt.xlabel("x (distance)")
plt.ylabel("y (distance)")
plt.plot(np.asarray(x_list), np.asarray(y_list))
plt.savefig("problem3_trajectory_forward_euler.png")
plt.clf()

time2 = time.time()
print("Time taken for forward Euler method at h = ", str(abs(h)), ": ", time2 - time1, " seconds")

# backward euler method
x0=a
y0=0.0
x_list = [x0]
y_list = [y0]

time1 = time.time()

while(x0+h>0.0):
    x0 = x0 + h
    def backeuler(y):
        return (y0 + h*f(x0,y) - y)
    y0 = fsolve(backeuler, y0)[0] # solves the implicit equation for y1, so the predicted next y-value
    if abs(y0) < 30.0: # prevent divergence from x0 being small
        x_list.append(x0)
        y_list.append(y0)

plt.title("Trajectory of plane with backward Euler method")
plt.xlabel("x (distance)")
plt.ylabel("y (distance)")
plt.plot(np.asarray(x_list), np.asarray(y_list))
plt.savefig("problem3_trajectory_backward_euler.png")
plt.clf()

time2 = time.time()
print("Time taken for backward Euler method at h = ", str(abs(h)), ": ", time2 - time1, " seconds")

# explicit midpoint method
time1 = time.time()

x0=a
y0=0.0
x_list = [x0]
y_list = [y0]

while(x0+h/2>0.0):
    y0=y0 + h*f(x0 + h/2, y0 + (h/2)*f(x0,y0))
    x0 = x0 + h
    if abs(y0) < 30.0: # prevent divergence from x0 being small
        x_list.append(x0)
        y_list.append(y0)

plt.title("Trajectory of plane with explicit midpoint method")
plt.xlabel("x (distance)")
plt.ylabel("y (distance)")
plt.plot(np.asarray(x_list), np.asarray(y_list))
plt.savefig("problem3_trajectory_explicit_midpoint.png")
plt.clf()

time2 = time.time()
print("Time taken for explicit midpoint method at h = ", str(abs(h)), ": ", time2 - time1, " seconds")


# implicit midpoint method
time1 = time.time()
x0=a
y0=0.0
x_list = [x0]
y_list = [y0]

while(x0+h/2>0.0):
    x0 = x0 + h
    def implicitmidpoint(y):
        return (y0 + h*f(x0 + h/2, y) - y)
    y0 = fsolve(implicitmidpoint, y0)[0] # solves the implicit equation for y1, so the predicted next y-value
    x0 = x0 + h
    if abs(y0) < 30.0: # prevent divergence from x0 being small
        x_list.append(x0)
        y_list.append(y0)

plt.title("Trajectory of plane with implicit midpoint method")
plt.xlabel("x (distance)")
plt.ylabel("y (distance)")
plt.plot(np.asarray(x_list), np.asarray(y_list))
plt.savefig("problem3_trajectory_implicit_midpoint.png")
plt.clf()

time2 = time.time()
print("Time taken for implicit midpoint method at h = ", str(abs(h)), ": ", time2 - time1, " seconds")


# Heun's method
time1 = time.time()
x0=a
y0=0.0
x_list = [x0]
y_list = [y0]

while(x0+h>0.0):
    y0 = y0 + h/2*(f(x0,y0) + f(x0+h, y0 + h*f(x0,y0)))
    x0 = x0 + h
    if abs(y0) < 30.0: # prevent divergence from x0 being small
        x_list.append(x0)
        y_list.append(y0)

plt.title("Trajectory of plane with Heun's method")
plt.xlabel("x (distance)")
plt.ylabel("y (distance)")
plt.plot(np.asarray(x_list), np.asarray(y_list))
plt.savefig("problem3_trajectory_heuns.png")
plt.clf()

time2 = time.time()
print("Time taken for Heun's method at h = ", str(abs(h)), ": ", time2 - time1, " seconds")

# Runge-Kutta RK3 method
time1 = time.time()
x0=a
y0=0.0
x_list = [x0]
y_list = [y0]

while(x0+h>0.0):
    k1 = f(x0,y0)
    k2 = f(x0 + h/2, y0 + (h/2)*k1)
    k3 = f(x0 + h, y0 - h*k1 + 2*h*k2)
    y0 = y0 + h/6*(k1 + 4*k2 + k3)
    x0 = x0 + h
    if abs(y0) < 30.0: # prevent divergence from x0 being small
        x_list.append(x0)
        y_list.append(y0)

plt.title("Trajectory of plane with RK3 method")
plt.xlabel("x (distance)")
plt.ylabel("y (distance)")
plt.plot(np.asarray(x_list), np.asarray(y_list))
plt.savefig("problem3_trajectory_RK3.png")
plt.clf()

time2 = time.time()
print("Time taken for RK3 method at h = ", str(abs(h)), ": ", time2 - time1, " seconds")

# Runge-Kutta RK4 method
time1 = time.time()
x0=a
y0=0.0
x_list = [x0]
y_list = [y0]

while(x0+h>0.0):
    k1 = f(x0,y0)
    k2 = f(x0 + h/2, y0 + (h/2)*k1)
    k3 = f(x0 + h/2, y0 + (h/2)*k2)
    k4 = f(x0 + h, y0 + h*k3)
    y0 = y0 + h/6*(k1 + 2*k2 + 2*k3 + k4)
    x0 = x0 + h
    if abs(y0) < 30.0: # prevent divergence from x0 being small
        x_list.append(x0)
        y_list.append(y0)

plt.title("Trajectory of plane with RK4 method")
plt.xlabel("x (distance)")
plt.ylabel("y (distance)")
plt.plot(np.asarray(x_list), np.asarray(y_list))
plt.savefig("problem3_trajectory_RK4.png")
plt.clf()

time2 = time.time()
print("Time taken for RK4 method at h = ", str(abs(h)), ": ", time2 - time1, " seconds")

