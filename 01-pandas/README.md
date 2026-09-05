# 🐼 Pandas for AI/ML

**Pandas** is an open-source Python library designed for data manipulation, data analysis, and data processing. It provides powerful and flexible tools for working with structured and tabular datasets.

In **AI and machine learning**, Pandas is commonly used during the data preparation stage to load, explore, clean, transform, analyze, and prepare datasets before they are used for feature engineering and model training.

This repository focuses on **practical Pandas concepts relevant to AI/ML workflows**, while also covering general data-analysis use cases.

---

## 🤔 Why Use Pandas?

Working with real-world data often involves missing values, duplicate records, incorrect data types, inconsistent formats, and unnecessary information.

Pandas provides convenient tools to handle these tasks efficiently and helps transform raw datasets into clean and structured data.

In an AI/ML workflow:

```text
Raw Data
   ↓
Load Data
   ↓
Explore Data
   ↓
Clean Data
   ↓
Transform Data
   ↓
Feature Engineering
   ↓
ML-Ready Dataset
```

Pandas is mainly used in the data preparation and analysis stages of this workflow.

---

## 🛠️ What Can Pandas Do?

Pandas can be used for:

* 📥 Loading data from CSV, Excel, JSON, SQL databases, and other sources
* 🔍 Exploring and understanding datasets
* 🧹 Cleaning missing and duplicate data
* 🔄 Transforming and reshaping data
* 🔗 Combining and merging datasets
* 📊 Performing data analysis and aggregation
* 📈 Working with time-series data
* 🧠 Preparing data for machine learning
* ⚙️ Performing feature engineering
* 💾 Reading and writing different data formats

Pandas is useful beyond AI/ML as well, including financial analysis, business analytics, reporting, research, data engineering, and general Python data processing.

---

## 🐙 Where is the Pandas Codebase?

Pandas is an open-source project, and its source code is publicly available on GitHub.

🔗 [Pandas GitHub Repository](https://github.com/pandas-dev/pandas)

The repository contains the Pandas implementation, tests, documentation, development tools, and supporting project files.

Exploring the codebase can also help understand how a large-scale Python open-source project is organized.

---

## 📦 Installation of Pandas

### Using pip

```bash
pip install pandas
```

### Using conda

```bash
conda install pandas
```

After installation, Pandas can be imported into a Python program.

---

## 📥 Import Pandas

Pandas is commonly imported using the `pd` alias:

```python
import pandas as pd
```

Here, `pd` is simply an alias for the `pandas` module.

For example:

```python
import pandas as pd

df = pd.DataFrame()
```

Using `pd` is a widely adopted convention in the Python data-science ecosystem.

---

## 🔢 Checking Pandas Version

The installed Pandas version can be checked using:

```python
import pandas as pd

print(pd.__version__)
```

Checking the version is useful when managing dependencies, troubleshooting compatibility issues, and reproducing Python environments.

---

## 🧠 Pandas in AI/ML

A typical AI/ML workflow can look like:

```text
Data Source
    ↓
CSV / JSON / API / Database
    ↓
🐼 Pandas
    ↓
Data Exploration
    ↓
Data Cleaning
    ↓
Data Transformation
    ↓
Feature Engineering
    ↓
NumPy / Scikit-learn
    ↓
Machine Learning Model
```

Pandas is **not a machine learning library**. Its primary role is to work with, analyze, transform, and prepare data that can later be used by machine learning libraries and models.

---

📚 Next

Continue with the detailed concepts of Pandas Series:

👉 Pandas Series →
[Learn Pandas Series →](./02-series/README.md)

---


