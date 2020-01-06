import pandas as pd
import matplotlib.pyplot as plt

from util import get_data, plot_data

def compute_daily_returns():
	daily_returns = df.copy()
	daily_returns[1:] = (df[1:]/df[:-1].values) - 1
	daily_returns.ix[0,:] = 0
	return daily_returns


def test_run():
	dates=pd.date_range('2009-01-01','2012,12,31')
	symbols = ['SPY', 'XOM']
	df = get_data(symbols, dates)
	plot_data(df)

	daily_returns = compute_daily_returns(df)
	
	daily_returns['SPY'].hist(bins=20,label="SPY")
	daily_returns['XOM'].hist(bins=20,label="XOM")

	plt.legend(loc='upper right')
	plt.show()