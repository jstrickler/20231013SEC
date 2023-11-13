import pandas as pd
from printheader import print_header

column_labels = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']  # column labels
row_labels = pd.date_range('2013-01-01 00:00:00', periods=6, freq='D')  # date range to be used as row indexes

print(row_labels, "\n")

values = [  # sample data
    [100, 110, 120, 930, 140],
    [250, 210, 120, 130, 840],
    [300, 310, 520, 430, 340],
    [275, 410, 420, 330, 777],
    [300, 510, 120, 730, 540],
    [150, 610, 320, 690, 640],
]

df = pd.DataFrame(values, row_labels, column_labels)  # create dataframe from data
print_header("Basic DataFrame:")
print(df)
print()

print_header("Triple each value")
print(df * 3)
print()  # multiply every value by 3

print_header("Multiply column gamma by 1.5")
df['gamma'] *= 1.5  # multiply values in column 'gamma' by 1.
print(df)
print()
