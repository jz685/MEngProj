import os
import numpy as np
import scipy as sp
from scipy.sparse import coo_matrix
import gzip

def readSMAT(filename):
	print '-now reading: ' + filename
	if (not os.path.isfile(filename)):
		raise Exception('ERROR: No such file:' + filename)
	if (os.path.isfile(filename + '.info')):
		# ## Need Modification
		# s = load(filename)
		# mdata = load(filename + '.info')
		# ind_i = s(m)
		return

	if (os.path.splitext(filename)[1] == '.gz'):
		# the outcome i, j, v are verctors and m, n are the size
		m, n, i, j, v = readSMATGZ(filename)
		# print i
		# print j
		# print m
		# print n
		# A = sp.sparse.coo_matrix((v, (i, j)), shape=(m,n))
		# A = sp.sparse.coo_matrix((v, (i, j)), shape = (m, n)).toarray()
		A = sp.sparse.coo_matrix((v, (i, j)), shape = (m, n))
		return A


def readSMATGZ(filename):
	## read from gz
	with gzip.open(filename, 'rb') as f:
		file_content = f.read()
	# print file_content
	## write back to new file
	f = open(filename[:-3], 'w+')
	f.write(file_content)
	f.close()
	## read that file into array
	tempArray = np.loadtxt(filename[:-3])
	## convert array to the required format
	m = tempArray[0, 0]
	n = tempArray[0, 1]
	nnz = tempArray[0, 2]
	iarray = tempArray[1:,0]
	jarray = tempArray[1:,1]
	varray = tempArray[1:,2]

	return (m, n, iarray, jarray, varray)


