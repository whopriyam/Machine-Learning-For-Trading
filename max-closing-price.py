import pandas as pd

def get_max_close(symbol):
	""" Return max closing value for stock indicated by symbol"""

	df = pd.read_csv("/Users/priyambasu/desktop/code/ML-For-Trading/{}.csv".format(Goldmann-Sachs.csv)) #Reading the data
	return df['Close'].max() #Compute and return max

def test_run():
	"""Function called by test run"""
	for symbol in ['AAPL', 'IBM']:
		print "Max Close"
		print symbol, get_max_close(symbol)


if __name__ == "__main__":
	test_run()