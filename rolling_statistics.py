def test_run():
	dates = pd.date_range('2010-01-01','2012-01-31')
	symbols = ['SPY', 'XOM', 'GOOG']
	df = get_data(symbols, dates)
	plot_data(df)
	print df.mean()
	print df.median()
	print df.std()

	ax = df['SPY'].plot(title="SPY rolling mean", label = 'SPY')
	rm_SPY = pd.rolling_mean(df['SPY'], window=20)
	sm_SPY.plot(label='Rolling mean', ax=ax)

	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	ax.legend(loc='upper left')
	plt.show()
	
test_run()test_run()