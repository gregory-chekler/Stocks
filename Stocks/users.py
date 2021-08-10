#!/usr/bin/python
# users.py

'''creates class called User, Stock, and Portfolio that has user related modules'''

__author__ = "Gregory Chekler"
__version__ = "1.1.0"

import finance_data as f
import pickle
import datetime

users = []
filename = 'user_data.txt'


# def save_info(): #uses pickle module to save data
#     print(users)
#     filename = 'user_data.txt'
#     outfile = open(filename, 'wb')
#     pickle.dump(users, outfile)
#     outfile.close()

def save_info():
    """saves the user information input during program use

    :return: saves data in user_data.txt
    """
    saving_list_level_one = [] #saves the users info including list
    saving_list_level_two = [] #highest level contains all user info
    saving_list_level_three = [] #contains the stocks user holds
    file = open(filename, 'wb')
    for i in range(len(users)): #saves data for each user in users
        saving_list_level_one = [] #resets list for each user
        saving_list_level_three = [] #resets list for each user
        saving_list_level_one.append(users[i].name)
        saving_list_level_one.append(users[i].bought_at)
        saving_list_level_one.append(users[i].success_rate)
        saving_list_level_one.append(users[i].total_stocks_bought)

        [saving_list_level_three.append([users[i].list[x].ticker,
                                        users[i].list[x].shares,
                                        users[i].list[x].prediction,
                                        users[i].list[x].date])
         for x in range(len(users[i].list))] #creates list of stocks and shares that each user has


        saving_list_level_one.append(saving_list_level_three) #appends list of stocks in another list
        saving_list_level_two.append(saving_list_level_one) #the previous list is appended to create usable format
    pickle.dump(saving_list_level_two, file) #saves data
    file.close()


    #How it will look: [[user1, bought_at_1, [ticker1, shares1, prediction1, date1]],
    # [user2, bought_at_2, [ticker2, shares2, prediction2, date2]]]
def create_user(name):
    """creates a user object and adds it to list users

    :param name: users name
    :return: a created user
    """
    vars()[str(name)] = User(str(name))
    users.append((vars()[name])) #appends the name as a variable
    return "User created"

def select_user(name): #used when there are many users and a specific one is desired
    """selects a user from list of users

    :param name: desired user to be selected
    :return: the user object
    """
    for i in range(len(users)):  # finds desired account
        if users[i].name == name:
            name = users[i] #changes name from string to object
    return name #this is the user object


class User():
    def __init__(self, name):
        """constructor

        :param name: user's name
        """
        self.name = name
        self.list = []  # list of stocks
        self.bought_at = 0 #compiles all prices of stocks when bought together/used for ROI
        self.ROI = 0
        self.current_total = 0 #current value of portfolio
        self.success_rate = 0
        self.total_stocks_bought = 0



    def add_stock(self, ticker, shares):
        """adds stock with certain number of shares to user's portfolio

        :param ticker: the name of the stock
        :param shares: number of shares
        :return: adds the stock to the user's portfolio/list
        """
        try:
            vars()[str(ticker)] = Stock(str(ticker), int(shares))
        except: #if there is no ticker of that name
            return "No stock"
        self.list.append(vars()[str(ticker)])
        self.bought_at += float(vars()[str(ticker)].current_price) * float(vars()[str(ticker)].shares)

        self.total_stocks_bought += 1

        #gives total value of stock and shares at the initial price
        return str(vars()[str(ticker)].ticker) + " added"

    def delete_stock(self, ticker):
        """deletes stock from users portfolio

        :param ticker: name of the stock
        :return: deletes the stock to the user's portfolio/list
        """
        for i in range(len(self.list)):
            try:
                if self.list[i].ticker == ticker: #looks to see if there is such a stock
                    self.bought_at -= (float(self.list[i].current_price) * float(self.list[i].shares))
                    #takes away money value from portfolio

                    if float(self.list[i].prediction) >= float(f.current_price(self.list[i].ticker)):
                        self.success_rate += 1
                    else:
                        pass

                    del self.list[i] #removes stock from list
                    return "Deleted stock from portfolio"
            except:
                return "No stock with that name in the portfolio"

    def portfolio_value(self):
        """Determines portfolio value by looking at all the stock price times the shares for each stock
        to get the total value

        :return: the current value of the user's portfolio
        """
        self.current_total = 0
        for i in range(len(self.list)):
            self.current_total += (float(self.list[i].current_price) * float(self.list[i].shares))
            #adds the price times share of each stock to find value

        return self.current_total

    def return_on_investment(self):
        """Determines the return on investment depeniding on the portfolions current value and the price the stocks were
        bought at

        :return: return on investment (positive or negative)
        """
        self.current_total = 0
        for i in range(len(self.list)):
            self.current_total += (float(self.list[i].current_price) * float(self.list[i].shares))
            # adds the price times share of each stock to find value
        self.ROI = self.bought_at - self.current_total #looks at the initial value vs current value of portfolio

        return self.ROI

    def show_portfolio(self):
        """gives a list of stocks and shares that the suer currently holds

        :return: a visual representation of portfolio holdings
        """
        phrase = ''
        for i in range(len(self.list)): #adds multipe stocks together into one
            phrase += str(self.list[i].shares) + " shares of " + str(self.list[i].ticker) \
                      + " at " + str(self.list[i].current_price) + "\n"

        return phrase

    def show_prediction(self, ticker):
        """Shows the prediction of stock price at time of purchase

        :param ticker: the stock
        :return: the prediction and the date of prediction
        """
        for i in range(len(self.list)):
            try:
                if self.list[i].ticker == ticker: #looks to see if there is such a stock
                    return "prediction of " + str(self.list[i].prediction) + " made on: " + str(self.list[i].date)
            except:
                return "No stock with that name in the portfolio"

    def success(self):
        """gives the rate of success in terms of predictions

        :return: success rate
        """
        return self.success_rate / self.total_stocks_bought

class Stock():
    def __init__(self, ticker, shares): #current_price, information, history, trend, volume, change_during_day,
        # change_per_day,quarterly_cashflow, quarterly_earnings, sustainability, analyst_recommendation, news,calendar,
        # predictor
        """
        constructor
        """
        months = 1 #used for yfinance plugin where a specific amount of timeframe needs to be used
        self.ticker = ticker
        self.current_price = f.current_price(self.ticker)
        self.shares = shares
        self.prediction = f.predictor(self.ticker, months)
        self.date = datetime.datetime.today()

        #useful data for later:

        # self.information = f.information(self.ticker)
        # self.history = f.history(self.ticker, months)
        # self.trend = f.trend(self.ticker, months)
        # self.volume = f.volume(self.ticker, months)
        # self.change_during_day = f.change_during_day(self.ticker, months)
        # self.change_per_day = f.change_per_day(self.ticker, months)
        # self.quarterly_cashflow = f.quarterly_cashflow(self.ticker)
        # self.quarterly_earnings = f.quarterly_earnings(self.ticker)
        # self.sustainability = f.sustainability(self.ticker)
        # self.analyst_recommendation = f.analyst_recommendation(self.ticker)
        # self.news = f.news(self.ticker)
        # self.calendar = f.calendar(self.ticker)

def import_saved_data():
    try: #used when there is no data
        #unpickles at the beginning of program run
        infile = open(filename, 'rb')
        saved_user_data = pickle.load(infile) #unloads data as a list with lists
        infile.close()

        for i in range(len(saved_user_data)): #creates user
            vars()[str(saved_user_data[i][0])] = User(str(saved_user_data[i][0])) #creates user object
            users.append((vars()[saved_user_data[i][0]])) #appends object to list
            vars()[str(saved_user_data[i][0])].bought_at = saved_user_data[i][1] #sets ROI value saved previously

            vars()[str(saved_user_data[i][0])].success_rate = saved_user_data[i][2]
            vars()[str(saved_user_data[i][0])].total_stocks_bought = saved_user_data[i][3]

            for z in range(len(saved_user_data[i][4])):#the amount of stocks someone holds
                vars()[str(saved_user_data[i][4][z][0])] = Stock(str(saved_user_data[i][4][z][0]),
                                                                 int(saved_user_data[i][4][z][1]))#sets ticker and shares
                                                                                                    #for the stock object

                # sets initial prediction
                (vars()[str(saved_user_data[i][4][z][0])]).prediction = str(saved_user_data[i][4][z][2])

                # sets date when bought
                (vars()[str(saved_user_data[i][4][z][0])]).date = str(saved_user_data[i][4][z][3])


                stock = vars()[str(saved_user_data[i][4][z][0])] #the stock thats data has been recovered from pickling
                (vars()[str(saved_user_data[i][0])]).list.append(stock) #appends stock to users portfolio
    except:
        pass


