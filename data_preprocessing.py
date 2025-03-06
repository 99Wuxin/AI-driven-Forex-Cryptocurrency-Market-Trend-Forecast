import pandas as pd

btc_data = pd.read_csv('btc_data.csv', index_col='Date', parse_dates=True)

btc_data['SMA_20'] = btc_data['Close'].rolling(window=20).mean()
btc_data['SMA_50'] = btc_data['Close'].rolling(window=50).mean()

btc_data['Price_Change'] = btc_data['Close'].pct_change()

btc_data.dropna(inplace=True)

btc_data.to_csv('btc_preprocessed.csv')
print(btc_data.head())
