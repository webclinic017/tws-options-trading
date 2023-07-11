from ibapi.client import EClient
from ibapi.wrapper import EWrapper
import threading


class TradingApp(
    EClient, EWrapper
):  # all methods available in EClient and EWrapper will be available inside TradingApp class
    def __init__(self):
        EClient.__init__(self, wrapper=self)
        self.nextValidOrderId = None

    def nextValidId(self, orderId):
        self.nextValidOrderId = orderId


app = TradingApp()
app.connect("127.0.0.1", 7497, 0)

t1 = threading.Thread(target=app.run)  # run app in an independent thread
t1.start()


# Waiting for TWS connection acknowledgement
while app.nextValidId == None:
    print("Waiting for TWS connection acknowledgement...")


print("Connection established.")
