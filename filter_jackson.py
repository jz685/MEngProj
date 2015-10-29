# From Eric's code
import math
import numpy as np
import scipy as sp

def filter_jackson(c):
    c = np.array(c)
    N = c.shape[0]
    n = np.array([range(0,N)])
    tau = math.pi / (N+1)
    g = ( (N-n+1) * np.cos(tau * n) + np.sin(tau * n) / np.tan(tau) ) / (N+1)
    return g.T * c