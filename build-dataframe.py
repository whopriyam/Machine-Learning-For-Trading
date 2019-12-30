import pandas as pd

def test_run():
	start_date='2010-01-22'
	end_date='2010-01-27'
	dates=pd.date_range(start_date,end_date)
	df1=pd.DataFrame(index=dates)
	print df1

test_run()