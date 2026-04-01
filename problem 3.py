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
# shown above). (2) You may express the trajectory in a table or in a more-preferred curve. (