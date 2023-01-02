import pandas as pd
from datetime import time,datetime

StockData = pd.read_csv("/home/karthikarchit/StockData.csv")

def TimeCategory(x):

    format = "%H:%M"
    StockTime = datetime.strptime(x,format)
    _9am = datetime.strptime("09:00",format)
    _12pm = datetime.strptime("12:00",format)
    _3pm = datetime.strptime("15:00",format)

    if(StockTime>=_9am and StockTime < _12pm):
        return 1
    elif(StockTime>=_12pm and StockTime < _3pm):
        return 2
    else:
        return 3

def GetDayFromDate(x):

    format = "%Y-%m-%d"
    day = datetime.strptime(x,format).weekday()
    return day+1

def CreateNewColumns(StockData):

    StockData["TimeCategory"] = StockData["Time"].apply(lambda x : TimeCategory(x=x))
    StockData["WeekDay"] = StockData["Date"].apply(lambda x : GetDayFromDate(x=x))

CreateNewColumns(StockData=StockData)
StockData.to_csv("/home/karthikarchit/StockData_NC.csv")






    