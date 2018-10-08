# Assignment 1: Review your classmate's Citibike project proposal

## a. verify that their Null and alternative hypotheses are formulated correctly

The Null and alternative hypotheses are formulated correctly. And it's a very good idea to think about the differece of customers' proportion between weekdays and weekends. However, the mathematical formulation is not being visualized in ADRF notebook. We may alter the syntax like:

_$H_0$ : $\frac{Customers_{\mathrm{weekend}}}{Totalriders_{\mathrm{weekend}}} <= \frac{Customers_{\mathrm{weekday}}}{Totalriders_{\mathrm{weekday}}}$

_$H_1$ : $\frac{Customers_{\mathrm{weekend}}}{Totalriders_{\mathrm{weekend}}} > \frac{Customers_{\mathrm{weekday}}}{Totalriders_{\mathrm{weekday}}}$

## b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)
It's very good to drop all those NA data to make the dataset clean. And the data has the appropriate features to answer teh question.

But the dataset is from August. So it may be more tourists come to NYC and using citibikes which can influence the test results. We may use the whole year data(but since the requirement said that we can use 1 or 2 month data). Or we can add some limitation factor to the hypotheses.

## c. chose an appropriate test to test H0 given the type of data, and the question asked. 


The data we have here is categorical data and is from 2 sample(weekdays and weekends). And also the standard deviation is unknown. So we will use the 2 sample t-test.






