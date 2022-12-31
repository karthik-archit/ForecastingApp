from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from WebScraping.StockInfo import StockInfo

driver_path = "./Webdriver/chromedriver"
options = Options()

# -------------------Developement--------------------# 
# options.add_argument("--window-size=1920,1080")
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(driver_path,options=options)
# driver.get('https://finance.yahoo.com/quote/%5ENSEI/')
#-----------------------------------------------------#

#-------------------Production-----------------------#
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("detach", True)
options.headless = True
driver = webdriver.Chrome(driver_path,options=options)
driver.get('https://finance.yahoo.com/quote/%5ENSEI/')
#----------------------------------------------------#


def getStockInfo():
    stock_price= driver.find_element(By.XPATH,"//fin-streamer[@class='Fw(b) Fz(36px) Mb(-4px) D(ib)']").text
    stock_name = driver.find_element(By.XPATH,"//h1[@class='D(ib) Fz(18px)']").text
    Date_time = driver.find_element(By.XPATH,"//div[@id='quote-market-notice']/span").text
    Date_time,stock_name = CleanData(Date_time=Date_time,stock_name=stock_name)
    stock_info = StockInfo(stock_name,stock_price,Date_time)
    return stock_info
    
def CleanData(Date_time,stock_name):
    Date_time = Date_time[9:-3]
    stock_name = stock_name[:9]
    return Date_time,stock_name







