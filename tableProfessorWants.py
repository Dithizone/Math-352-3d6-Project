# This will create the table the professor wants for the paper

from UsefulFunctions import rollslist, slicelist
import numpy as np

# It'll be structured like this:
#
# Sum  |              Total rolls ...
#      | avg across trials | variance across trials
# 3    |
# 4    |
# 5    |
# 6    |
# 7    |
# 8    |
# 9    |
# 10   |
# 11   |
# 12   |
# 13   |
# 14   |
# 15   |
# 16   |
# 17   |
# 18   |

sums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
table = {}

rolls = 0
for normalizeddata in slicelist:
    totalrolls = rollslist[rolls]
    for specificsum in sums:
        mean = np.mean(normalizeddata[f'{specificsum}'].values)
        variance = 0
        for i in range(20):
            deltavariance = (normalizeddata.iloc[i, (specificsum - 3)] - mean)**2
            variance += deltavariance
        print(f'{specificsum} | {mean} | {variance} | {totalrolls}')
        if str(specificsum) not in table:
            table[f'{specificsum}'] = [mean, variance]
        if str(specificsum) in table:
            table[f'{specificsum}'].append(mean)
            table[f'{specificsum}'].append(variance)
    rolls += 1

# Yay, here it is.

for key in table.keys():
    print(f'{key}', end=',')
    for value in table[key]:
        print(f'{value}', end=',')
    print('\n', end='')
