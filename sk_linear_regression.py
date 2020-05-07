import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plot
from datetime import datetime as dt


def calculate_days(startdatestr, enddatestr):
    startdate = dt.strptime(startdatestr, '%Y-%m-%d')
    enddate = dt.strptime(enddatestr, '%Y-%m-%d')
    delta = enddate - startdate
    return delta.days


def prepare_data(location): 
    data = pd.read_csv(location)
    startdate = data.iloc[0, 0]
    
    noofrows = data.shape[0]
    for i in range(noofrows):
        enddate = data.iloc[i, 0]
        days = calculate_days(startdate, enddate)
        data['Date'][i] = days
    return data


def prepare_model(dataset):
    x = dataset[['Date']].values
    y = dataset[['Open']].values
    linearRegressor = LinearRegression()
    linearRegressor.fit(x, y)
    plot.scatter(x, y, color='red')
    plot.plot(x, linearRegressor.predict(x), color='blue')
    plot.title('Number of days VS Open Stock Price (Training set)')
    plot.xlabel('Number of days')
    plot.ylabel('Open Stock price')
    plot.show()
    return linearRegressor


def predict(model, location):
    dataset = pd.read_csv(location)
    startdatestr = dataset.iloc[0, 0]
    desireddate = input("Enter the date: ")
    day = calculate_days(startdatestr, desireddate)
    print(model.predict([[day]]))


if __name__ == '__main__':
    location = "DataSets/TSLA.csv"
    dataset = prepare_data(location)
    model = prepare_model(dataset)
    predict(model, location)
