import os
import numpy as np
import scipy as sp
from scipy.sparse import coo_matrix
import gzip

## The readSMAT function takes a filename as paremeter, checks if it is a valid 
## file, and calles the readSMATGZ to handle the file. 
def readSMAT(filename):
	print '--reading: ' + filename
	if (not os.path.isfile(filename)):
		raise Exception('ERROR: No such file:' + filename)
	# if (os.path.isfile(filename + '.info')):
	# 	return

	if (os.path.splitext(filename)[1] == '.gz'):
		# the outcome i, j, v are verctors and m, n are the size
		m, n, i, j, v = readSMATGZ(filename)
		## Some Testing Code
		print i
		print j
		print m
		print n
		# A = sp.sparse.coo_matrix((v, (i, j)), shape=(m,n))
		# A = sp.sparse.coo_matrix((v, (i, j)), shape = (m, n)).toarray()
		A = sp.sparse.coo_matrix((v, (i, j)), shape = (m, n))

		## For testing 
		return (A, m)
		# ## Original
		# return A

## The readSMATGZ function takes a .gz filename as input parameter, extract 
## from .gz, and read in its content
def readSMATGZ(filename):
	print "read from gz"
	with gzip.open(filename, 'rb') as f:
		file_content = f.read()

	# print file_content
	## write back to new file
	f = open(filename[:-3], 'w+')
	f.write(file_content)
	f.close()

	## read that file into array
	print 'reading: ' + filename[:-3]
	tempArray = np.loadtxt(filename[:-3])
	print tempArray

	## convert array to the required format
	m = tempArray[0, 0]
	n = tempArray[0, 1]
	nnz = tempArray[0, 2]
	iarray = tempArray[1:,0]
	jarray = tempArray[1:,1]
	varray = tempArray[1:,2]

	return (m, n, iarray, jarray, varray)


