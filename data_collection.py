import yfinance as yf
import pandas as pd

btc_data = yf.download('BTC-USD', start='2022-01-01', end='2025-03-06', interval='1d')
btc_data.to_csv('btc_data.csv')  
print(btc_data.head())
