import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

btc_data = pd.read_csv('btc_preprocessed.csv', index_col='Date', parse_dates=True')
prices = btc_data[['Close']].values

scaler = MinMaxScaler()
scaled_prices = scaler.fit_transform(prices)

def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i + seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

seq_length = 20  # 
X, y = create_sequences(scaled_prices, seq_length)

split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(seq_length, 1)),
    Dropout(0.2),
    LSTM(50, return_sequences=False),
    Dropout(0.2),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()

history = model.fit(X_train, y_train, epochs=20, batch_size=16, validation_data=(X_test, y_test))

import matplotlib.pyplot as plt

predictions = model.predict(X_test)

predictions = scaler.inverse_transform(predictions)
y_test_rescaled = scaler.inverse_transform(y_test)

plt.figure(figsize=(10, 6))
plt.plot(y_test_rescaled, label='real price')
plt.plot(predictions, label='Forecast prices')
plt.legend()
plt.title("LSTM model predicted price vs real price")
plt.xlabel("time step")
plt.ylabel("Bitcoin Closing Price")
plt.show()


