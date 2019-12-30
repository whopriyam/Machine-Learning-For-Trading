import pandas as pd

def test_run():
	start_date='2016-01-22'
	end_date='2016-07-27'
	dates=pd.date_range(start_date,end_date)
	df1=pd.DataFrame(index=dates)
	
	dfspy = pd.read_csv("/Users/priyambasu/desktop/code/Machine-Learning-For-Trading/spy.csv", index_col="date",parse_dates=True, usecols=['date','adj close'], na_values=["nan"]) #Using date column as index
	df1=df1.join(dfspy)
	df1=df1.dropna()
	print df1

test_run()
