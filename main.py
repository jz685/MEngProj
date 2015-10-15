## main
from load_graph import *
from readSMAT import *

filename = 'mytest'

# A = load_graph(filename)
B = load_graph(filename)

print B

B, C = load_graph(filename)
print B
print C