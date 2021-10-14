import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('ETH_Historical_Data.csv')

del df['Volume']

# update

# Date column shows up as string MM/DD/YYYY
def string_to_date(date_string):

    # split string into month, date, year
    date = date_string.split('/')

    month = int(date[0])
    day = int(date[1])
    year = int(date[2])

    date_time = datetime(year, month, day)

    return date_time


# create a raw date list to be used to convert date strings into datetime objects
raw_dates = df['Date'].values
dates = []

# iterate through raw dates and change them to datetime objects
# populate dates list with new datetime objects
for i in raw_dates:
   date = string_to_date(i)
   dates.append(date)

# set new column to
df['Date'] = dates

df['Monthly Average'] = df['Open'].rolling(30).mean()

df.set_index('Date', inplace=True)

df.sort_values(by='Date', ascending=False, inplace=True)

plt.style.use('ggplot')

plt.plot(df.index, df.Open)
plt.plot(df.index, df['Monthly Average'])

plt.legend()
plt.title('Historical ETH Price Data')

plt.xticks(rotation=45)


plt.show()


