# ea_bot
Learning EA BOT

## Clone the project
`git clone https://github.com/MehdiShad/ea_bot.git`

## Create virtual environment
`python -m venv .venv`

### Activate virtual environment
`.\.venv\Scripts\activate`

## Install packages
`pip install MetaTrader5 pandas numpy python-dotenv loguru`

### Add your packages into requirements.txt
`pip freeze > requirements.txt`


# MetaTrader5 (Python) — README Cheat-Sheet (Functions in Your List)
This is a **paste-ready** reference for the `MetaTrader5` Python package functions shown in your screenshot.
It focuses on: **what it does**, **what it returns**, and **usable examples**.

> Import convention used below:
> ```python
> import MetaTrader5 as mt
> ```

## 0) Session / Connection

### `initialize()`
**What it does:** Connects Python to the running MT5 terminal (enables API calls).  
**Returns:** `True` on success, `False` on failure.

```python
import MetaTrader5 as mt

if not mt.initialize():
    raise SystemExit(f"initialize() failed: {mt.last_error()}")
```


### `copy_rates_from(...)` — OHLC bars (candles)

Fetch **aggregated candle/bar data** (OHLC) for a given symbol and timeframe.

- **Returns** bar fields: `time, open, high, low, close, tick_volume, spread, real_volume`
- **You choose** the timeframe: `TIMEFRAME_M1`, `TIMEFRAME_M5`, `TIMEFRAME_H1`, etc.
- **Best for:** indicators, candle-based strategies, backtesting on bars, feature engineering

#### Signature
```python
mt.copy_rates_from(symbol, timeframe, date_from, count)
```

### copy_rates_from_pos() 
fetches OHLC bar (candle) data like copy_rates_from(), but instead of specifying a start datetime, you specify a position (index) in the terminal’s bar history.

Signature (conceptually)

copy_rates_from_pos(symbol, timeframe, start_pos, count)

Meaning

start_pos = 0 → start from the most recent bar

start_pos = 1 → the bar before that

…

count → how many bars to return

What it returns

An array of bars with fields like:
time, open, high, low, close, tick_volume, spread, real_volume

Example

Get the latest 200 M5 candles:

rates = mt.copy_rates_from_pos("EURUSD", mt.TIMEFRAME_M5, 0, 200)

###### Example mental model: “Give me the last 500 M5 candles starting from time X.”

### copy_ticks_from(...) = raw ticks (tick-by-tick)
* Returns individual tick events: time, bid, ask, last, volume, flags
* You choose the tick type (all ticks / trade ticks / quote ticks depending on API)
* Best for: scalping logic, spread analysis, microstructure, precise entry/exit simulation, tick-based backtests

###### Example mental model: “Give me every price update since time X.”



