#Open a new python script or notebook or ipython file
#Load in any dataset you like
#Find a extension that will allow you to see the data in a data viewer
#Load the extension and view the data
import pandas as pd
data = pd.read_csv("ClassData.csv")
print(data.head())

import pandas as pd

# Sample dataset using Data Wrangler
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, None, 30],
    "Score": [85, 90, 95]
}

df = pd.DataFrame(data)
print(df)

import plotly
print(plotly.__version__)
