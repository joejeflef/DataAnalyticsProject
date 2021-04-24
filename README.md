# A Comparison of Housing Prices vs. Income in Washington Counties from 2008 and 2019
A data analytics project for WSUV.

Motivation:

My goal when analyzing this data, was to see if home prices in the counties of Washington State were correlated to the
median income of the county. With the 2019 real estate market being so hot, I was wondering if the rise in house prices was related to an increase in income, or a 2008 like housing market speculation bubble.

Data Process:

To answer this question I needed to find data on the median price of houses by county in Washington State, and the median income in Washington State. I found historic median house prices by county for Washington on this website https://wcrer.be.uw.edu/archived-reports/ , but the problem was that the data was stored in PDFs, not the CSV files that I needed to be able to easily analyze the data. So I wrote a python script that could scrape all of the data I needed out of the PDFs, and convert them to CSVs. You can find this python script in the main github directory. The median Washington State income by county was easier to access, since it was stored in a single excel file on this website 
https://ofm.wa.gov/washington-data-research/economy-and-labor-force/median-household-income-estimates . I combined these two CSVs by hand, since I was running out of time to complete this project, and the data cleaning was tiresome in R. I actually used my python script to extract 10 years of data, with four quarters for each year, but was having problems analyzing all of the data in R, and decided instead to just analyze the first quarter from 2008 and 2019. I also head to remove Clark and Lincoln countys from the data, because they were incomplete.

Visualization:

<img src="https://github.com/joejeflef/DataAnalyticsProject/blob/main/2008MedianHousePricevsMedianIncome.PNG">

<img src="https://github.com/joejeflef/DataAnalyticsProject/blob/main/2019MedianHousePricevsMedianIncome.PNG">

<img src="https://github.com/joejeflef/DataAnalyticsProject/blob/main/2008MedianIncomeHistogram.PNG">

<img src="https://github.com/joejeflef/DataAnalyticsProject/blob/main/2019MedianIncomeHistogram.PNG">

<img src="https://github.com/joejeflef/DataAnalyticsProject/blob/main/2008MedianHomePrice.PNG">

<img src="https://github.com/joejeflef/DataAnalyticsProject/blob/main/2019MedianHomePrice.PNG">

Analysis:

For the analysis, I wanted to see what effect "Median Income" had on the "Median House Price" so I plotted two scatterplots for 2008 and 2019, and applied a linear regression model to them. The two scatterplots showed that generally speaking, the higher the median income of a county, the higher the home price. But the R-squared value was not particularly high for either 2008, with 0.4465, or 2019, with 0.4769. This indicated that there was more to housing prices in Washington besides just median income. This could also potentially indicate that the housing market is experiencing similar bubble territory that 2008 was experiencing, because of the fact that their R-squared values are so similar. Or this could indicate that housing prices are always around this correlated to median incomes.


