import pandas as pd
import os
from datetime import datetime
 
Stock_folder = "/home/karthikarchit/Final"
Stock_folder_files = os.listdir("/home/karthikarchit/Final")
Stock_folder_files.sort()

Stock_Data = pd.DataFrame()

for folder in Stock_folder_files:
    folder_path = os.path.join(Stock_folder,folder)
    files = os.listdir(folder_path)
    files = sorted(files,key =  lambda x: int(x[:-4]))
    for filename in files:
        file_path = os.path.join(folder_path,filename)
        df = pd.read_csv(file_path,names=['Index','Date','Time','Open','High','Low','Close'],header=None,usecols=[i for i in range(7)])
        df = df[1:] 
        df['Date'] = pd.to_datetime(df['Date'],format="%Y%m%d")
        Stock_Data = pd.concat([Stock_Data,df],ignore_index=True)
        Stock_Data.sort_values(by=['Date'],ignore_index=True)

Stock_Data.to_csv("/home/karthikarchit/StockData.csv")







