# Useful functions so we don't have to type so much

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# All the frequency dataframes, normalized using these
# lambda things I don't quite understand.
one = pd.read_csv('data/dice runs/ThreeDiceData50.txt', index_col='Trial')
two = pd.read_csv('data/dice runs/ThreeDiceData100.txt', index_col='Trial')
three = pd.read_csv('data/dice runs/ThreeDiceData500.txt', index_col='Trial')
four = pd.read_csv('data/dice runs/ThreeDiceData1000.txt', index_col='Trial')
five = pd.read_csv('data/dice runs/ThreeDiceData5000.txt', index_col='Trial')
six = pd.read_csv('data/dice runs/ThreeDiceData10000.txt', index_col='Trial')
seven = pd.read_csv('data/dice runs/ThreeDiceData50000.txt', index_col='Trial')
eight = pd.read_csv('data/dice runs/ThreeDiceData100000.txt', index_col='Trial')
nine = pd.read_csv('data/dice runs/ThreeDiceData500000.txt', index_col='Trial')
ten = pd.read_csv('data/dice runs/ThreeDiceData1000000.txt', index_col='Trial')
eleven = pd.read_csv('data/dice runs/ThreeDiceData5000000.txt', index_col='Trial')
twelve = pd.read_csv('data/dice runs/ThreeDiceData10000000.txt', index_col='Trial')

datalist = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]
rollslist = [50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]

# Normalized dataframes.
slice1 = pd.read_csv('data/normalized dice runs/normalized50.csv', index_col='Trial')
slice2 = pd.read_csv('data/normalized dice runs/normalized100.csv', index_col='Trial')
slice3 = pd.read_csv('data/normalized dice runs/normalized500.csv', index_col='Trial')
slice4 = pd.read_csv('data/normalized dice runs/normalized1000.csv', index_col='Trial')
slice5 = pd.read_csv('data/normalized dice runs/normalized5000.csv', index_col='Trial')
slice6 = pd.read_csv('data/normalized dice runs/normalized10000.csv', index_col='Trial')
slice7 = pd.read_csv('data/normalized dice runs/normalized50000.csv', index_col='Trial')
slice8 = pd.read_csv('data/normalized dice runs/normalized100000.csv', index_col='Trial')
slice9 = pd.read_csv('data/normalized dice runs/normalized500000.csv', index_col='Trial')
slice10 = pd.read_csv('data/normalized dice runs/normalized1000000.csv', index_col='Trial')
slice11 = pd.read_csv('data/normalized dice runs/normalized5000000.csv', index_col='Trial')
slice12 = pd.read_csv('data/normalized dice runs/normalized10000000.csv', index_col='Trial')

slicelist = [slice1, slice2, slice3, slice4, slice5, slice6, slice7, slice8, slice9, slice10, slice11, slice12]

lawoflargenumbers = pd.read_csv('data/rollquantityvariance.csv', index_col='Roll Quantity')


def expectationvalue(dataframe, trial, rolls, savetofile=False):
    """Calculates the expectation value and variance across trials.
    Should be around <x> = 10.5."""
    values = dataframe.transpose().loc[:, trial].values
    total = np.sum(values)
    expectation = 0
    for i in range(len(values)):
        expectation += (i + 3) * values[i] / total  # This is x*p(x), where x = 3, 4, etc.
    variance = 0                                    # and p(x) = values/total (i.e. probability)
    for j in range(len(values)):
        variance += ((j + 3) - expectation)**2      # (x - mu)**2
    print(f'In trial {trial}, expectation value is {expectation} with variance {variance} and StDev {np.sqrt(variance)}.')
    if savetofile is not False:
        with open(f'data/trial expectation and variance/trialExpectationAndVar{rolls}.csv', 'a') as file:
            file.write(f'\n{trial},{expectation},{variance}')


def meanandvariance(dataframe, rolls, savetofile=False):
    """Calculates the percent mean and variance (in percent squared) for
    each sum (3, 4, 5, ... , 18. Then calls expectationvalue() for the
    expectation value and variance of trials 1 through 20"""
    for dicesum in dataframe.columns.values:
        # Columns are 3, 4, ... , 18. probmean converts total rolls to
        # a percentage of total rolls, so 10 and 11 become like 12.5%.
        probmean = np.average(dataframe.loc[:, dicesum].values) / rolls
        variance = 0
        # Variance is sum of (x - mu)**2. In this case, it has units
        # of percent squared, which is not intuitive.
        for i in dataframe.loc[:, dicesum].values:
            variance += ((i / rolls) - probmean) ** 2
        print(f'{dicesum} occurs with probability mean {probmean}, variance {variance}, and StDev {np.sqrt(variance)}.')
        if savetofile is not False:
            with open(f'data/sum mean and variance/sumMeanAndVar{rolls}.csv', 'a') as file:
                file.write(f'\n{dicesum},{probmean},{variance}')
    for trial in dataframe.transpose().columns.values:
        # Also get the expectation and variance of the twenty trials
        # by calling the expectationvalue() function defined earlier
        expectationvalue(dataframe, trial=trial, savetofile=savetofile, rolls=rolls)


def barChartTheThing(dataframetoplot,
                     columntoplot,
                     title=None,
                     titlefontsize=15,
                     xaxislabel=None,
                     yaxislabel=None,
                     color='xkcd:cerulean blue',
                     islogscale=False,
                     figuredimensions=(8, 6),
                     filepathtosavepng=None,
                     legend=False):
    dataframetoplot.plot(kind='bar',
                         y=columntoplot,
                         color=color,
                         figsize=figuredimensions,
                         logy=islogscale,
                         legend=legend)
    plt.xlabel(xlabel=xaxislabel)
    plt.ylabel(ylabel=yaxislabel)
    plt.title(label=title, fontsize=titlefontsize)
    if filepathtosavepng is not None:
        plt.savefig(fname=filepathtosavepng,
                    bbox_inches='tight',
                    orientation="landscape",
                    pad_inches=0.2,
                    dpi=600)
    return plt.show()


def saveThisGraph(filepathtosavepng, dpi=600):
    plt.savefig(fname=filepathtosavepng, bbox_inches='tight', orientation="landscape", pad_inches=0.2, dpi=dpi)
    return print('Graph saved!')
