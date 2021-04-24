# A Comparison of Housing Prices vs. Income in Washington Countys from 2008 and 2019
A data analytics project for WSUV.

Motivation:

My goal when analyzing this data, was to see if home prices in the counties of Washington State were correlated to the
median income of the county. With the 2019 real estate market being so hot, I was wondering if the rise in house prices was related to an increase in income, or a 2008 like housing market speculation bubble.

Data Process:

To answer this question I needed to find data on the median price of houses by county in Washington State, and the median income in Washington State. I found historic median house prices by county for Washington on this website https://wcrer.be.uw.edu/archived-reports/ , but the problem was that the data was stored in PDFs, not the CSV files that I needed to be able to easily analyze the data. So I wrote a python script that could scrape all of the data I needed out of the PDFs, and convert them to CSVs. You can find this python script in the main github directory. The median Washington State income by county was easier to access, since it was stored in a single excel file on this website 
https://ofm.wa.gov/washington-data-research/economy-and-labor-force/median-household-income-estimates . I combined these two CSVs by hand, since I was running out of time to complete this project, and the data cleaning was tiresome in R. I actually used my python script to extract 10 years of data, with four quarters for each year, but was having problems analyzing all of the data in R, and decided instead to just analyze the first quarter from 2008 and 2019.

Visualization:

<img src="https://github.com/joejeflef/DataAnalyticsProject/blob/main/2008MedianHousePricevsMedianIncome.PNG">

<img src="https://github.com/joejeflef/DataAnalyticsProject/blob/main/2019MedianHousePricevsMedianIncome.PNG">

<img src="https://github.com/joejeflef/DataAnalyticsProject/blob/main/2008MedianIncomeHistogram.PNG">

<img src="https://github.com/joejeflef/DataAnalyticsProject/blob/main/2019MedianIncomeHistogram.PNG">

<img src="https://github.com/joejeflef/DataAnalyticsProject/blob/main/2008MedianHomePrice.PNG">

<img src="https://github.com/joejeflef/DataAnalyticsProject/blob/main/2019MedianHomePrice.PNG">

Analysis:

