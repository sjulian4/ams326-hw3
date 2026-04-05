import numpy as np
from problem_2 import E

# calculating T value
x0 = np.random.uniform(0.0, 1.0)
y0 = np.random.uniform(0.0, 0.1)
a0 = np.random.uniform(0.0, np.pi/2)
average = 0.0
for i in range(100):
    x1 = x0 + np.random.uniform(-0.01, 0.01)
    y1 = y0 + np.random.uniform(-0.01, 0.01)
    a1 = a0 + np.random.uniform(-0.01, 0.01)
    average += abs(E(x1,y1,a1)- E(x0,y0,a0))
average = average/100
print("average T value:", average)
# 0.003591041788252627
# This will change depending on the run, but this is the first value I got.