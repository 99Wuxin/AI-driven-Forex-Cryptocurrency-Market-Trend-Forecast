Forex/Cryptocurrency Market Trend Prediction Project

This project utilizes machine learning (Random Forest) and deep learning (LSTM) methods to predict the price trend of forex or cryptocurrencies (Bitcoin as an example) from historical market data. The project covers data collection, preprocessing, feature engineering, model training, and visualization of prediction results, and is suitable as a project to demonstrate AI and data analytics capabilities.

Install the required dependencies:

pip install yfinance pandas numpy matplotlib scikit-learn tensorflow

Run the data_collection.py script to get bitcoin historical data from Yahoo Finance and save it as a CSV file:

python data_collection.py
This script will generate the btc_data.csv file in the current directory.

Data Preprocessing
Run the data_preprocessing.py script to clean the raw data, calculate the technical indicators and generate the labeled data:

python data_preprocessing.py
The pre-processed data will be saved as btc_preprocessed.csv.

Machine learning modeling (random forest)
Run the random_forest_model.py script to use the Random Forest model to make categorical price rise and fall predictions:

python random_forest_model.py
The script outputs the accuracy of the model on the test set.

Deep Learning Modeling (LSTM)
Run the lstm_model.py script to build and train an LSTM model, then visualize the predictions against real prices:

python lstm_model.py
At the end of training, a popup chart will show the prediction results.

