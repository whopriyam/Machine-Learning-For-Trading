import pandas as pd

def get_mean_volume(symbol):
	""" Return max closing value for stock indicated by symbol"""

	df = pd.read_csv("data/{}.csv".format(symbol)) #Reading the data
	return df['Volume'].mean() #Compute and return max

def test_run():
	"""Function called by test run"""
	for symbol in ['AAPL', 'IBM']:
		print "Mean Volume"
		print symbol, get_mean_volume(symbol)


if __name__ == "__main__":
	test_run()