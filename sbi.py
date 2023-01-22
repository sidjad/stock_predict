import pandas as pd
import talib
import  mplfinance as fplt

# Read CSV 
sbi_df = pd.read_csv("output.csv",index_col=0, parse_dates=True)

# Define Time Range
dt_range = pd.date_range(start="2021-01-03", end="2023-01-19")
sbi_df = sbi_df[sbi_df.index.isin(dt_range)]

#Combine in all input in  sbi_df variable
sbi_df.head()

# Creating a Indicator variable
sbi_df["SMA"] = talib.SMA(sbi_df.Close, timeperiod=20)

sbi_df["RSI"] = talib.RSI(sbi_df.Close, timeperiod=21)

sbi_df["EMA_50"] = talib.EMA(sbi_df.Close, timeperiod=50)

sbi_df['UP_BB'], sbi_df['MID_BB'], sbi_df['LOW_BB'] = talib.BBANDS(sbi_df.Close, nbdevup=2, nbdevdn=2, matype=0,timeperiod=20)

#Combine in all Indicator in sbi_df variable
sbi_df.head()

# Created Variable to plot in new variable
sma = fplt.make_addplot(sbi_df[["SMA", "EMA_50"]])
bb = fplt.make_addplot(sbi_df[["UP_BB","MID_BB","LOW_BB"]])

#Plot all the above data
fplt.plot(
    sbi_df,
    type='candle',
    addplot = [sma,bb],
    title='SBIN, July- 2017',
    ylabel='Price in (₹)'
    )

# Generate Signal 

#compare 20 SMA & 50 SMA cross location with closed candle

#compare previous closed candle and current closed candle 

# if candle is closed higher than previous closed and equal or above the BB above band or  20 SMA is above 50 SMA and RSI is between 50-60 == BUY

# if candle is closed lower than previous closed and equal or below the BB above band or  20 SMA is below 50 SMA and RSI is between 80-65 == SELL 
    
