import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    #main()
    return render_template("base.html")

@app.route("/train", methods =["POST"])   
def train():
    
    title = request.form.get("title")
    if title == "":
        return redirect(url_for("index"))
    else:
        print(title)
        main(title)
        return render_template("query.html")


def stock_predictor(data):
    dataset_file = data.split(" ")[0]
    desired_year = data.split(" ")[1]
    df = pd.read_csv(dataset_file)

    #Remove Null Values
    df = df.dropna()

    #Slicing Training and Test
    index_list = list(df.index.values)
    imp_value = -1
    for i in index_list:
        if df["Date"][i].split("-")[0] == desired_year:
            imp_value = i
            break
    if imp_value == -1:
        print("Incorrect Dataset")
    else:

        training_set = df[:imp_value]
        global test_set
        test_set = df[imp_value:]

        #Training Set (Feature Scaling and Getting the inputs and the ouputs)
        training_set = training_set.iloc[:,1:2]
        training_set = training_set.values
        global sc
        sc = MinMaxScaler()
        training_set = sc.fit_transform(training_set)
        X_train = training_set[0:len(training_set)-1]
        y_train = training_set[1:len(training_set)]
        X_train = np.reshape(X_train, (imp_value-1, 1, 1))

        #RNN Model
        """
        A recurrent neural network (RNN) is a type of artificial neural network which uses sequential data or time series data. 
        
        """
        global model
        model = Sequential()
        model.add(LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 1)))
        model.add(Dense(units = 1))
        model.compile(optimizer = 'adam', loss = 'mean_squared_error')
        model.fit(X_train, y_train, batch_size = 32, epochs = 200)

        """
        while True:
            print("Type your Query")
            myquery_date = input("Date (example: 2022-01-31)")
            myquery_index = -1
            for index, row in test_set.iterrows():
                #print(row['Date'], index)
                if row["Date"] == myquery_date:
                    myquery_index = index

            if myquery_index == -1:
                print("Incorrect Date")

            else:
                real_stock_price = test_set.iloc[:, 1:2]
                real_stock_price = real_stock_price.loc[myquery_index:myquery_index, "Open"]
                real_stock_price = real_stock_price.values

                inputs = real_stock_price
                inputs = [inputs]
                inputs = sc.transform(inputs)
                inputs = np.reshape(inputs, (1, 1, 1))

                predicted_stock_price = model.predict(inputs)
                predicted_stock_price = sc.inverse_transform(predicted_stock_price)
                print("Predicted Stock Price:", predicted_stock_price[0][0], "USD")

                """


@app.route("/myquerypage", methods =["POST"])   
def query():
    
    title = request.form.get("title")
    if title == "":
        return render_template("query.html")
    else:
        print(title)
        query_output(title)
        return render_template("output.html", variable = predicted_stock_price)

def query_output(data):
                
    myquery_date = data
    myquery_index = -1
    for index, row in test_set.iterrows():
        #print(row['Date'], index)
        if row["Date"] == myquery_date:
            myquery_index = index

    if myquery_index == -1:
        print("Incorrect Date")

    else:
        real_stock_price = test_set.iloc[:, 1:2]
        real_stock_price = real_stock_price.loc[myquery_index:myquery_index, "Open"]
        real_stock_price = real_stock_price.values

        inputs = real_stock_price
        inputs = [inputs]
        inputs = sc.transform(inputs)
        inputs = np.reshape(inputs, (1, 1, 1))

        global predicted_stock_price
        predicted_stock_price = model.predict(inputs)
        predicted_stock_price = sc.inverse_transform(predicted_stock_price)
        print("Predicted Stock Price:", predicted_stock_price[0][0], "USD")
        predicted_stock_price = predicted_stock_price[0][0]

@app.route("/return", methods =["POST"]) 
def go_back():
    return render_template("query.html")


def main(data):
    stock_predictor(data)

if __name__ == '__main__':
    app.run(debug = True)
    