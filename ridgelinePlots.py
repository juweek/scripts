import pandas as pd
import matplotlib.pyplot as plt
from joypy import joyplot 
from pandas.api.types import CategoricalDtype

#to start, we're going to read in the CSV. the usecols command allows us to only get data from certain columns.
#df stands for DataFrame. the head is the top of the DataFame
df = pd.read_csv('weatherAUS.csv', usecols=['Date', 'Location', 'MinTemp', 'MaxTemp'])
df.head()

#in this dataframe, we are quering for rows where the 'Location' column equals Sydney. we store that in an object
sydney = df.query("Location == 'Sydney'")

#once you store the Sydney data into the sydney document, you can drop it
sydney = sydney.drop('Location', axis=1)

#reformat the data as appropriate. first, reformat the Date property to a datetime format. once that's done, you can find the monthname, so we store that as a new variable called Month
sydney['Date'] = sydney['Date'].astype('datetime64')
sydney['Month'] = sydney['Date'].dt.month_name()

sydney.head()

#create a directory of months so you can clean the data up
cat_month = CategoricalDtype(
    ['January', 'February', 'March', 'April', 'May', 'June',
     'July', 'August', 'September', 'October', 'November', 'December']
)

sydney['Month'] = sydney['Month'].astype(cat_month)

sydney.dtypes

#pyplot has the figure command that allows us to create a new figure (kind of like a new canvas)
plt.figure()

#use joyplot to create a ridgeline plot
joyplot(
    data=sydney[['MaxTemp', 'Month']], 
    by='Month',
    figsize=(12, 8)
)

#this is essentially like instantiating the canvas
plt.show()