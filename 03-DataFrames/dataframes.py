import pandas as pd;

# Create Simple DataFrame 

NiftyOhlcvData = {

    "day1":[21060,21150,21000,21150,4000000],
    "day2":[21160,21400,21300,21250,3800000]
}

NiftyDf = pd.DataFrame(NiftyOhlcvData)

""" Output will be
      day1     day2
0    21060    21160
1    21150    21400
2    21000    21300
3    21150    21250
4  4000000  3800000
"""

# print(NiftyDf)


# we can locate Row by Index with the help of loc attribute 

# print(NiftyDf.loc[0]) 

""" Output will be
day1    21060
day2    21160
Name: 0, dtype: int64
This example returns a Pandas Series.
"""


# print(NiftyDf.loc[[0,1]]) 

""" output will be

    day1   day2
0  21060  21160
1  21150  21400

When using [], the result is a Pandas DataFrame.
""" 


# Named Index 

"""
you can name your own indexes with the index argument
"""

NiftyDfWithIndex = pd.DataFrame(NiftyOhlcvData,index=["OPEN","HIGH","LOW","CLOSE","VOLUME"])

print(NiftyDfWithIndex)

""" output will be 

           day1     day2
OPEN      21060    21160
HIGH      21150    21400
LOW       21000    21300
CLOSE     21150    21250
VOLUME  4000000  3800000

"""

# Locate Named Indexes
