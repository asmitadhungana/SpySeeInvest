import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plot
from tensorflow import keras
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
    estimator = tf.estimator.DNNRegressor(feature_columns=feature,
                                          hidden_units=[1024, 512, 256],
                                          optimizer=tf.train.ProximalGradientDescentOptimizer(
                                              learning_rate=0.001
                                          ))


if __name__ == '__main__':
    location = "DataSets/TSLA.csv"
    feature, label = prepare_data(location)
