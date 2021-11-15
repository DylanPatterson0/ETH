import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
#import ETH_Price_Updates

#market_stats = ETH_Price_Updates.get_market_data()


df = pd.read_csv('ETH_Historical_Data_1Y.csv')

# delete column, every value is n/a
del df['Volume']


# Date column shows up as string MM/DD/YYYY
def string_to_date(date_string):

    # split string into month, date, year
    date = date_string.split('/')

    month = int(date[0])
    day = int(date[1])
    year = int(date[2])

    date_time = datetime(year, month, day)

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

# set new column to
df['Date'] = dates

df['Monthly Average'] = df['Open'].rolling(30).mean()
df['Weekly Average'] = df['Open'].rolling(7).mean()

df.set_index('Date', inplace=True)

df.sort_values(by='Date', ascending=False, inplace=True)

plt.style.use('ggplot')

fig = plt.figure()

ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.plot(df.index, df.Open)
ax1.plot(df.index, df['Monthly Average'])

ax1.set_title('Historical ETH Price Data', fontsize=12)
ax1.legend(['Daily Price', 'Monthly Average'])

for tick in ax1.get_xticklabels():
    tick.set_rotation(20)
    tick.set_fontsize(8)


ax2.plot(df.index, df['Daily % Change'])
ax2.legend(['Daily Volatility'])
ax2.set_title('Historical ETH Price Volatility', fontsize=12)
for tick in ax2.get_xticklabels():
    tick.set_rotation(20)
    tick.set_fontsize(8)

fig.tight_layout(pad=1.08)

plt.show()


