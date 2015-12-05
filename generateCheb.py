import os
import numpy as np
import scipy as sp
from scipy.sparse import coo_matrix
import gzip
import time
from MyTimer import MyTimer
from load_graph import load_graph
from nadjacency import nadjacency
from moments_cheb import moments_cheb
import math
import numpy as np
import scipy as sp


## The demo function is a simple function that calles a series of functions and display the result
def generateCheb(dname, Ncheb = 1000, Nbin = 50):
	
	## Calling loadgraph and set timer 1
	with MyTimer('Timer One'):
		A, mylambda = load_graph(dname)
		N = nadjacency(A)

		c = moments_cheb(N, Ncheb, 10)
		cheb_file_content = '\n'.join([str(st) for st in c])

		cheb_filename = 'data/' + dname + '.cheb'
		f = open(cheb_filename, 'w+')
		f.write(cheb_file_content)
		f.close()
