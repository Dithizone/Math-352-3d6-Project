# Useful functions so we don't have to type so much

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def expectationvalue(dataframe, trial):
    values = dataframe.transpose().loc[:, trial].values
    total = np.sum(values)
    expectation = 0
    for i in range(len(values)):
        expectation += (i + 3) * values[i] / total
    variance = 0
    for j in range(len(values)):
        variance += ((j + 3) - expectation)**2
    print(f'In trial {trial}, expectation value is {expectation} with variance {variance}.')


def meanandvariance(dataframe, rolls):
    for dicesum in dataframe.columns.values:
        probmean = np.average(dataframe.loc[:, dicesum].values) / rolls
        variance = 0
        for i in dataframe.loc[:, dicesum].values:
            variance += ((i / rolls) - probmean) ** 2
        print(f'{dicesum} occurs with probability mean {probmean} and variance {variance}.')
    for trial in dataframe.transpose().columns.values:
        expectationvalue(dataframe, trial=trial)
