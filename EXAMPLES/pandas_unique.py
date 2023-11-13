import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('https://qrc.depaul.edu/Excel_Files/Presidents.xlsx', sheet_name='Master',
                  na_values='NA()')
df.index = range(1,len(df)+1)

print(df.head())
print(df.loc[1])
party_counts = df['Political Party'].value_counts()
print(party_counts)
# plot the data
plt.figure(figsize=(20.0,8.0))
party_counts.plot(kind='barh')
plt.show()
