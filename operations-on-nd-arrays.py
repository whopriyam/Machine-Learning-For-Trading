import numpy as np

def test_run():
	np.random.seed(693)
	a=np.random.randint(0,10,size=(5,4))
	print "Array:\n", a
	print "Sum of all elements:\n", a.sum()
	print "Sum of each column:\n", a.sum(axis=0)
	print "Sum of each row:\n", a.sum(axis=1)
	print "Min of each row:\n", a.min(axis=1)
	print "Min of each column:\n", a.min(axis=0)
	print "Max of each row:\n", a.min(axis=1)
	print "Max of each column:\n", a.min(axis=0)
	print "Mean of each row:\n", a.mean(axis=1)
	print "Mean of each column:\n", a.mean(axis=0)

test_run()