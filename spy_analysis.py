#!/usr/bin/env python3
from pathlib import Path

import pandas as pd

ALL_TIME_HIGH_THRESHOLD = 1  # percent


def set_all_time_high_columns(threshold):
    """Insert new columns for "All-Time High".

    All-Time High: absolute highest value the Close price has reached.
    All-Time High Delta: The percent distance Close is from All-Time High
    Near All-Time High: Boolen indicating if Close is within `threshold` percent of All-Time High
    """
    df['All-Time High'] = 0

    # Seed the first Current High value to the first data point's High value.
    df.loc[0, 'All-Time High'] = df.loc[0]['Close']

    # Iterate over rest of rows so we can reference the previous row.
    for i in range(1, len(df)):
        # Set All-Time High to whichever is greater: current all-time high or most recent close price.
        df.loc[i, 'All-Time High'] = max(df.loc[i - 1, 'All-Time High'],
                                         df.loc[i, 'Close'])

    df['All-Time High Delta (%)'] = df.apply(lambda row: (
        (row['All-Time High'] - row['Close']) / row['All-Time High'] * 100),
                                             axis=1)
    df['Near All-Time High'] = df.apply(
        lambda row: row['All-Time High Delta (%)'] <= threshold, axis=1)


if __name__ == "__main__":
    INPUT_FILE = Path('SPY.csv')

    df = pd.read_csv(INPUT_FILE)

    set_all_time_high_columns(ALL_TIME_HIGH_THRESHOLD)

    # print(df.tail(10))

    # TODO: Allow start date to be configurable. Allow date ranges to be 'blacked out'
    df = df[5700:]

    print(
        "All-time high is defined here as price within ALL_TIME_HIGH_THRESHOLD percent of the current all time high"
    )
    print(
        "When SPY is not near all-time highs, how long does it typically take to get back to all-time highs?"
    )
    times_to_recover = []
    count = 0
    for value in df['Near All-Time High'].values:
        if value == False:
            count += 1
        else:
            times_to_recover.append(count)
            count = 0
    times_to_recover = pd.Series(times_to_recover)
    # TODO: This can be configurable. Set to 0 means we'll see "chatter", where SPY is sitting around the threshold percent away from all-time highs
    # so every other day it's above/below threshold. This drives down the time to recover.
    times_to_recover = times_to_recover[times_to_recover > 0]
    print(f"    {times_to_recover.mean()} days")
    print()

    print("How often is SPY near all-time highs?")
    print(df['Near All-Time High'].value_counts(normalize=True))
    print()

    print(
        "When SPY is not near all-time highs, how far does it typically deviate?"
    )
    days_not_near_all_time_high = df.loc[df['Near All-Time High'] == False]
    print(
        f"    {days_not_near_all_time_high['All-Time High Delta (%)'].mean()} %"
    )
    print()
