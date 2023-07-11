from ibapi.order import Order
from connect import TradingApp

o1 = Order()
o1.action = "BUY"
o1.orderType = "LMT"
o1.totalQuantity = 10
o1.lmtPrice = 130


# Place order
app = TradingApp()
orderId = app.nextValidOrderId
app.placeOrder(
    orderId,
)
