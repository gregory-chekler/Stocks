import yfinance as yf
import math
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web
import datetime as dt
import datetime

def Stocks_graph(symb):
    now = datetime.datetime.now()
    symb = str(symb)
    style.use("ggplot")
    start = dt.datetime(2006, 1, 1)
    end = dt.datetime(int(now.year), int(now.month), int(now.day))
    df = web.get_data_yahoo(symb, start, end)
    figure = df["Adj Close"].plot()
    f = figure.get_figure()
    #plt.show()
    f.savefig("Stock_Graph.png")
#     im = Image.open('Stock_Graph.png')
#     im = im.convert('RGB').convert('P', palette = Image.ADAPTIVE)
#     im.save('Stock_Graph.gif')

#Olav7D Tutorials on youtube helped me write this code