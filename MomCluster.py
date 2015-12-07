from clusterByMom import clusterByMom
from listAllDatasets import listAllDatasets
from superLearning import superLearning
from superTesting import superTesting

print "||-------------------------------||"
print ('Choose your command from bellow:')
print ('CAD \t--Cluster All Data, which will cluster all datasets in folder \data')
print ('SL \t--Supervised Learning, which will perform a supervised ML with training and testing datasets of your choise')
command = raw_input('Enter your command: ')
if (command == 'CAD'):
	## Print all available data
	listAllDatasets()

	## Cluster all cheb files in data
	clusterCentro = clusterByMom()
	print 'Calculated Centrals are: '
	print clusterCentro
elif (command == 'SL'):
	## Print all available data
	listAllDatasets()

	print ('Choose your training data in the format as: data1, data2 ...')
	training = raw_input('Enter your training data: ')
	print ('Choose your testing data in the format as: data1, data2 ...')
	testing = raw_input('Enter your testing data: ')

	trainDataArray = training.split(', ')
	print trainDataArray
	testDataArray = testing.split(', ')
	print testDataArray

	book = superLearning(trainDataArray)
	superTesting(testDataArray, book)


else:
	raise Exception('Cannot recognize this command:' + command)
