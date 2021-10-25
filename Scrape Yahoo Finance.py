import pandas_datareader as pdr
from datetime import datetime
import csv
from itertools import zip_longest
import argparse
import matplotlib.pyplot as plt
import pandas as pd

# optional argument

static = False

parser = argparse.ArgumentParser(description='Scrapes Yahoo News for Johnson & Johnson historical stock data')
parser.add_argument('--static', action='store_true', default=False, dest='static', help='Opens dataset file and conducts data analysis')

args = parser.parse_args()

# scrapes for Johnson & Johnson historical stock data from Yahoo Finance

if args.static == False:

    jnj = pdr.get_data_yahoo(symbols='JNJ', start=datetime(2021, 4, 12), end=datetime(2021, 4, 25))

    # creates a CSV file for the dataset

    dates = ['2021-04-12', '2021-04-13', '2021-04-14', '2021-04-15', '2021-04-16', '2021-04-19', '2021-04-20', '2021-04-21', '2021-04-22', '2021-04-23']
    adj_closing = jnj['Adj Close']

    yahoo_data = [dates, adj_closing]
    export_data = zip_longest(*yahoo_data, fillvalue='')

    with open('Yahoo Finance Dataset.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(['Date'], ['Adjusted Closing']))
        writer.writerows(export_data)

# opens CSV file of the dataset

if args.static == True:
    with open('Yahoo Finance Dataset.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    jnj_stock_data = pd.read_csv('Yahoo Finance Dataset.csv')

    # creates DataFrame for the Yahoo Finance Dataset

    jnj_stock_df = pd.DataFrame(jnj_stock_data, columns=['Date', 'Adjusted Closing'])
    print(jnj_stock_df)

    # creates line graph based on Johnson & Johnson adjusted closing stock price each day

    jnj_stock_df.plot(x='Date', y='Adjusted Closing', kind='line')
    plt.show()


