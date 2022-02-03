# PythonApp-StockPredictor
* Created a tool that allows you to predict stock prices using historical stock data obtained through Yahoo Finance.
* Used LSTM (Long Short-Term Memory), which is a Recurrent Neural Network (RNN) based architecture for time series forecasting.
* Previously, I trained a RNN model to predict stock prices of Alphabet and Bitcoin on a Jupyter notebook.
  * Data Cleaning/Visualization (removed null values, train-test split, feature scaling with MinMaxScaler, ...)
  * Model Building (RNN model)
* After that, I built a client facing application using Flask (web framework) that:
  * automatically trains a RNN model with dataset obtained through Yahoo Finance that you must include inside the project folder.
  * allows you to use that model in order to query the predicted stock price.


## Resources Used
* **Python Version:** 3.10
* **Packages:** pandas, numpy, sklearn, flask, keras, tensorflow
* **Flask Activation:** https://flask.palletsprojects.com/en/2.0.x/installation/ (after activation, type "python main.py" to run the app)
* **Stock Datasets:** https://finance.yahoo.com/quote/GOOG/history/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAADgKAIw8R5G5EDld4xwcKfDy-4pHRLkyy6MSV7CO-qSLp4RObjlKq9Ve75PbaTqJZBaQDK3kldwM1aGby9x9GOTACKjfEW788ZT1mOtqxhQG_rjoq9mRac97_NJGomhjGUhATCM3Oc6bH7F7sqTQGKOKAtXDlwL9C8BOEuZIAWmK
* **Markdown Syntax** https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
* **Requirements** https://www.youtube.com/watch?v=eW0BmZ8i8Eo (Remember to use "pip3 install -r requirements.txt")


