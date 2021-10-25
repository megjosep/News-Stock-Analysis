# News-Stock-Analysis

This repository contains 7 files:

- Scrape LA Times (Python script)
- Scrape BBC News (Python script)
- Scrape Yahoo Finance (Python script)
- Project Description (PDF)
- Requirements (txt)
- Database Files (folder, with 3 CSV files)
- ReadMe (Markdown)

## Data Scraping

The Scrape LA Times and Scrape BBC News Python script files scrape the News API for articles published by the LA Times and BBC News about Johnson & Johnson. It retrieves the date and links of the articles and creates a CSV files of the datasets.

The Scrape Yahoo Finance Python script file scrapes the Yahoo Finance website for the daily adjusted closing stock prices of Johnson & Johnson. This also creates a CSV file of the dataset.

Users can use an optional argument ('--static') to open the CSV files of the datasets and perform analysis on them.

## Project Description

This file describes the motivation, data sources used, analyses done, and conclusions that can be made with the outputs.

## Requirements

This file details the required packages that need to be installed in order to run the program. Input '$ pip install -r requirements.txt' into the command line.

## Database Files

This folder contains the database files of the Python script files, which are the CSV files containing the datasets.


## Running the Project

Run 'Scrape LA Times.py', 'Scrape BBC News.py', and 'Scrape Yahoo Finance.py' to scrape the API and website to retrieve the datasets. The datasets should look like the CSV files that are located in the 'Outputs' folder.

Run the above files with the option argument ('--static') to create the tables and graphs based on the three datasets that were created from the previous step. These should look like the PNG files that are located in the 'Outputs' folder.
