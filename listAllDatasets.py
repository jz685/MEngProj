import os

def listAllDatasets():

	# datanames = []
	print "//----------------Data Sets Available---------------\\\\"
	filenames = os.listdir('data')
	for filename in filenames:
		if (filename[0] != '.' and filename.endswith(".cheb")):
			print (filename[:-5])
			# datanames.append(filename[:-5])
	# print datanames

	print "\\\\-------------------End of List------------------//"
