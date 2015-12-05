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
from generateCheb import generateCheb

## ------Generate all cheb for newdata

filenames = os.listdir('data')
for filename in filenames:
	if (filename[0] != '.' and filename.endswith(".smat.gz")):
		print (filename[:-8])
		generateCheb(filename[:-8])