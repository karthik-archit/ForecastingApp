class StockInfo:

    def __init__(self, StockName, StockPrice, Date_Time):
        self.StockName = StockName
        self.StockPrice = StockPrice
        self.Date_Time = Date_Time
    def __str__(self):
        return f"{self.StockName} had a price of {self.StockPrice} on {self.Date_Time}"
    



