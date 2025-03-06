import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

btc_data = pd.read_csv('btc_preprocessed.csv', index_col='Date', parse_dates=True)

features = ['SMA_20', 'SMA_50', 'Price_Change']
X = btc_data[features]
y = btc_data['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Random Forest Model Accuracy. {accuracy:.2f}')
