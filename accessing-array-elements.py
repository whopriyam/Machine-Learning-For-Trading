import numpy as np

def test_run():
	a = np.random.rand(5,4)
	print a
	element = a[3,2]
	print element
	print a[0,1:4]
	print a[0:2,0:2]
	print a[:,0:3:2]

test_run()