# Background
SPY is usually near all-time highs. Is this alpha?

This program seeks to answer the following questions:
1. What does "near all-time highs" mean?
    - When SPY is within ALL_TIME_HIGH_THRESHOLD percent of the current all time high.
2. How often is SPY near all-time highs?
3. When SPY is not near all-time highs, how far does it typically deviate?
4. When SPY is not near all-time highs, how long does it typically take to get back to all-time highs?

# Method
Obtain historical data from Yahoo Finance.

Run Python script to run analysis.

- Use `Close Price`

# Trading Strategy
Go long on SPY when it's not at all-time highs

1. Buy 100 shares when X percent away
2. Set stop loss at Y percent away
3. Sell:
    - After N days?
    - After N percent profit?
    - After SPY is within Z percent of all-time high?

## Usage
In install the prerequisites:
```console
$ python -m pip install -r requirements.txt
```

Run the program
```console
python ./spy_analysis.py
```

Tweak `ALL_TIME_HIGH_THRESHOLD` in the script for different behavior. 
