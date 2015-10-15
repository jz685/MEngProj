import os
import gzip

filename = 'data/mytest.smat'

f = open(filename, 'r')
content = f.read()
f.close()

with gzip.open(filename + '.gz', 'w+') as f:
	f.write(content)
