def test_run():
	dates = pd.date_range('2010-01-01','2012-01-31')
	symbols = ['SPY', 'XOM', 'GOOG']
	df = get_data(symbols, dates)
	plot_data(df)
	print df.mean()
	print df.median()
	print df.std()

test_run()