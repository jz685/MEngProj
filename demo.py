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
from filter_jackson import filter_jackson
from compare_chebhist import compare_chebhist

## The demo function is a simple function that calles a series of functions and display the result
def demo(dname, Ncheb = 1000, Nbin = 50):
	
	## Calling loadgraph and set timer 1
	with MyTimer('Timer One'):
		A, mylambda = load_graph(dname)
		N = nadjacency(A)

	## Calculate cheb moments and set timer 2
	with MyTimer('Timer Two'):
		c = moments_cheb(N, Ncheb, 10)

	## Compare the resuts and display plot, notice filtered cheb moments are passed 
	compare_chebhist(dname, mylambda, filter_jackson(c), Nbin)




