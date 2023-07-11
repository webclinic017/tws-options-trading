from ibapi.contract import Contract

# Define an Apple Stock contract

c1 = Contract()

c1.symbol = "AAPL"
c1.secType = "STK"
c1.currency = "USD"
c1.exchange = "SMART"
c1.primaryExchange = "NASDAQ"


print(c1.currency)
