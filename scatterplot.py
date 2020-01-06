import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from util import get_data, plot_data

def compute_daily_returns():
	daily_returns = df.copy()
	daily_returns[1:] = (df[1:]/df[:-1].values) - 1
	daily_returns.ix[0,:] = 0
	return daily_returns


def test_run():
	dates=pd.date_range('2009-01-01','2012,12,31')
	symbols = ['SPY', 'XOM'. 'GLD']
	df = get_data(symbols, dates)
	plot_data(df)

	daily_returns = compute_daily_returns(df)
	beat_XOM, alpha_XOM = np.ployfit(daily_returns['SPY'], daily_returns['XOM'], 1)
	print "beta_XOM= ", beta_XOM
	print "alpha_XOM", alpha_XOM
	plt.plot(daily_returns['SPY'], beta_XOM*daily_returns['SPY']+alpha_XOM,'-',color='r') # mx+b
	plt.show()
	
	daily_returns.plot(kind='scatter', x='SPY', y='GLD')
	plt.show()

	print daily_returns.corr(method='pearson')