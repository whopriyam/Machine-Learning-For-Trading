#Slicing
import pandas as pd

def test_run():
	df = pd.read_csv("/Users/priyambasu/desktop/code/ML-For-Trading/Goldmann-Sachs.csv")
	print df[10:21]


if __name__ == "__main__":
	test_run()