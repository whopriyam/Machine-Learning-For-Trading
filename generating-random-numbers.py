import numpy as np

def test_run():
	print np.random.rand(5,4)
	#Sample numbers from a Gaussian distribution
	print np.random.normal(size=(2,3))
	print np.random.randint(0,10, size = (2,3))

test_run()