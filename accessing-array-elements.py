import numpy as np

def test_run():
	a = np.random.rand(5,4)
	print a
	element = a[3,2]
	print element
	print a[0,1:4]
	print a[0:2,0:2]
	print a[:,0:3:2]
	a[0,0] = 1
	a[1:] = 7
	print a
	a[:, 3] = [1,2,3,4,5]
	print a
test_run()