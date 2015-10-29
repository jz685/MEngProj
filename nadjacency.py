from scipy.sparse import issparse
from scipy.sparse import coo_matrix
import scipy as sp
import numpy as np
import math


# Did not implement the function handle part

def nadjacency(A):
	# # # Recover to dense
	# # d = A.todense();
	# # # get sum of anix 2
	# # d = d.sum(1);
	# d = np.array(coo_matrix.sum(A,1)).T 
	# for x in np.nditer(d, op_flags = ['readwrite']):
	# 	if x != 0:
	# 		x[...] = 1/(math.sqrt(x))

	# if sp.sparse.issparse(A):
	# 	[i, j, v] = sp.sparse.find(A)
	# 	# m, n = A.shape
	# 	N = sp.sparse.coo_matrix(( v * d[i] * d[j], (i,j)), shape = A.shape)
	# else:
	# 	N = np.dot(np.dot(np.diag(d), A), np.diag(d));

	# return N

	if (sp.sparse.issparse(A)):

		[d] = np.array(coo_matrix.sum(A,1)).T
		for x in np.nditer(d, op_flags = ['readwrite']):
			if x != 0:
				x[...] = 1/(math.sqrt(x))

		[i,j,v] = sp.sparse.find(A)
		N = coo_matrix((v * d[i] * d[j],(i,j)),shape = A.shape)

	else:
		d = np.array(np.sum(A,1))
		d = d.astype(float)
		d[d!=0] = 1 / (d[d!=0] ** (0.5))

		N =  np.dot(np.dot(np.diag(d),A),np.diag(d))

	return N


	# for each element e in d, if e != 0, let e = 1/sqrt(e)

