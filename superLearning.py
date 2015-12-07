import numpy as np
from numpy import random
from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten, kmeans2
import matplotlib.pyplot as plt
import os

def superLearning(training):

	datanames = []
	datasets = []

	filenames = os.listdir('data')
	for filename in filenames:
		if (filename[0] != '.' and filename.endswith(".cheb")):
			# print ('Now Reading:' + filename[:-5])
			rawname = filename[:-5]
			## Check if training
			if rawname in training:
				# print ('Now Reading:' + rawname)
				datanames.append(filename[:-5])
				dataarray = []
				f = open('data/' + filename, 'r')

				for content in f.readlines():
	  				# print content
					item = content[1:-2]
					# print item
					dataarray.append(float(item))
					content = f.readline()
				f.close()
				datasets.append(dataarray)

	# print datasets



	## -------------------
	# print datanames
	datasets = np.array(datasets)
	# print datasets
	whiten_data = whiten(datasets);
	# print whiten_data

	initial = [kmeans(datasets, i) for i in range(1,10)]
	plt.plot([var for (cent,var) in initial])
	plt.show()

	## Run with random initialization
	## Don't use this, not positive definite matrix, will not work in this case
	# result, assignment = kmeans2(whiten_data, 3);
	# result, assignment = kmeans2(datasets, 4);
	# print assignment

	## *****!!!!!_____Change Number of Clusters Here______!!!!!******
	# ## Run with manual initialization
	book = array ((whiten_data[0], whiten_data[5]));
	result, assignment = kmeans2(whiten_data, book);
	# print assignment
	# book = array ((test_data[5], test_data[15], test_data[25], test_data[35]));
	# result, assignment = kmeans2(test_data, book);
	# print assignment



	## Enable these lines if you wants to see the assignments of training data
	# for i in range (len(assignment)) :
	# 	print str(datanames[i]) + "\t\tis assigned to\t\t" + str(assignment[i])

	return result