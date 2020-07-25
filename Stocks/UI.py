#!/usr/bin/python
#UI.py

'''provides user interface that allows typing into text boxes,
selecting from different functions, and displaying results in a text area'''

__version__ = "1.0.0"
__author__ = 'Gregory Chekler'


import finance_data
from tkinter import PhotoImage
import tkinter
from tkinter.font import Font
import time
from PIL import Image


# these words will appear in the menu:
OPTIONS = [
    "Choose A Function:",
    "Current Price",
    "Stock Info",
    "Stock History",
    "Stock Graph",
    "Composite news/data rating",
    "Analyst Recommendations",
    "Sustainability",
    "Next Event",
    "Quarterly Earnings",
    "Quarterly Cashflow",
    "Trend interpreter",
    "Average change per day",
    "Average change from day to day",
    "Volume interpreter",
    "Stock Price Prediction"
    
    ]

pic = None
root = tkinter.Tk() #the base window that all tkinter objects go into
 # you can name it anything, but usually root or master or window
 # the buttons and windows and menu will all be placed into this window
 
root.title("Stock analysis")  #set title to something you like

###################################
# FUNCTIONS CALLED BY MENU AND BUTTONS:
###################################
def quitting_time():
    '''called when Quit button is pressed'''
    root.destroy()
  
def add_pic():
    global input_area, pic
    input_area.delete(1.0, tkinter.END)          # delete previous text

    im = Image.open('Stock_Graph.png')

    im = im.convert('RGB').convert('P', palette = Image.ADAPTIVE)
    im.save('Stock_Graph.gif')
    root.photo2 = tkinter.PhotoImage(file='Stock_Graph.gif')      # fun photo to display at start

    pic = input_area.image_create(tkinter.END, image=root.photo2)  # inserts fun photo
    
def show_instructions(event):
    '''Called when menu item is selected and will show instructions'''

    global menu_var, results_display
    
    selection = menu_var.get()  # get which item was selected
    # set instructions text for the item selected:
    
    if selection == "Stock Info":
        instructions = "Input the stock/ticker symbol in the first box"
    elif selection == "Stock History":
        instructions = "Input the stock/ticker symbol in the first box" +\
                       " and then input the amount of months you want in" +\
                       " the second box"
    elif selection == "Stock Graph":
        instructions = "Input the stock/ticker symbol in the first box. Then" +\
                       " click the submit and then the adpic button."
    elif selection == "Composite news/data rating":
        instructions = "Input the stock/ticker symbol. This is an equation" +\
                     " that takes conclusion from analysts and determines if" +\
                     " the news is good or bad. If the number is below 1, the" +\
                     " news is bad. If it is above one, it is good."
    elif selection == "Analyst Recommendations":
        instructions = "Input the stock/ticker symbol in the first box"
    elif selection == "Sustainability":
        instructions = "Input the stock/ticker symbol in the first box (some " +\
                       "stocks may not have this information)"
    elif selection == "Next Event":
        instructions = "Input the stock/ticker symbol in the first box"
    elif selection == "Quarterly Earnings":
        instructions = "Input the stock/ticker symbol in the first box"
    elif selection == "Quarterly Cashflow":
        instructions = "Input the stock/ticker symbol in the first box"
    elif selection == "Trend interpreter":
        instructions = "Input the stock/ticker symbol in the first box" +\
                       " and then input the amount of months you want in" +\
                       " the second box"
    elif selection == "Average change per day":
        instructions = "Input the stock/ticker symbol in the first box" +\
                       " and then input the amount of months you want in" +\
                       " the second box"
    elif selection == "Average change from day to day":
        instructions = "Input the stock/ticker symbol in the first box" +\
                       " and then input the amount of months you want in" +\
                       " the second box"
    elif selection == "Volume interpreter":
        instructions = "Input the stock/ticker symbol in the first box" +\
                       " and then input the amount of months you want in" +\
                       " the second box"
    elif selection == "Stock Price Prediction":
        instructions = "Input the stock/ticker symbol in the first box" +\
                       " and then input the amount of months you want in" +\
                       " the second box"
    elif selection == "Current Price":
        instructions = "Input the stock/ticker symbol in the first box"
    else :
        instructions = "Nothing selected yet"
        
    ### DISPLAYS INSTRUCTIONS IN THE BIG TEXT AREA: ###
    results_display.configure(state="normal")         # allow editing of text
    results_display.delete(1.0, tkinter.END)          # delete previous text
    results_display.insert(tkinter.END, instructions) # show results in text area
    results_display.configure(state="disabled")       # prevent editing of text

    
def submit():
    '''called when the submit button is clicked'''
    
    global menu_var, results_display, entry_1, entry_2, entry_3
    global entry_4, input_area, results_label
    # gets values (as strings) from the entry boxes
    arg_1 = entry_1.get()
    arg_2 = entry_2.get()
    arg_3 = entry_3.get()
    arg_4 = entry_4.get()

    ### USE THIS FOR LARGER BODIES OF INPUTTED TEXT THAT WON'T FIT IN THE LITTLE BOXES ###
   
    # get text from large text area:
    
    large_text = input_area.get("1.0", tkinter.END)  # see explanation below:     
    
    # EXPLANATION:
     
      # "1.0" = STARTING point: means the input should be read from line 1, character 0
      #       (something like "2.3" = line 2 character 3)
      # tkinter.END = ENDING point: tkinter.END reads all the way to the end of the text area
      #       (something like END + "-2c" means to not read the last two characters)
      #       (use END + "-1C" to get rid of the newline character at the end!)

    
    large_text = large_text.strip()   # extra \n needs to be stripped

    return_text=""
    selection = menu_var.get()
    
    # calls selected function, sending it the necessary arguments
    #    and storing the returned string into display_text:
    import Stock_Graph
    if selection == "Stock Info":
        display_text = finance_data.information(arg_1)
    elif selection == "Stock History":
        display_text = finance_data.history(arg_1, arg_2)
    elif selection == "Stock Graph":
        display_text = Stock_Graph.Stocks_graph(arg_1)
    elif selection == "Composite news/data rating":
        display_text = finance_data.news(arg_1)
    elif selection == "Analyst Recommendations":
        display_text = finance_data.analyst_recommendation(arg_1)
    elif selection == "Sustainability":
        display_text = finance_data.sustainability(arg_1)
    elif selection == "Next Event":
        display_text = finance_data.calendar(arg_1)
    elif selection == "Quarterly Earnings":
        display_text = finance_data.quarterly_earnings(arg_1)
    elif selection == "Quarterly Cashflow":
        display_text = finance_data.quarterly_cashflow(arg_1)
    elif selection == "Trend interpreter":
        display_text = finance_data.trend(arg_1, arg_2)
    elif selection == "Average change per day":
        display_text = str(finance_data.change_per_day(arg_1, arg_2)) + "%"
    elif selection == "Average change from day to day":
        display_text = str(finance_data.change_during_day(arg_1, arg_2)) + "%"
    elif selection == "Volume interpreter":
        display_text = finance_data.volume(arg_1, arg_2)
    elif selection == "Stock Price Prediction":
        display_text = finance_data.predictor(arg_1, arg_2)
    elif selection == "Current Price":
        display_text = finance_data.current_price(arg_1)
    else:
        display_text = "No function selected or not ready yet"
        

    # show something in the label:
    results_label.config(text = "Results of calling function " + selection.upper() + ":") 
    
    # deletes old text and insert results text into the large text area:
    input_area.configure(state="normal") # allow editing of text
    input_area.delete(1.0, tkinter.END)
    input_area.insert(tkinter.END, display_text) # show results in text area
    input_area.configure(state="disabled") # prevent editing of text
    

def main():
    global input_area

    global menu_var, results_display, entry_1, entry_2, entry_3
    global entry_4, input_area, results_label
    ###################################
    # SET UP ALL THE DISPLAY COMPONENTS:
    ###################################
    
    # nice font:
    my_font = Font(family="Verdana", size=15, weight="bold")
    
    ###################################
    # 1. TEXT AREA THAT DISPLAYS RESULTS, USING THE ABOVE FONT
    ###################################
    results_display = tkinter.Text(root,  #display needs the tkinter window to be put in
                            height=30,
                            relief="ridge",
                            bd=6, 
                            width=60,
                            font=my_font,
                            foreground='green',
                            background='black')
    
    photo = tkinter.PhotoImage(file='tenor.gif')      # fun photo to display at start
        #(PhotoImages must be .gif)
    
    results_display.configure(state="normal") # allow editing of text
    results_display.image_create(tkinter.END, image=photo)  # inserts fun photo
    results_display.insert(tkinter.END, "                                   " +\
                           "                                                " +\
                           "                                                " +\
                           "                                                " +\
                           "                                                " +\
                           "Welcome to the stock analysis software. " +\
                           "This software will help you make informed market" +\
                           " decisions, and predict future stock price. " +\
                           "As this is an early build of the software, there" +\
                           " are a couple restrictions on what can be done." +\
                           " Right now, please refrain from inputting stocks" +\
                           " that are over $1000 dollars, and if you do not see" +\
                           " anything in the display area, there may either" +\
                           " be no data, or there may be a bug. Also, " +\
                           "when using the stock graph, if used more than once," +\
                           " it may display two stocks at the same time. If " +\
                           "this happens, please restart the software." +\
                           " All these bugs will be fixed in the future. " +\
                           "Otherwise, enjoy!")         # insesrts default text
    results_display.configure(state="disabled")
    
    ###################################
    # 2. TEXT AREA FOR ENTERING LARGE AMOUNTS OF TEXT
    ###################################
    input_area = tkinter.Text(root,
                            height=30,
                            bd=2, 
                            width=60,
                            font=my_font,
                            foreground='red',
                            background='black')
#     im = Image.open('Stock_Graph.png') Keep this for future edits(for addign stock graph)
# 
#     im = im.convert('RGB').convert('P', palette = Image.ADAPTIVE)
#     im.save('sg.gif')
#     photo2 = tkinter.PhotoImage(file='sg.gif')      # fun photo to display at start
# 
   # input_area.image_create(tkinter.END, image=photo2)  # inserts fun photo
    ###################################
    # 3. TEXT LABEL THAT CAN SHOW RESULTS:
    ###################################

    results_label = tkinter.Label(text="Version 1.0.0")
    
    ###################################
    # 4. BUTTONS
    ###################################
    
    # will call the submit() function when pressed:
    submit_button = tkinter.Button(text="SUBMIT", command=submit)
    
    # will call quitting_time when pressed:
    quit_button = tkinter.Button(root, text="Quit", command=quitting_time)
    
    pic_button = tkinter.Button(root, text="addpic", command=add_pic)
    ###################################
    # 5. SET UP PULLDOWN MENU OF FUNCTION CHOICES:
    ###################################
    
    # this variable holds the selected value from the menu
    menu_var = tkinter.StringVar(root)
    menu_var.set(OPTIONS[0]) # default value
    
    # create the optionmenu (pulldown menu) with the options above:
    option_menu = tkinter.OptionMenu(root, menu_var, *OPTIONS, command=show_instructions)
    
    ###################################
    # 6. PLACE EVERYTHING IN THE TKINTER WINDOW:
    #     a "grid" allows you to turn the tkinter window into a series
    #     of rows and columns and specifcy where to place everything
    ###################################
    # place the menu in the top left:
    option_menu.grid(row=0, column=0, columnspan=1)
    
    # place the buttons in the top middle:
    submit_button.grid(row=0, column=1, columnspan=1)
    quit_button.grid(  row=0, column=2, columnspan=1)
    pic_button.grid(  row=0, column=3, columnspan=1)

    # sets up argument input boxes...ADD MORE IF YOU NEED THEM!!!
    entry_1 = tkinter.Entry()  # makes an Entry object
    entry_2 = tkinter.Entry()
    entry_3 = tkinter.Entry()
    entry_4 = tkinter.Entry()
    
    # place the entry boxes in the next row, going across...ADD MORE IF NEEDED!!!
    entry_1.grid(row=1, column=0)
    entry_2.grid(row=1, column=1)
    entry_3.grid(row=1, column=2)
    entry_4.grid(row=1, column=3)
    
    # place the label in the next row (is just one row of text):
    results_label.grid(row=3, column=0, columnspan=4)
    
    # place the text areas in the next row (is a whole box of text):
    results_display.grid(row=4, column=0, columnspan=2)
    input_area.grid(     row=4, column=2, columnspan=2)
    # make it so that words won't get broken up when reach end of text box:
    results_display.config(wrap=tkinter.WORD)
    input_area.config(     wrap=tkinter.WORD)
    
    # waits for button clicks to take actions:
    root.mainloop()
if __name__ == "__main__":    
    main()