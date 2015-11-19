import numpy as np
from numpy import random
from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten, kmeans2
import matplotlib.pyplot as plt

# ## -----Test One-----
# test_data = np.zeros((40000, 4))
# test_data[0:10000, :] = 30.0
# test_data[10000:20000, :] = 60.0
# test_data[20000:30000, :] = 90.0
# test_data[30000:, :] = 120.0
# # whiten_data = whiten(test_data);
# result = kmeans(test_data, 4);
# print result;

## -----Test Two-----
## Generate Testing Data
test_data = np.zeros((40, 2))
for i in range (len(test_data)) :
	test_data[i, 0] = 20. * (i / 10) + 10 * np.random.random();
	test_data[i, 1] = 20. * (i / 10) + 10 * np.random.random();
print test_data;

# ## by setting random.seed, the result will be the same each time
# random.seed((1000,2000));

whiten_data = whiten(test_data);
# print whiten_data;

# ## Run with random initialization
# result = kmeans2(whiten_data, 4);
# result = kmeans2(test_data, 4);

# ## Run with manual initialization
book = array ((whiten_data[5], whiten_data[15], whiten_data[25], whiten_data[35]));
result = kmeans2(whiten_data, book);
# book = array ((test_data[5], test_data[15], test_data[25], test_data[35]));
# result = kmeans2(test_data, book);
print result;

## Plotting
# Defin colors
COLOR_MAP = ['#FF2121' ,'#FF8936' ,'#00BC12' ,'#424C50' ,'#065279' ,'#574266' ,'#CCA4E3' ,'#F3D3E7' ,'#F2BE45' ,'#E9E7EF' ,'#B35C44' ,'#FF2D51']

# Show Varience
initial = [kmeans(test_data, i) for i in range(1,10)]
plt.plot([var for (cent,var) in initial])
plt.show()

# Dot plot
cent, var = initial[3]
# vq get assignments
assignment,cdist = vq(test_data,cent)
# Assign color
colors = [COLOR_MAP[l] for l in assignment]
plt.scatter(test_data[:,0], test_data[:,1], c=colors)
plt.show()