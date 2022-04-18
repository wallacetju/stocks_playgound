# Reference: https://towardsdatascience.com/historical-stock-price-data-in-python-a0b6dc826836
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd


def sample_prices():
    data = yf.download('VOO, AAPL', '2010-01-01', '2022-04-01')
    data['Adj Close'].plot()
    plt.show()


def sample_multi_stocks():
    tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']
    # Fetch the data
    data = yf.download(tickers_list, '2010-1-1')['Adj Close']

    # Print first 5 rows of the data
    print(data.head())

    # Plot all the close prices
    ((data.pct_change() + 1).cumprod()).plot(figsize=(10, 7))

    # Show the legend
    plt.legend()

    # Define the label for the title of the figure
    plt.title("Returns", fontsize=16)

    # Define the labels for x-axis and y-axis
    plt.ylabel('Cumulative Returns', fontsize=14)
    plt.xlabel('Year', fontsize=14)

    # Plot the grid lines
    plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
    plt.show()


if __name__ == '__main__':
    sample_multi_stocks()
