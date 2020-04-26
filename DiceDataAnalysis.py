# This is a beginning attempt at printing out graphs to show the change in variance
# and such. When we know what graphs would best work for our project, we can
# set it all up step-by-step in a jupyter notebook.

import pandas as pd
import matplotlib.pyplot as plt
from UsefulFunctions import sumMeanVarList, trialExpVarList

print(sumMeanVarList[0])
print(trialExpVarList[0].sort_values(by='Expectation Value', ascending=True))
