## Eric's code
import math
import numpy as np
import scipy as sp
from scipy.sparse import coo_matrix

def moments_cheb(A,N=10,num_samples=100,kind=1):
    m = A.shape[0]

    Z = np.random.randn(m,num_samples)
    c = np.zeros((N,1))

    c[0] = m
    c[1] = sum(A.diagonal())
    P0 = Z
    P1 = coo_matrix.dot(A,Z) * kind

    for n in range(2,N):
        Pn = 2 * coo_matrix.dot(A,P1) - P0
        for j in range(1,num_samples):
            c[n] = c[n] + np.dot(Z[:,j] , Pn[:,j])
        c[n] = c[n] / num_samples
        P0 = P1
        P1 = Pn
    return c
