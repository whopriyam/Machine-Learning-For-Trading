import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def f(X):
	"""Given a scalar X, return some value (a real number)"""
	Y=(X-1.5)**2 + (0.5*X) + 7
	print "X = {}, Y = {}".format(X, Y) #For tracing
	return Y

def test_run():
		Xguess=2.0
		min_result = spo.minimize(f, Xguess, method='SLSQP', options={'disp': True})
		print "Minima found at:"
		print "X={}, Y={}".format(min_result.x, min_result.fun)

		Xplot = np.linspace(0.5,2.5,21)
		Yplot = f(Xplot)
		plt.plot(Xplot, Yplot)
		plt.plot(min_result.x, min_result.fun, 'ro')
		plt.title("Minima")
		plt.show()

test_run()