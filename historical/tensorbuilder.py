# This won't actually make a tensor, but it will create a
# set of .csv files which can be thought of as slices of a
# tensor. Imagining it this way makes it easier to construct
# the graphs I need.
# It performed its job admirably!

import pandas as pd
from UsefulFunctions import datalist, rollslist

# I added the lambda stuff to UsefulFunctions.py and
# now needed to save the results in new files.
for i in range(len(datalist)):
    normalizeddata = datalist[i]
    rollquantity = rollslist[i]
    # normalizeddata.to_csv(path_or_buf=f'data/normalized dice runs/normalized{rollquantity}')
