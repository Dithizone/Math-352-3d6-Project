# This is a beginning attempt at printing out graphs to show the change in variance
# and such. When we know what graphs would best work for our project, we can
# set it all up step-by-step in a jupyter notebook.

import pandas as pd
import matplotlib.pyplot as plt
from UsefulFunctions import datalist, rollslist, slicelist, lawoflargenumbers
from matplotlib.cm import get_cmap
import numpy as np


# For the first graph
prettycolorforchart1 = get_cmap('cool')(np.linspace(0, 1, 12))
prettycolorforchart2 = get_cmap('afmhot')(np.linspace(0, 1, 20))

plt.figure(figsize=(8, 6))
for k in range(len(slicelist)):
    plt.plot(slicelist[k].transpose().iloc[:, 3], label=f'{rollslist[k]} Rolls', color=prettycolorforchart1[k])
plt.title(label='Relative Frequency of Each Dice Roll Sum', fontsize=15)
plt.legend()
plt.xlabel('Dice Sum')
plt.ylabel('Normalized Frequency')
plt.show()

# For the second graph
plt.figure(figsize=(12, 9))
for k in range(len(slicelist)):
    plt.plot(slicelist[k].iloc[:, 7], label=f'{rollslist[k]} Rolls', color=prettycolorforchart2[k], linewidth=3.3)
plt.title(label='Relative Frequency of Dice Sum of 10', fontsize=15)
plt.legend(loc='lower left')
plt.xlabel('Trial')
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
plt.ylabel('Normalized Frequency (Theoretical: 0.125)')
plt.show()

# for the third graph, first need to create the variance dataframe

for i in range(len(slicelist)):
    data = slicelist[i]
    rollquantity = rollslist[i]
    the10s = data.iloc[:, 7].values
    variance = 0
    mean = np.average(the10s)
    for k in the10s:
        variance += (k - mean)**2
    # with open('data/rollquantityvariance.csv', 'a') as file:
    #     file.write(f'\n{rollquantity},{variance}')

print(lawoflargenumbers)
plt.figure(figsize=(8, 6))
lawoflargenumbers.plot(kind='line')
plt.title(label='Variance in Relative Frequency of a Dice Sum of 10', fontsize=15)
plt.xscale('log')
plt.xlabel('Roll Quantity')
plt.ylabel('Variance')
plt.show()

# All done, yay!
