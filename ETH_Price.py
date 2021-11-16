import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# we're going to be using ETH price data from Nasdaq, you can download the data at:
# https://www.nasdaq.com/market-activity/cryptocurrency/eth/historical

df = pd.read_csv('ETH_Historical_Data_1Y.csv')

# delete column, every value is n/a
del df['Volume']


# function to change 'Date' column into datetime object
def string_to_date(date_string):

    # split string into month, date, year
    date = date_string.split('/')

    # Date column shows up as string MM/DD/YYYY
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])

    # create datetime object
    date_time = datetime(year, month, day)

    # return object
    return date_time


# rename column
df['Close'] = df['Close/Last']


# create column to track daily change
df['Daily Change'] = df['Open'] - df['Close']


# use daily change column to caldulate percent change column
df['Daily % Change'] = df['Daily Change'] / ((df['Open'] + df['Close']) / 2) * 100


# create a raw date list to be used to convert date strings into datetime objects
raw_dates = df['Date'].values
dates = []


# iterate through raw dates and change them to datetime objects
# populate dates list with new datetime objects
for i in raw_dates:

   date = string_to_date(i)
   dates.append(date)

# set new column to array of datetime objects
df['Date'] = dates


# create a column to keep track of monthly average with rolling() method
df['Monthly Average'] = df['Open'].rolling(30).mean()


# change the index to the 'Date' column populated with datetime objects
df.set_index('Date', inplace=True)

# Flip the data so that we are going from past -> present
df.sort_values(by='Date', ascending=False, inplace=True)

# change style to 'ggplot'
plt.style.use('ggplot')

# create a figure object to create subplots
fig = plt.figure()

# create two subplots, one above another
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# on top plot Opening price across time, with Monthly Average price overlaying
ax1.plot(df.index, df.Open)
ax1.plot(df.index, df['Monthly Average'])

# set titles and add a legend
ax1.set_title('Historical ETH Price Data', fontsize=12)
ax1.legend(['Daily Price', 'Monthly Average'])

# reformat x-ticks
for tick in ax1.get_xticklabels():
    tick.set_rotation(20)
    tick.set_fontsize(8)

# on bottom plot Daily Percent Change as volatility measure
ax2.plot(df.index, df['Daily % Change'])

# set titles and add a lenend
ax2.set_title('Historical ETH Price Volatility', fontsize=12)
ax2.legend(['Daily Volatility'])

# reformat x-ticks
for tick in ax2.get_xticklabels():
    tick.set_rotation(20)
    tick.set_fontsize(8)

fig.tight_layout(pad=1.08)

plt.show()


