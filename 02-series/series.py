import pandas as pd


# create Simple Pandas Series From List

OHLCVData = [100,130,95,102,120000];

OhlcvSeries = pd.Series(OHLCVData)

# print(OhlcvSeries) 

""" Output will be
0       100
1       130
2        95
3       102
4    120000
dtype: int64

>>> If nothing else is specified, the values are labeled with their index number
>>> This label can be used to access a specified value.
"""

# print(OhlcvSeries[0]) # output will be  100


# create labels (with index argument we can create labes )

OhlcvSeriesWithLabel = pd.Series(OHLCVData,index=["OPEN","HIGH","LOW","CLOSE","VOLUME"])

# print(OhlcvSeriesWithLabel)

""" Output Will Be 
100
OPEN         100
HIGH         130
LOW           95
CLOSE        102
VOLUME    120000
dtype: int64
"""

# When you have created labels you can access an item by referring to the label.

# print(OhlcvSeriesWithLabel["OPEN"])


# You can Create Series from Key Value Object Like Dictionary 

OhlcvDictionary = {
    "OPEN":100,
    "HIGH":102,
    "LOW":97,
    "CLOSE":99
}

OhlcvDictionarySeries = pd.Series(OhlcvDictionary)
print(OhlcvDictionarySeries)