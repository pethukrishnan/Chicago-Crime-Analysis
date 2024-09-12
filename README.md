# Chicago Crime Analysis

Here I performed an analysis of crime within Chicago based on publicly provided data from the city of Chicago. My main goal was to learn more about crime throughout Chicago by exploring the data and then to build a dashboard using Power BI to allow others to also explore the data.


## Data Preprocessing

As of 3/10/2020, the [dataset](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2) provided by the city of Chicago on crime (excluding murders) contains over 7 millions rows and 22 columns. This [dataset](#https://data.cityofchicago.org/Public-Safety/Homicides/k9xv-yxzs) contained the homicides, about 10,000, from the last 20 years. To facilitate early exploration of the data and focus on more recent, relevant trends, I removed crimes from before 2010, unneeded columns, and rows with nulls. The reduced dataset contained just under 3 million rows of crimes  

After reducing the size of the dataset, I cleaned up the text columns by manually matching values of each column with a smaller subset of categories in excel, mapped the Community Area ID's to their name and group (e.g. Community Area 8 maps to Near North Side and Central) based on [this](https://en.wikipedia.org/wiki/Community_areas_in_Chicago) Wikipedia page, and added some categorical columns based on the date of the crime.  

Also added in the Community Area population sizes from the [2010 Census](https://www.chicago.gov/content/dam/city/depts/zlup/Zoning_Main_Page/Publications/Census_2010_Community_Area_Profiles/Census_2010_and_2000_CA_Populations.pdf) to allow for an approximated Crimes/Homicides per Capita calculation. Unfortunately, this data isn't provided year over year and as of 3/30/2020, the 2020 Census isn't available, which is why I needed to use 2010 population sizes.


## Data Exploration

I performed a brief exploratory analysis of the cleaned dataset. I looked at a few different columns in the cleaned dataset to get an initial idea of whether or not they would be helpful features for predicting whether there will be an arrest for a new crime. The columns I believe will be most helpful are the community area, type of crime, and the year the crime occurred.

I also explored the raw counts of crimes and homicides, along with the per capita counts, to see if there were any interesting trends. One of the most interesting trends I want to point out is how the raw counts of crimes and homicides can be deceiving. Looking specifically at the plots showing the Community Areas with the Least and Most Crimes with both the raw counts and crimes per capita in the All Crimes and Homicides by Community Area section, we can see that Fuller Park is among the community areas with the least amount of crime, but when looking at the crimes per capita (the raw counts divided by the 2010 Census population sizes), Fuller Park has more crime per capita than all the  community areas in Chicago.  

Another thing I found interesting was the low arrest rate. The arrest rate for all crimes in the city of Chicago was only 24.96%, which shocked me. The arrest rate for homicides was higher at 37.18% but still lower than I thought it would be (though that's probably because I've been watching too many unrealistic cop shows).
```

