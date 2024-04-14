import pandas as pd
import yfinance as yf

ticker_symbol = 'AAPL'

data = yf.download(ticker_symbol, start='2023-01-01', end='2023-01-31')

df = pd.DataFrame(data)

print(df)
