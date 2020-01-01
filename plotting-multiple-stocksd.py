import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_selected(df, columns, start_index, end_index):
	plot_data(df.ix[start_index:end_index, columns], title="Selected data")

def symbol_to_path(symbol, base_dir="data"):
	"""Return CSV file path given ticker symbol"""
	return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
	"""Read stock data for given symbols from CSV files"""
	df = pd.DataFrame(index=dates)
	if 'SPY' not in symbols:
		symbols.insert(0, 'SPY')

	for symbol in symbols:
		df_temp = pd.read_csv("/Users/priyambasu/desktop/code/Machine-Learning-For-Trading/spy.csv", index_col="date",parse_dates=True, usecols=['date','adj close'], na_values=["nan"])
		df_temp = df_temp.rename(columns={'Adj Close': symbol})
		df = df.join(df_temp)

		if symbol == 'SPY':
			df = df.dropna(subset=["SPY"])

		return df

def normalize(df, title="Stock prices"):
	return df/df.ix[0,:]

def plot_data(df):
	'''Plot stock prices'''
	ax = df.plot(title=title)
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	plt.show()


