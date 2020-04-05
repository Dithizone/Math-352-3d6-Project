# This is a beginning attempt at printing out graphs to show the change in variance
# and such. When we know what graphs would best work for our project, we can
# set it all up step-by-step in a jupyter notebook.

import pandas as pd
import matplotlib.pyplot as plt

columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
totalrolls = 0
diceDataFromFile = pd.read_csv('data/dice runs/ThreeDicedata1000.txt', index_col="Trial")
for i in diceDataFromFile.iloc[1, :]:
    totalrolls += i

normalizedDiceData = diceDataFromFile / totalrolls
print(totalrolls)
diceData = normalizedDiceData.transpose()
print(diceData)
diceData.plot(kind='bar', y=columns, figsize=(8, 4), color='xkcd:jade', legend=False)
plt.title('The normalized sum frequency of 3d6 over 1,000 rolls')
plt.xlabel('Sum')
plt.ylabel('Percent Appearance')
plt.xticks(rotation=0)
plt.show()
