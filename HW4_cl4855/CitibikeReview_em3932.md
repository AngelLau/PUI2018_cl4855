## Question A: 
Verify that the null and alternative hypotheses are formulated correctly

## Response A: 
The null hypothesis is stated correctly in words. Since the idea is that long trips are more likely on weekends than on weekdays, the null hypothesis is that the proportion of long trips on weekends is the same or smaller than the proportion of long trips on weekdays. 

The null hypothesis is set up partially correctly in mathematical format since the proportion of weekday long trips should be greater than or equal to the proportion of weekend long trips. However, since we're testing the proportion of long trips for each sample (weekday trips vs. weekend trips), the fractions should be weekday long trips / **total weekday trips** and weekend long trips / **total weekend trips**. 

The correct mathematical formats for null and alternative hypotheses should be as follows: 

H0: weekend long trips / total weekend trips <= weekday long trips / total weekday trips

H1: weekend long trips / total weekend trips > weekday long trips / total weekday trips 

A significance level was included (alpha = 0.05) which is also part of correctly stating the null hypothesis. 

## Question B: 
Verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

## Response B: 
The data supports the project. The data has the appropriate features needed to answer the question - date and trip duration. The data was partially pre-processed to extract the needed values. 'Starttime' was converted to 'date', and 'duration' was left as is. One additional step would be to prepare the data for statistical testing. To prepare the data for statistical testing, I would recommend splitting the data into 'weekend trips' and 'weekday trips', since weekend riders and weekday riders are the samples being compared. 


## Question C:
Choose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell. 

## Response C: 
I would use the Chi-Square test to test H0. I would use the Chi-Square test because we are answering the question,'Is there a difference between groups that are unpaired?'. The two groups - weekday riders and weekend riders - are unpaired. The dependent variabel is a categorical variable - long trip vs. not long trip. Based on the table [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3116565/), when we have categorical data and we're answering the question "Is there a difference between groups that are unpaired?' we should use the Chi-Square test. 

This models the way the Chi-Square test was used in assignment 3 - to compare the percentage of prisoners who were employed after release for the control group and the program group. Here, we can use the Chi-Square test to compare the percentage of long trips on the weekends vs. on weekdays.  

One variation or additional step that I would recommend would be to do some analysis on trip duration before deciding that 10 minutes defines a 'long trip'. From the bar chart showing distribution of trip duration, we can see that on nearly every day of the week, the proportion of 'long trips' is significantly higher than the proportion of 'short trips'. I would recommend looking at the distribution of trip duration on weekdays during commuting hours to get an idea of how long commuting trips typically take. Then, a more informed threshold can be set for 'long trip'.

I would also recommend using both a cold month and a warm month to control for seasonality, since people might not want to commute to work on a bike in the cold. 