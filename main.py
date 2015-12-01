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
from calcEigen import calcEigen
from readSMAT import readSMAT
import matplotlib.pyplot as plt

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

# # dname = 'marvel-chars-cc'
# # demo(dname)

## ------Check eigen function
# filename = "musm-cc"
# fullfilename = 'data/' + filename + '.smat.gz'
# A, n = readSMAT(fullfilename)
# print n
# print A
# B = calcEigen(A, n)
# normalizedB = B / float(max(B)) + 1
# print normalizedB

# # print file_content
# ## write back to new file
# # C = map(str, B)
# C = "\n".join(str(element) for element in normalizedB)
# # print ', '.join(str(x) for x in list_of_ints)

# f = open(fullfilename[:-2] + 'jiaeigs', 'w+')
# f.write(C)
# f.close()

# # plt.hist(normalizedB)

## -------Plot 

# filename = "musm-cc"
# fullfilename = 'data/' + filename + '.smat.gz'
# mylambda = np.loadtxt(fullfilename[:-2] + 'jiaeigs')
# print mylambda
# plt.show()

# # C = normalize(B)
# # print B