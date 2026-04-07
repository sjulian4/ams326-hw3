# Tossing a disc of diameter d to parralel
# lines of distance w = 1
# estimate the probability when
# any part of the disc crosses a parallel
# line for n = 4444444 tosses with the 
# disc diameters
# d = 1/10, 2/10, 3/10, 4/10, 5/10, 6/10, 7/10, 8/10, 9/10, 10/10, 15/10, 20/10, 30/10

# for d < w, you may cross no more than 1 line
#  and the crossing probability depends on d.

# for d > w, you may cross more than 1 line and, as such, you 
# must specify the probabilities for crossing at least 1-, 2-, 3-, 4-,... lines. 

# estimate and make a plot for the probabilities as a function of d.

# largest d value is 3, which can cross at most 4 lines at once (but this is very rare)
# so let's use 4+1 = 5 lines.
# y=0, y=1, y=2, y=3, y=4
# restrict domain to 0,4

import numpy as np
import matplotlib.pyplot as plt
import time

time1 = time.time()
n_tot = 4444444

prob_arr1 = np.zeros(13) # number of radii
prob_arr2 = np.zeros(13) 
prob_arr3 = np.zeros(13) 
prob_arr4 = np.zeros(13) 
counter = 0
d_arr = np.array([1/10, 2/10, 3/10, 4/10, 5/10, 6/10, 7/10, 8/10, 9/10, 10/10, 15/10, 20/10, 30/10])

for d in [1/10, 2/10, 3/10, 4/10, 5/10, 6/10, 7/10, 8/10, 9/10, 10/10, 15/10, 20/10, 30/10]: # loop over diameters
    temp_prob1 = 0.0
    temp_prob2 = 0.0
    temp_prob3 = 0.0
    temp_prob4 = 0.0


    
    for n in range(n_tot):
        y_0 = np.random.uniform(0.0, 4.0) # random y

        # (x-x0)^2 + (y-y0)^2 <= (d/2)^2
        if d < 1.0:
            for y in [0.0, 1.0, 2.0, 3.0, 4.0]: # see if disc intersects each line with the discrimiant
                if (d/2.0)**2 - (y-y_0)**2 >= 0: 
                    temp_prob1 += 1.0

        if d >= 1.0 and d < 2.0:
            crosses = 0
            for y in [0.0, 1.0, 2.0, 3.0, 4.0]: # see if disc intersects each line with the discrimiant
                if (d/2.0)**2 - (y-y_0)**2 >= 0: 
                    crosses += 1.0
            if crosses == 1.0:
                temp_prob1 += 1.0
            if crosses == 2.0:
                temp_prob2 += 1.0
                temp_prob1 += 1.0
        if d>=2.0 and d < 3.0:
            crosses = 0
            for y in [0.0, 1.0, 2.0, 3.0, 4.0]: # see if disc intersects each line with the discrimiant
                if (d/2.0)**2 - (y-y_0)**2 >= 0: 
                    crosses += 1.0
            if crosses == 1.0:
                temp_prob1 += 1.0
            if crosses == 2.0:
                temp_prob2 += 1.0
                temp_prob1 += 1.0
            if crosses == 3.0:
                temp_prob3 += 1.0
                temp_prob2 += 1.0
                temp_prob1 += 1.0
        if d >= 3.0:
            crosses = 0
            for y in [0.0, 1.0, 2.0, 3.0, 4.0]: # see if disc intersects each line with the discrimiant
                if (d/2.0)**2 - (y-y_0)**2 >= 0: 
                    crosses += 1.0
            if crosses == 1.0:
                temp_prob1 += 1.0
            if crosses == 2.0:
                temp_prob2 += 1.0
                temp_prob1 += 1.0
            if crosses == 3.0:
                temp_prob3 += 1.0
                temp_prob2 += 1.0
                temp_prob1 += 1.0
            if crosses == 4.0:
                temp_prob4 += 1.0
                temp_prob3 += 1.0
                temp_prob2 += 1.0
                temp_prob1 += 1.0

    prob_arr1[counter] = temp_prob1/n_tot
    prob_arr2[counter] = temp_prob2/n_tot
    prob_arr3[counter] = temp_prob3/n_tot
    prob_arr4[counter] = temp_prob4/n_tot
    counter += 1

time2 = time.time()
print(f"Time taken: {time2-time1:.2f} seconds")


# Plotting

plt.title("P(1 line) versus d")
plt.xlabel("d")
plt.ylabel("P(1 line)")
plt.scatter(d_arr, prob_arr1, label="Data", color='blue')
plt.plot(d_arr, prob_arr1, label="Trendline", color='red')
plt.savefig("problem1_probability_1_line.png")
plt.legend()
plt.clf()


plt.title("P(2 lines) versus d")
plt.xlabel("d")
plt.ylabel("P(2 lines)")
plt.scatter(d_arr, prob_arr2, label="Data", color='blue')
plt.plot(d_arr, prob_arr2, label="Trendline", color='red')
plt.savefig("problem1_probability_2_lines.png")
plt.legend()
plt.clf()

plt.title("P(3 lines) versus d")
plt.xlabel("d")
plt.ylabel("P(3 lines)")
plt.scatter(d_arr, prob_arr3, label="Data", color='blue')
plt.plot(d_arr, prob_arr3, label="Trendline", color='red')
plt.savefig("problem1_probability_3_lines.png")
plt.legend()
plt.clf()

plt.title("P(4 lines) versus d")
plt.xlabel("d")
plt.ylabel("P(4 lines)")
plt.scatter(d_arr, prob_arr4, label="Data", color='blue')
plt.plot(d_arr, prob_arr4, label="Trendline", color='red')
plt.savefig("problem1_probability_4_lines.png")
plt.legend()
plt.clf()

print("Plots saved as problem1_probability_1_line.png, problem1_probability_2_lines.png, problem1_probability_3_lines.png, problem1_probability_4_lines.png")
print(prob_arr1, prob_arr2, prob_arr3, prob_arr4)