#!/usr/bin/python
#Stock_Graph.py

'''Creates a graph of a certain stock'''

__version__ = "1.1.0"
__author__ = 'Gregory Chekler'

from matplotlib import style
import pandas
import pandas_datareader as web
import datetime as dt

def Stocks_graph(symb, year, month, day):
    """creates a graph of stock price
    
    :param symb: stock that will be analyzed
    :return stock graph"""
    now = dt.datetime.now()
    symb = str(symb)
    style.use("ggplot")
    if year == '' and month == '' and day == '':
        start = dt.datetime(2010, 1, 1)
    else:
        start = dt.datetime(int(year), int(month), int(day))
    end = dt.datetime((now.year), int(now.month), int(now.day))
    df = web.get_data_yahoo(symb, start, end)
    figure = df["Adj Close"].plot()
    f = figure.get_figure()
    f.savefig("Stock_Graph.png")
    #This next part is for future editing
#     im = Image.open('Stock_Graph.png')
#     im = im.convert('RGB').convert('P', palette = Image.ADAPTIVE)
#     im.save('Stock_Graph.gif')

# Olav7D Tutorials on youtube helped me write this code
# Also Mr. Beckwith helped me with some parts of this that I did not know
