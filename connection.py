from ibapi.client import EClient
from ibapi.wrapper import EWrapper


class TradingApp(
    EClient, EWrapper
):  # all methods available in EClient and EWrapper will be available inside TradingApp class
    pass
