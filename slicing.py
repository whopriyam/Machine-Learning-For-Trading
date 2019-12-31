import pandas as pd
	
dfspy = pd.read_csv("/Users/priyambasu/desktop/code/Machine-Learning-For-Trading/spy.csv", index_col="date",parse_dates=True, usecols=['date','adj close'], na_values=["nan"]) #Using date column as index

	for symbol in symbols:
		df_temp = pd.read_csv("/Users/priyambasu/desktop/code/Machine-Learning-For-Trading/spy.csv", index_col="date",parse_dates=True, usecols=['date','adj close'], na_values=["nan"])

		df_temp = df_temp.rename(columns={'adj close': symbol})
		df1 = df1.join(df_temp)

		if symbol == 'SPY':
			df = df.dropna(subset=["SPY"])

	return df1


def test_run():
	start_date='2016-01-22'
	end_date='2016-07-27'
	dates=pd.date_range(start_date,end_date)
	symbols = ['GOOG', 'IBM', 'GLD']

	df1 = get_data(symbols, data)

	print df.ix['2010-01-01':'2010-01-31']

	print df1['GOOG']