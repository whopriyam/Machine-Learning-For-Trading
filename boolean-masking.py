import numpy as np

def test_run():
	a=np.array([(12,23,34,54,67,77),(34,55,67,87,34,67)])
	print a

	mean = a.mean()
	print mean

	print a[a<mean]

test_run()