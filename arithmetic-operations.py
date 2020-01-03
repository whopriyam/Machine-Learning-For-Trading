import numpy as np

def test_run():
	a=np.array([(12,23,34,54,67,77),(48,55,67,87,34,67)])
	print a
	b=np.array([(21,23,34,54,67,77),(34,55,67,87,34,67)])
	print b

	print 2*a
	print a/2
	print a+b
	print a*b
	print a/b
test_run()