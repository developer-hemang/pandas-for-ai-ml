# 📈 Pandas Series

A **Pandas Series** is a one-dimensional labeled data structure that can store a sequence of values along with an associated index.

It is one of the fundamental data structures in Pandas and is commonly used to represent a **single column or sequence of data**.

---

## 📚 Contents

* [What is Pandas Series?](#-what-is-pandas-series)
* [Why Use Pandas Series?](#-why-use-pandas-series)
* [Series Structure](#-series-structure)
* [How to Create a Series](#-how-to-create-a-series)
* [Index and Values](#-index-and-values)
* [Series Data Types](#-series-data-types)
* [Series in AI/ML](#-series-in-aiml)
* [Practical Implementation](#-practical-implementation)

---

## 🧠 What is Pandas Series?

A **Pandas Series** is a one-dimensional labeled array capable of holding different types of data such as integers, floating-point numbers, strings, dates, and more.

A Series contains two main components:

```text
Index   →   Labels identifying each value
Values  →   Actual data stored in the Series
```

For example:

```text
Index    Value
  0       10
  1       20
  2       30
```

In Python:

```python
import pandas as pd

data = pd.Series([10, 20, 30])
```

Output:

```text
0    10
1    20
2    30
dtype: int64
```

Here:

* `0, 1, 2` → Index
* `10, 20, 30` → Values
* `int64` → Data type

### 📌 Simple Definition

> **A Pandas Series is a one-dimensional labeled data structure used to store and work with a sequence of values.**

---

## 🤔 Why Use Pandas Series?

A Series provides a convenient way to work with a single sequence of data while keeping an associated index.

It is useful when you need to:

* Store a single column of data
* Access values using labels or positions
* Perform mathematical operations
* Filter data
* Handle missing values
* Perform statistical operations
* Work with time-series values
* Prepare individual features for analysis or machine learning

For example, a dataset may contain:

```text
Name       Age       Salary
John       25        50000
David      30        65000
Alex       28        58000
```

Each column can conceptually be represented as a Series:

```text
Name    → Series
Age     → Series
Salary  → Series
```

This is why understanding Series is important before working deeply with Pandas DataFrames.

---

## 🏗️ Series Structure

A Series can be visualized as:

```text
        Index       Values
          ↓           ↓

          0           10
          1           20
          2           30
          3           40
```

The general structure is:

```python
pd.Series(data, index=index)
```

For example:

```python
import pandas as pd

data = pd.Series(
    [100, 200, 300],
    index=["A", "B", "C"]
)
```

Output:

```text
A    100
B    200
C    300
dtype: int64
```

Here the index is explicitly defined:

```text
A → 100
B → 200
C → 300
```

---

## ⚙️ How to Create a Series

A Series can be created from different Python data structures.

### From a List

```python
import pandas as pd

data = pd.Series([10, 20, 30, 40])
```

### From a List with Custom Index

```python
data = pd.Series(
    [10, 20, 30],
    index=["A", "B", "C"]
)
```

### From a Dictionary

```python
data = pd.Series({
    "Apple": 150,
    "Microsoft": 420,
    "Google": 180
})
```

The dictionary keys become the Series index.

---

## 🔢 Index and Values

Every Series contains an index and values.

You can access them using:

```python
data.index
```

and:

```python
data.values
```

Example:

```python
import pandas as pd

data = pd.Series(
    [100, 200, 300],
    index=["A", "B", "C"]
)

print(data.index)
print(data.values)
```

The index identifies **where or how the data is labeled**, while the values contain the actual data.

---

## 🧮 Series Operations

Pandas allows mathematical and analytical operations directly on Series.

```python
import pandas as pd

prices = pd.Series([100, 200, 300])

print(prices.mean())
print(prices.sum())
print(prices.max())
print(prices.min())
```

You can also perform element-wise operations:

```python
prices * 2
```

Result:

```text
0    200
1    400
2    600
```

This makes Series useful for efficient data manipulation and analysis.

---

## 🔍 Filtering a Series

Series can be filtered using conditions.

```python
prices = pd.Series([100, 200, 300, 400])

high_prices = prices[prices > 200]
```

Result:

```text
2    300
3    400
```

This type of filtering is frequently used during data analysis and preprocessing.

---

## 🧠 Series in AI/ML

Series are relevant to AI/ML because individual dataset columns are commonly represented as Pandas Series.

For example, consider financial data:

```text
Date        Open    High    Low    Close
01-09       100     105     98     103
02-09       103     108     101    107
03-09       107     110     104    109
```

The `Close` column can be represented as a Series:

```python
close_prices = df["Close"]
```

Now `close_prices` is a Pandas Series.

This can be used for operations such as:

```python
returns = close_prices.pct_change()
```

The resulting Series can become part of a feature-engineering workflow.

### Typical AI/ML Flow

```text
Raw Dataset
     ↓
Pandas DataFrame
     ↓
Select Column
     ↓
Pandas Series
     ↓
Clean / Transform
     ↓
Feature Engineering
     ↓
NumPy / Scikit-learn
     ↓
ML Model
```

### Example

A financial ML workflow might calculate a return feature:

```python
df["return"] = df["Close"].pct_change()
```

Here, `df["Close"]` is a Series, and the resulting calculation produces another Series that can be added back to the DataFrame.

Series can therefore be useful for:

* 📊 Feature analysis
* 🧹 Data cleaning
* 🔄 Data transformation
* 📈 Time-series analysis
* 💰 Financial data processing
* 🧠 Feature engineering
* 🤖 Preparing ML features

---

## 🧪 Practical Implementation

The concepts covered in this section are implemented in Python.

### Python Implementation

📄 [Open `series.py`](./series.py)

The implementation demonstrates practical examples of:

* Creating a Series
* Custom indexes
* Accessing values
* Working with indexes
* Data types
* Mathematical operations
* Filtering
* Basic Series analysis

The README focuses on **concepts and explanations**, while `series.py` contains the **executable Python examples**.

---

## 🔗 Related Concepts

Series is one of the fundamental building blocks of Pandas and provides the foundation for understanding how Pandas works with one-dimensional data.

Next, we will build on this foundation with additional Pandas concepts.

---

