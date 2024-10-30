# Simple Backtesting in Python

A simple backtesting library in Python with no frills. Just easy backtesting.

> Note that this project is in <ins>**active development**</ins>. For feature suggestions, feel free to head on over to the [Issues](https://github.com/SSBakh07/simple-backtester/issues) tab.

Compatible with Python 3.7+.

## Dependencies

- Pandas


## Usage guide

Pretend we're looking to implement a simple strategy where if the closing price falls twice, we buy. If the price rises two candles in a row, we sell.

### 1. Implement your strategy

We do this by creating a class that inherits from the `SBStrat` subclass;

```


```

### 2. Add your data

For now, the only way we can add our candle data data is by passing in a [`pandas DataFrame`](https://pandas.pydata.org/docs/reference/frame.html).

```


```

> Tick data is not supported at this time.

If our columns have different names or our date column has a specific format, we can pass those in:

```

```

And then, all we need to do is to 


### 3. Profit!

And now, all that's left is running our test!

```

```

We can specify our tests to be run from or to a certain date:

```

```

And we can 


## To-do List:

+ [ ] Limit orders
+ [ ] Writing up *proper* documentation
+ [ ] Adding more tests/cleaning up tests
+ [ ] Adding indicators using `talib`
+ [ ] Adding commission fees
+ [ ] Adding Yfinance support
+ [ ] Adding support for tick data


> Questions? Concerns? Email me at ssbakh07 (at) gmail.com