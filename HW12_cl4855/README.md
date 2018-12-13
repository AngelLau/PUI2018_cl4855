# HW12 

## Assignment 1
Find periodicity with Fourier Transforms in the time series from HW11. Comment on what you find: what are the most significant periods? 

In this notebook, I sum all the card types data so I got 600 stations in 194 weeks data. Then I standardized the dataset and did fourier transformation. Because we want to know what is the trend for annual year which is 52 weeks. I focused on 52 weeks peaks to see which time series has the values that larger than the others. Credit to Tiffanay here for helping me know where should I look at.


## Assignent 2  
Cluster zipcodes based on the economic development (business counts) in time for 1993-2006 Clustering often takes time, particularly hierarchical clustering. Dont start at the last minute! Comment on patterns you see: which zipcodes have similar time evolution in the number of businesses? what are peculiar the characteristics in the economic evolution of each cluster ? upward trends, downward trends, inflection points, discontinuities? 

In this notebook, I tried to use curl to pull the sequence dataset. But I didn't figure it out how to download raw data with curl so I used urlib. Here credits to Rohun for teaching me how to pull the data. And then I make a dictionary convert all datasets columns to lower case then put each of them in dictionary. Kept zip code and each year columns so that I got the time series of 21 years for each zip code. After merging with NYC zipcodes dataset, I got those time series in NYC.
After standardized dataset I did K-mean cluster, affinity propagation cluster and agglomerative clustering along with the dandrogram.