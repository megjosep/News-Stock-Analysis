import requests
import csv
import argparse
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# optional argument

static = False

parser = argparse.ArgumentParser(description='Scrapes News API for Johnson & Johnson articles by BBC News')
parser.add_argument('--static', action='store_true', default=False, dest='static', help='Opens dataset file and conducts data analysis')

args = parser.parse_args()

url = 'https://newsapi.org/v2/everything?'

# scrapes for BBC News articles about Johnson & Johnson within the specified timeframe

if args.static == False:

	parameters = {
		'q': 'Johnson & Johnson',
		'sources': 'bbc-news',
		'from': '2021-04-12',
		'to': '2021-04-25',
		'language': 'en',
		'sort_by': 'publishedAt',
		'pageSize': 100,
		'apiKey': '59aca34e116b4f19bb41b5c9ac1a6ed8'
	}

	response = requests.get(url, params=parameters)
	response_json = response.json()
	articles = response_json['articles']

	urls = list(['Link'])
	dates = list(['Date'])

	for article in articles:
		urls.append(article['url'])
		dates.append(article['publishedAt'][0:10])

	# creates a CSV file for the dataset

	with open('BBC News Dataset.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerows(zip(dates, urls))

# opens CSV file of the dataset

if args.static == True:
	with open('BBC News Dataset.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			print(row)

	bbc_news_data = pd.read_csv('BBC News Dataset.csv')

	# creates DataFrame for the BBC News Dataset, sorted ascending by date

	bbc_news_df = pd.DataFrame(bbc_news_data, columns=['Date', 'Link'])
	bbc_news_df.sort_values(by=['Date'], inplace=True)
	print(la_times_df)

	# creates bar graph based on the count of articles published by the BBC News on each date

	sns.countplot(y='Date', data=bbc_news_df)
	plt.show()

