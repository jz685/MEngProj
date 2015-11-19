import os
import numpy as np
import scipy as sp
from scipy.sparse import coo_matrix
import gzip
import time
from MyTimer import MyTimer
from load_graph import load_graph
from nadjacency import nadjacency
import math
from demo import demo


# ## main
# # ------Check load_graph function
# from load_graph import *
# from readSMAT import *
# from MyTimer import MyTimer
# # import time


# filename = 'Erdos02-cc'
# # A = load_graph(filename)

# B = load_graph(filename)

# print B

# # B, C = load_graph(filename)
# # print B
# # print C

# ------Check nadjacency function

# dname = 'Erdos02-cc'
# A, mylambda = load_graph(dname)
# N = nadjacency(A)

# ------Check Demo function

filenames = os.listdir('data')
for filename in filenames:
	if (filename[0] != '.' and filename.endswith(".smat.gz")):
		print (filename[:-8])
		demo(filename[:-8])

# dname = 'marvel-chars-cc'
# demo(dname)