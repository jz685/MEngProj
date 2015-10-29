import os
import numpy as np
import scipy as sp
from scipy.sparse import coo_matrix
import gzip
import time
from MyTimer import MyTimer
from load_graph import load_graph
from nadjacency import nadjacency

def demo(dname, Ncheb = 1000, Nbin = 50):
	
	with MyTimer('hello'):
		A, mylambda = load_graph(dname)
		N = nadjacency(A)


	with MyTimer('hello2'):
		c = moments_cheb(N, Ncheb, 10)

	compare_chebhist(1 - mylambda, filter_jackson(c), Nbin)




