import time

class MyTimer(object):

	def __init__(self, name):
		self.myname = name

	def __enter__(self):
		self.startTime = time.time()

	def __exit__(self, type, value, traceback):
		print 'Time Spend: %s' % (time.time() - self.startTime)