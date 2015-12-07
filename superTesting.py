import numpy as np
from numpy import random
from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten, kmeans2
import matplotlib.pyplot as plt
import os

def superTesting(testing, book):

	datanames = []
	datasets = []

	filenames = os.listdir('data')
	for filename in filenames:
		if (filename[0] != '.' and filename.endswith(".cheb")):
			# print ('Now Reading:' + filename[:-5])
			rawname = filename[:-5]
			## Check if testing
			if rawname in testing:
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


	#---------
	code_book = book
	# print datanames
	datasets = np.array(datasets)
	# print datasets
	whiten_data = whiten(datasets);
	assignment, distance = vq(whiten_data,code_book)
	# print assignment
	# print distance

	for i in range (len(assignment)) :
		print str(datanames[i]) + "\t\tis assigned to\t\t" + str(assignment[i])
