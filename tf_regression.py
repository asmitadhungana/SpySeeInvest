import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.layers import Dense
import pandas as pd
import matplotlib.pyplot as plot
from datetime import datetime as dt


def calculate_days(startdatestr, enddatestr):
    startdate = dt.strptime(startdatestr, '%Y-%m-%d')
    enddate = dt.strptime(enddatestr, '%Y-%m-%d')
    delta = enddate - startdate
    return delta.days


def prepare_data(location):
    dataset = pd.read_csv(location)
    dataset = dataset.drop('High', axis=1)
    dataset = dataset.drop('Low', axis=1)
    dataset = dataset.drop('Close', axis=1)
    dataset = dataset.drop('Adj Close', axis=1)
    dataset = dataset.drop('Volume', axis=1)
    label = dataset.pop('Open')
    startdate = dataset.iloc[0, 0]
    noofrows = dataset.shape[0]
    for i in range(noofrows):
        enddate = dataset.iloc[i, 0]
        days = calculate_days(startdate, enddate)
        dataset['Date'][i] = days
    return dataset, label


def build_model(feature, label):
    model = keras.Sequential([
        Dense(64, activation=tf.nn.relu, input_shape=[len(feature.keys())]),
        Dense(64, activation=tf.nn.relu),
        Dense(1)
    ])

    optimizer = tf.train.RMSPropOptimizer(0.001)

    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mae', 'mse'])

    EPOCHS = 1000

    model.fit(
      feature, label,
      epochs=EPOCHS, validation_split=0.2, verbose=0)
    plot.scatter(feature, label, color='red')
    plot.plot(feature, model.predict(feature), color='blue')
    plot.title('Number of days VS Open Stock Price (Training set)')
    plot.xlabel('Number of days')
    plot.ylabel('Open Stock price')
    plot.show()
    return model


def predict(model, location):
    dataset = pd.read_csv(location)
    startdatestr = dataset.iloc[0, 0]
    desireddate = input("Enter the date: ")
    day = calculate_days(startdatestr, desireddate)
    print(model.predict([[day]]))


if __name__ == '__main__':
    location = "DataSets/TSLA.csv"
    feature, label = prepare_data(location)
    model = build_model(feature, label)
    predict(model, location)
