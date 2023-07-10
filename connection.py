from ibapi.client import EClient
from ibapi.wrapper import EWrapper
import threading


class TradingApp(
    EClient, EWrapper
):  # all methods available in EClient and EWrapper will be available inside TradingApp class
    def __init__(self):
        EClient.__init__(self, wrapper=self)


app = TradingApp()
app.connect("127.0.0.1", 7497, 0)

t1 = threading.Thread(target=app.run)
t1.start()

print("After Thread")
