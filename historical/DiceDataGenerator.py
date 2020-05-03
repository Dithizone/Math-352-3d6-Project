# This script will generate the distribution of sums from a number of dice rolls
# stated in the trialstorun list. Running this script will regenerate the data
# found in data/dice runs, but will take about 6.5 hours to do so.
# I've commented out the file-writing bits so we don't damage our current data.

# 1 million rolls takes 76 seconds
# 10 million rolls takes 12.39 minutes
# 25 million rolls takes 29.51 minutes
# 100 million rolls (5 million, 20 times) will probably take 2 hours
# 200 million rolls (10 million, 20 times) will probably take 4 hours
# 1 billion rolls (50 million, 20 times) will probably take 20 hours...

# This script performed its job admirably!

import numpy as np
import time

print("This is for the final project in probability and statistics.")
print("We have to determine likelihood of each sum. (1 way for sum 3, 1 way for sum 18, etc.)")

trialstorun = [50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
trialscompleted = 0
aggregatesums = {'3': 0,
                 '4': 0,
                 '5': 0,
                 '6': 0,
                 '7': 0,
                 '8': 0,
                 '9': 0,
                 '10': 0,
                 '11': 0,
                 '12': 0,
                 '13': 0,
                 '14': 0,
                 '15': 0,
                 '16': 0,
                 '17': 0,
                 '18': 0}

start = time.process_time()
for m in range(len(trialstorun)):           # m goes from 0 to 11
    totalrolls = trialstorun[m]             # Converts e.g. "3" into "1000"
    trialnumber = 1
    # file = open(f"data/dice runs/ThreeDiceData{totalrolls}.txt", "w")
    # file.write("Trial,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18\n")
    for k in range(20):  # Repeat e.g. 1000 rolls twenty times.
        for i in range(totalrolls):
            die1 = np.random.randint(low=1, high=7, size=1)     # "roll" the three dice
            die2 = np.random.randint(low=1, high=7, size=1)
            die3 = np.random.randint(low=1, high=7, size=1)
            alldice = die1 + die2 + die3                        # Add up each die roll
            print(f"{i + 1}\t{totalrolls}\t{(20 * len(trialstorun)) - trialscompleted}\n")  # (for debugging)
            aggregatesums[str(alldice[0])] += 1                 # Tally this dice sum in the
                                                                # Python dict called "aggregatesums"
        trialscompleted += 1
        # file.write(f"{trialnumber},"
        #            f"{aggregatesums['3']},"
        #            f"{aggregatesums['4']},"
        #            f"{aggregatesums['5']},"
        #            f"{aggregatesums['6']},"
        #            f"{aggregatesums['7']},"
        #            f"{aggregatesums['8']},"
        #            f"{aggregatesums['9']},"
        #            f"{aggregatesums['10']},"
        #            f"{aggregatesums['11']},"
        #            f"{aggregatesums['12']},"
        #            f"{aggregatesums['13']},"
        #            f"{aggregatesums['14']},"
        #            f"{aggregatesums['15']},"
        #            f"{aggregatesums['16']},"
        #            f"{aggregatesums['17']},"
        #            f"{aggregatesums['18']}\n")
        print(f"Trials Completed: {trialscompleted}")
        trialnumber += 1

        for j in aggregatesums.keys():
            print(f"{j}: {aggregatesums[j]}")
            aggregatesums[j] = 0

    # file.close()


end = time.process_time()

print(f'Time elapsed: {(end - start) / 60} minutes.')
