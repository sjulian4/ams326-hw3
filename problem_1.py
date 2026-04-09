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

for d in d_arr: # loop over diameters
   
    r = d / 2.0

    y_centers = np.random.uniform(0.0, 4.0, n_tot)
        
    crosses = np.zeros(n_tot)
    
    # check every line against all 4.4 million centers simultaneously
    for y_line in [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0]:
        # This adds 1 to the 'crosses' count for any disc that intersects this line
        crosses += (r**2 - (y_line - y_centers)**2 >= 0)
        
    # 4. Count how many tosses crossed at least 1, 2, 3, or 4 lines
    prob_arr1[counter] = np.sum(crosses >= 1) / n_tot
    prob_arr2[counter] = np.sum(crosses >= 2) / n_tot
    prob_arr3[counter] = np.sum(crosses >= 3) / n_tot
    prob_arr4[counter] = np.sum(crosses >= 4) / n_tot
    
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