import os
from readSMAT import readSMAT
import numpy as np
from calcEigen import calcEigen
import matplotlib.pyplot as plt

# This function will load a given graph in .gz format
# This function calls function readSMAT and uses numpy
# input value is the name of given graph, return both the matrix and eigs
def load_graph(graphname):
	# ## use full path
	# currentPath = os.getcwd();
	# smatfile = currentPath + '/data' + graphname + '.smat'
	# smatgzfile = currentPath + '/data' + graphname + '.smat.gz'

	## use local path
	currentPath = os.getcwd();

	# ## Old data
	# smatfile = 'data/' + graphname + '.smat'
	# smatgzfile = 'data/' + graphname + '.smat.gz'
	#------------
	## New data
	smatfile = 'data/' + graphname + '.smat'
	smatgzfile = 'data/' + graphname + '.smat.gz'
	fullfilename = 'data/' + graphname + '.smat.normalized.eigs'

	## choose to read .gz file first
	if(os.path.isfile(smatgzfile)):
		A, n = readSMAT(smatgzfile)
	elif (os.path.isfile(smatfile)):
		A, n = readSMAT(smatfile)
	else:
		raise Exception('Graph does not exist.')

	# ## Old data
	# if(os.path.isfile('data/' + graphname + '.smat.normalized.eigs')):
	# 	varargout = np.loadtxt('data/' + graphname + '.smat.normalized.eigs')
	#------------
	## New data		
	if(os.path.isfile(fullfilename)):
		varargout = np.loadtxt(fullfilename)
	else: 
		## Use to Rainse Exception
		# raise Exception('eigs file does not exist.')
		varargout = 'Do not exist';
		# ## if enabled, his subrouting can calculate eigen values
		# ## Only for small matrix only
		# ## Cannot handle large file
		# B = calcEigen(A, n)
		# normalizedB = B / float(max(B)) + 1
		# C = "\n".join(str(element) for element in normalizedB)
		# # print ', '.join(str(x) for x in list_of_ints)
		# f = open(fullfilename, 'w+')
		# f.write(C)
		# f.close()

		# ## Generate Plot
		# varargout = np.loadtxt(fullfilename)
		# # print varargout
		# plt.clf()
		# plt.hist(varargout, 50)
		# filename = fullfilename[:-5] + '-eigen-dist.png'
		# # plt.show()
		# plt.savefig(filename)

	return (A, varargout)
