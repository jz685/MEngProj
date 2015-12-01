import math
import numpy as np
import scipy as sp
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

def calcEigen (A, n):
	## A is sp.sparse.coo_matrix
	## n is the number of elements
	print "-calculating.."
	vals, vecs = eigsh(A, k=n - 1)
	return vals;



# def normalize(a, axis=-1, order=2):
# 	print "-normalizing.."
#     l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
#     l2[l2==0] = 1
#     return a / np.expand_dims(l2, axis)
