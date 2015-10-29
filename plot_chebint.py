import math
import numpy as np
import scipy as sp
from scipy.sparse import coo_matrix

def plot_chebint(c,xx):
    N = c.shape[0]
    txx = np.arccos(xx)
    yy = c[0] * (txx-math.pi)/2
    for NP in range(1,N):
        n = NP 
        yy = yy + c[NP] * np.sin(n*txx) / n
    yy = -2 / math.pi * yy
    return yy