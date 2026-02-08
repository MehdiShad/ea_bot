import logging
import MetaTrader5 as mt  # pip install Metatrader5
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly
from datetime import datetime

print("Start !!!!!!!")
# Start the platform with initialize()
mt_initialize = mt.initialize()
print("is initialized: ", mt_initialize)

# Login to Trade Account with Login()
login = 10009535590
password = "RvW*5mVi"
server = "MetaQuotes-Demo"

mt.login(login, password, server)



# Get Account info

account_info = mt.account_info()
print(account_info)

# Getting specific account data
login_number = account_info.login
balance = account_info.balance
equity = account_info.equity

print()
print("login", login_number)
print("balance", balance)
print("equity", equity)

# Get number of symbols with symbols_total()
num_symbols = mt.symbols_total()
print(num_symbols)
print("================================================================================")

# Get all symbols and their specifications
# symbols = mt.symbols_get()
# print(symbols)
print("================================================================================")

# Get symbol specifications
symbol_info = mt.symbol_info("EURUSD")._asdict()
print(symbol_info)
print("================================================================================")

# Get current symbol price
symbol_price = mt.symbol_info_tick("EURUSD")._asdict()
print(symbol_price)
print("================================================================================")

# OHLC data
ohlc_data = pd.DataFrame(mt.copy_rates_range("EURUSD", mt.TIMEFRAME_D1, datetime(2025,1,1), datetime.now()))
fig = px.line(ohlc_data, x=ohlc_data["time"], y=ohlc_data["open"])
fig.show()
# print(ohlc_data)

print("================================================================================")

# Requesting tick data
tick_data = pd.DataFrame(mt.copy_ticks_range("EURUSD", datetime(2026,2,1), datetime.now(), mt.COPY_TICKS_ALL))
fig2 = px.line(tick_data, x=tick_data["time"], y=[tick_data["bid"], tick_data["ask"]])
fig2.show()
print("================================================================================")

# Total number of orders
num_orders = mt.orders_total()
print(num_orders)
print("================================================================================")

# List of order
orders = mt.orders_get()
print(orders)
print("================================================================================")

# Total number of positions
num_positions = mt.positions_total()
print(num_positions)
print("================================================================================")

# Total number of positions
positions = mt.positions_total()
print(positions)
print("================================================================================")

# Number of history orders
num_order_history = mt.history_orders_total(datetime(2026, 1, 1), datetime.now())
print(num_order_history)

print("================================================================================")

# List of history orders
order_history = mt.history_orders_get(datetime(2026, 1, 1), datetime.now())
print(order_history)
print("================================================================================")

# Number of history deals
num_deal_history = mt.history_deals_total(datetime(2026, 1, 1), datetime(2026, 2, 1))
print(num_deal_history)
print("================================================================================")

# History deals
deal_history = mt.history_deals_get(datetime(2026, 1, 1), datetime(2026, 2, 1))
print(deal_history)
print("================================================================================")

# Send order to the market
# documentation:

request = {
    "action": mt.TRADE_ACTION_DEAL,
    "symbol": "EURUSD",
    "volume": 2.0, # Float
    "type": mt.ORDER_TYPE_BUY,
    "price": mt.symbol_info_tick("EURUSD").ask,
    "sl": 0.0, # Float
    "tp": 0.0,  # Float
    "deviation": 20, # INT
    "magic": 23400, # INT
    "comment": "python  Script open",
    "type_time": mt.ORDER_TIME_GTC,
    "type_filling": mt.ORDER_FILLING_FOK,
}
order = mt.order_send(request)
print(order)
print("================================================================================")


# Close position

request = {
    "action": mt.TRADE_ACTION_DEAL,
    "symbol": "EURUSD",
    "volume": 2.0, # Float
    "type": mt.ORDER_TYPE_SELL,
    "position": 151550296175, # Select the position you want to close
    "price": mt.symbol_info_tick("EURUSD").ask,
    "sl": 0.0, # Float
    "tp": 0.0,  # Float
    "deviation": 20, # INT
    "magic": 23400, # INT
    "comment": "python  Script open",
    "type_time": mt.ORDER_TIME_GTC,
    "type_filling": mt.ORDER_FILLING_FOK,
}
order = mt.order_send(request)
print(order)

print("================================================================================")


print("================================================================================")


print("================================================================================")


print("================================================================================")


print("================================================================================")


print("================================================================================")
print("================================================================================")
print("================================================================================")
print("================================================================================")
print("================================================================================")
print("================================================================================")
print("================================================================================")
print("================================================================================")
print("================================================================================")
print("================================================================================")
print("================================================================================")
print("================================================================================")

