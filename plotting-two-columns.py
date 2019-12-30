import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("/Users/priyambasu/desktop/code/ML-For-Trading/Goldmann-Sachs.csv")
    # TODO: Your code here
    print df[['Close', 'Adj Close']]
    df[['Close', 'Adj Close']].plot()
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()
