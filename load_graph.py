import os
from readSMAT import readSMAT
import numpy as np

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
	smatfile = 'data/' + graphname + '.smat'
	smatgzfile = 'data/' + graphname + '.smat.gz'
	## choose to read .gz file first
	if(os.path.isfile(smatgzfile)):
		A = readSMAT(smatgzfile)
	elif (os.path.isfile(smatfile)):
		A = readSMAT(smatfile)
	else:
		raise Exception('Graph does not exist.')

	if(os.path.isfile('data/' + graphname + '.smat.normalized.eigs')):
		varargout = np.loadtxt('data/' + graphname + '.smat.normalized.eigs')
	else: 
		raise Exception('eigs file does not exist.')

	return (A, varargout)