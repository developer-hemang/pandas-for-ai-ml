import pandas as pd

# Creat simple pandas series from a list 

age = [12,12,33,22]

ageSeries = pd.Series(age);
# print(ageSeries)


""" output will be , 
0    12
1    12
2    33
3    22
dtype: int64

If nothing else is specified, the values are labeled with their index number
"""

# This label can be used to access a specified value.

# print(ageSeries[0]) # output will be 12 


# create labels (with index argument we can create labes )

SeriesOfAge = pd.Series(age,index=["Hemang","Jigar","Hardik","Meet"])

# print(SeriesOfAge)

""" Output will be

Hemang    12
Jigar     12
Hardik    33
Meet      22
dtype: int64

"""
# you can get age by lable 
# print(SeriesOfAge['Hemang']) # output will ve 12


# key/value pair object  as Series 

"""
we can also create key value pair object like dictionary as series.
"""

stockReturns = {"day1":"2%","day2":"2.5%","day3":"5%"}

stockReturnsSeries = pd.Series(stockReturns)

print(stockReturnsSeries)

""" output will be
day1      2%
day2    2.5%
day3      5%
dtype: object

The keys of the dictionary become the labels.
"""
 