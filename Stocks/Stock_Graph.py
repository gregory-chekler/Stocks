#!/usr/bin/python
#Stock_Graph.py

'''Creates a graph of a certain stock'''

__version__ = "1.0.0"
__author__ = 'Gregory Chekler'

from matplotlib import style
import pandas_datareader as web
import datetime as dt

def Stocks_graph(symb):
    """creates a graph of stock price
    
    :param symb: stock that will be analyzed
    :return stock graph"""
    now = dt.datetime.now()
    symb = str(symb)
    style.use("ggplot")
    start = dt.datetime(2006, 1, 1)
    end = dt.datetime(int(now.year), int(now.month), int(now.day))
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
