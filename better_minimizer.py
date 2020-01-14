import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo

def error(line, data):
	"""Compute error between given line model and observed data
	Parameters:

	line:tuple/lis/array (C0, C1) where C0 is the slope and C1 is the y-intercept
	data:2D array where each row is at a point (x,y)

	Returns arror as a single real value
	"""

	#Sum of squared Y axis differences

	err = np.sum((data[:,1]-(line[0]*data[:,0]+line[1])) ** 2)
	return err

def fit_line(data, error_func):
	#Generate initial guess for line model
	l=np.float32([0,np.mean(data[:,1])])

	x_ends = np.float32([5,-5])

	plt.plot(x_ends,l[0]*x_ends + l[1], 'm--', linewidth=2.0, label="Initial guess")

	result = spo.minimize(error_func, l, args=(data), method='SLSQP', options={'disp': True})

	return result.x

def test_run():
	l_orig = np.float32([4,2])
	print "Original line: C0={}, C1={}".format(l_orig[0], l_orig[1])
	Xorig = np.linespace(0,10,21)
	Yorig = l_orig[0] * Xorig + l_orig[1]
	plt.plot(Xorig,Yorig, 'b--', linewidth=2.0, label="Original line")

	noise_sigma = 3.0
	noise = np.random.normal(0, noise_sigma, Yorig.shape)
	data = np.asarray([Xorig, Yorig + noise]).T
	plt.plot(data[:,0], data[:,1], 'go', label="Data Points")

test_run()