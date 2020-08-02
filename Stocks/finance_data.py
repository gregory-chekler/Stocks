#!/usr/bin/python
#finance_data.py

'''Holds functions that preform specific tasks related to stocks'''

__version__ = "1.0.0"
__author__ = 'Gregory Chekler'

import yfinance as yf
import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', None)
pandas.set_option('display.max_colwidth', -1)

def current_price(stock):
    """determines current stock price of a certain stock
    
    :param stock: stock that will be analyzed
    :return current stock price"""
    
    stock = yf.Ticker(str(stock))
    hist = str(stock.history(period=("1h")))
    l = hist.split() #List form of hist split into individual words
    stock = yf.Ticker(str(stock))
    current_price = l[13] #number in list that is stock price
    return current_price
    

def information(stock):
    """gets current information about a certain stock
    
    :param stock: stock that will be analyzed
    :return stock information"""
    
    stock = yf.Ticker(str(stock))
    return stock.info

def history(stock, time):
    """determines current stock price of a certain stock
    
    :param stock: stock that will be analyzed
    :param time: time period of data collected
    :return stock history in time period"""
        
    stock = yf.Ticker(str(stock))
    hist = str(stock.history(period=(str(time)) + "mo"))
    return hist

def trend(stock, time):
    """determines current stock trends within a time period
    
    :param stock: stock that will be analyzed
    :param time: time period of data collected
    :return stock trend in time period"""
    
    stock = yf.Ticker(str(stock))
    hist = str(stock.history(period=(str(time)) + "mo"))

    open_price = []
    high_price = []
    low_price = []
    close_price = []
    

    l = hist.split() #List form of hist split into individual words

    ############################################
    ### CREATES LISTS OF FINANCIAL DATA PER DAY
    ############################################
    START_OF_LIST = 10
    INTERVAL = 8
    END_OF_LIST = len(l) - 6

    for i in range(START_OF_LIST, END_OF_LIST, INTERVAL):
        open_price.append(l[i])

    for i in range(START_OF_LIST + 1, END_OF_LIST + 1, INTERVAL):
        high_price.append(l[i])

    for i in range(START_OF_LIST + 2, END_OF_LIST + 2, INTERVAL):
        low_price.append(l[i])

    for i in range(START_OF_LIST + 3, END_OF_LIST + 3, INTERVAL):
        close_price.append(l[i])

    
    #################
    ### LOW COUNTER
    #################
    low_counter = 0
    lowest_price = float(low_price[0])
    for i in range(len(low_price)):
        if float(low_price[i]) < float(lowest_price):
            low_counter = low_counter + 1
            lowest_price = float(low_price[i])
    #################
    ### HIGH COUNTER
    #################
    high_counter = 0
    highest_price = high_price[0]
    for i in range(len(high_price)):
        if float(high_price[i]) > float(highest_price):
            high_counter = high_counter + 1
            highest_price = float(high_price[i])
    
    
    #############
    ### LOW TREND
    #############
    if low_counter > high_counter: #Low trend
        if abs(low_counter - high_counter) > 5: #difference in # of lows vs. highs is big
            return "Strong Low trend"
        if abs(low_counter - high_counter) <= 5: #difference in # of lows vs. highs is small
            return "Weak Low trend"
    #############
    ### HIGH TREND
    #############

    if low_counter < high_counter: #high trend
        if abs(high_counter - low_counter) > 5: #difference in # of lows vs. highs is big
            return "Strong High trend"
        if abs(high_counter - low_counter) <= 5: #difference in # of lows vs. highs is small
            return "Weak High trend"
    



###########################
### Volume interpreter
###########################
def volume(stock, time):
    """analyzes current stock volume within a time period
    
    :param stock: stock that will be analyzed
    :param time: time period of data collected
    :return stock volume analysis in time period"""
    
    stock = yf.Ticker(str(stock))
    hist = str(stock.history(period=(str(time)) + "mo"))
    l = hist.split() #List form of hist split into individual words
    START_OF_LIST = 10
    INTERVAL = 8
    END_OF_LIST = len(l) - 6
    volume = []
    open_price = []
    
    for i in range(START_OF_LIST, END_OF_LIST, INTERVAL):
        open_price.append(l[i])
    
    for i in range(START_OF_LIST + 4, END_OF_LIST + 4, INTERVAL):
        volume.append(l[i])

    #Low Volume is considered bad, high volume is good
    if volume[-1] == volume[-2]:
        return "Equal Volume"
    if volume[-1] < volume[-2]: #Low volume
        return "Low Volume"
    if volume[-1] > volume[-2]: #High volume
        if open_price[-1] > open_price[-2]:
            return "High Volume: Buy"
        if open_price[-1] < open_price[-2]:
            return "High Volume: Sell"


    
def change_during_day(stock, time):
    """determines average percent change in a day
    
    :param stock: stock that will be analyzed
    :param time: time period of data collected
    :return average percent change in a day for a certain time period"""
    
    START_OF_LIST = 10
    END_OF_LIST = 169
    INTERVAL = 8
    stock = yf.Ticker(str(stock))
    hist = str(stock.history(period=(str(time)) + "mo"))

    open_price = []
    close_price = []
    percent_change_during = []  # % change during day
    percent_change_day = [] # % change from day to day
    

    l = hist.split() #List form of hist split into individual words

    ############################################
    ### CREATES LISTS OF FINANCIAL DATA PER DAY
    ############################################
    
    START_OF_LIST = 10
    INTERVAL = 8
    END_OF_LIST = len(l) - 6

    for i in range(START_OF_LIST, END_OF_LIST, INTERVAL):
        open_price.append(l[i])

    for i in range(START_OF_LIST + 3, END_OF_LIST + 3, INTERVAL):
        close_price.append(l[i])

    ###########################
    ### PERCENT CHANGE IN A DAY
    ###########################
    # These lines of code get a percent change in a day and then
    # average it out for a period of time 
    change = 0
    for i in range(len(close_price)):
        change = abs(((float(close_price[i]) - (float(open_price[i]))) /
                      float(close_price[i]))) * 100
        percent_change_during.append(float(change))
        
    change_during = 0
    for i in range(len(close_price)):
        change_during = percent_change_during[i] + change_during
    
    average_change_during = 0
    average_change_during = change_during / len(close_price)
    
    return average_change_during
  

def change_per_day(stock, time):
    """determines average percent change per day
    
    :param stock: stock that will be analyzed
    :param time: time period of data collected
    :return average percent change per day for a certain time period"""
    
    START_OF_LIST = 10
    END_OF_LIST = 169
    INTERVAL = 8
    stock = yf.Ticker(str(stock))
    hist = str(stock.history(period=(str(time)) + "mo"))

    open_price = []
    close_price = []
    percent_change_during = []  # % change during day
    percent_change_day = [] # % change from day to day
    

    l = hist.split() #List form of hist split into individual words

    ############################################
    ### CREATES LISTS OF FINANCIAL DATA PER DAY
    ############################################
    START_OF_LIST = 10
    INTERVAL = 8
    END_OF_LIST = len(l) - 6

    for i in range(START_OF_LIST, END_OF_LIST, INTERVAL):
        open_price.append(l[i])

    for i in range(START_OF_LIST + 3, END_OF_LIST + 3, INTERVAL):
        close_price.append(l[i])

    ###########################
    ### PERCENT CHANGE IN A DAY
    ###########################
    # These lines of code get a percent change in a day and then average
    # it out for a period of time
    change = 0
    for i in range(len(close_price)):
        change = abs(((float(close_price[i]) - (float(open_price[i]))) /
                      float(close_price[i]))) * 100
        percent_change_during.append(float(change))

    change = 0
    for i in range(len(close_price) - 1):
        change = abs(((float(percent_change_during[i]) -
                       (percent_change_during[i + 1])) /
                      float(percent_change_during[i])))
        percent_change_day.append(float(change))
        
    change_during = 0
    for i in range(len(close_price) - 1):
        change_during = percent_change_day[i] + change_during
    
    average_change_day = 0
    average_change_day = change_during / len(close_price)
    
    return average_change_day

# show cashflow
def quarterly_cashflow(stock):
    """gets the quarterly cashflow of a certain company
    
    :param stock: stock that will be analyzed
    :return quarterly cashflow"""
    stock = yf.Ticker(str(stock))
    return stock.quarterly_cashflow

# show earnings
def quarterly_earnings(stock):
    """gets the quarterly earnings of a certain company
    
    :param stock: stock that will be analyzed
    :return quarterly earnings"""
    
    stock = yf.Ticker(str(stock))
    return stock.quarterly_earnings

# show sustainability
def sustainability(stock):
    """gets the sustainablity of a certain company
    
    :param stock: stock that will be analyzed
    :return sustainability"""
    
    stock = yf.Ticker(str(stock))
    return stock.sustainability

# show analysts recommendations
def analyst_recommendation(stock):
    """gets the analyst recomendations of a certain company
    
    :param stock: stock that will be analyzed
    :return analyst recommendations"""
    stock = yf.Ticker(str(stock))
    return stock.recommendations


#### Calculating good news vs. Bad News ####
def news(stock):
    """analyzes analyst recommendations using keywords and assigns values to them
    
    :param stock: stock that will be analyzed
    :return recommendations value"""
    stock = yf.Ticker(str(stock))
    reco = str(stock.recommendations) # Stands for recomend
    reco = reco.split()
    reco.reverse()
    del reco[15 :-1]
    
    #### KEY WORDS ###
    
    buy = reco.count("Buy") #Means price is going up = Good
    sell = reco.count("Sell") #Means price is going down = Bad
    hold = reco.count("Hold") #Means price is going to increase = Good
    neutral = reco.count("Neutral") #Means price is not going to drastically change = Neutral
    overweight = reco.count("Overweight") #Means stock is better value for money than others = Good
    equalweight = reco.count("Equal-Weight") #Means stock is about the same value compared to others = Neutral
    underweight = reco.count("Underweight") #Means stock is worse value than what it is assesed to be = Bad
    perform = reco.count("Perform") #Means stock performance is on par with the industry average = Neutral
    outperform = reco.count("Outperform") #Means stock performance will be slightly better than industry = Good
    underperform = reco.count("Underperform") #Means stock performance will be slightly worse than industry = Bad
    if (buy + hold + neutral + equalweight + overweight + outperform) == 0:
        news = .95 / (sell + underweight + perform + underperform)
    elif (sell + underweight + perform + underperform) == 0:
        news = 1.05 * (buy + .5 * hold + .1 * neutral + .1 * equalweight +
                       overweight + outperform)
    else:
        news = (buy + .5 * hold + .1 * neutral + .1 * equalweight + overweight +
                outperform)/(sell + underweight + perform + underperform)
    if news < 1:
        if news < .5:
            news = 1 - news
    return news



#show next event (earnings, etc)
def calendar(stock):
    """gives the calendar of important events for a company
    
    :param stock: stock that will be analyzed
    :return events"""
    stock = yf.Ticker(str(stock))
    return stock.calendar
      
def predictor(stock, time):
    """predicts future stock price
    
    :param stock: stock that will be analyzed
    :param time: time period that is used
    :return future stock price"""
    # Interprets trends into numbers
    if trend(stock, time) == "Weak Low trend":
        trends = .995
    if trend(stock, time) == "Weak High trend":
        trends = 1.005
    if trend(stock, time) == "Strong Low trend":
        trends = .99
    if trend(stock, time) == "Strong High trend":
        trends = 1.01

    current = float(current_price(stock))
    
    # Interprets volume into numbers
    if volume(stock, time) == "High Volume: Sell":
        vol = .9875
    if volume(stock, time) == "High Volume: Buy":
        vol = 1.015
    if volume(stock, time) == "Equal Volume":
        vol = 1
    if volume(stock, time) == "Low Volume":
        vol = .99
    
    change = float(change_per_day(stock, time) / 100)
        
    prediction = "$" + str(current * trends * vol) + " within a range of $" + str(
        current * (change))
    return prediction

# Big thank you to Mr. Beckwith for helping figure out some of the collection of data
# as well as Ran Aroussi for creating yfinance