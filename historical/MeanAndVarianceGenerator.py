# This created .csv files with columns=[mean (or expectation), variance] and
# rows=(sum or trial) for each roll total
# It has performed its job admirably!

import pandas as pd
from UsefulFunctions import *

# expectationvalue(dataframe=one, rolls=rollslist[0], trial=1, savetofile=True)
for i in range(len(rollslist)):
    meanandvariance(dataframe=datalist[i], rolls=rollslist[i], savetofile=True)
