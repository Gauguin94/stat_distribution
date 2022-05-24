# show plot and calculate combination nCx

import math
import matplotlib.pyplot as plt
import numpy as np

def combination(trial, target_count):
    deno = math.factorial(trial) # deno means denominator.
    nume_1 = math.factorial(target_count) # nume_1 means numerator that factorial of number of target.
    nume_2 = math.factorial(trial - target_count) # nume_2 means numerator that factorial of "trial - number of target".
    result = deno/(nume_1*nume_2) # n!/x!(n-x)! => (nCx)
    return result

def showPlot(histo, mew=None, val=None, marker=True):
    plt.figure(figsize=(40,40))
    if marker:
        plt.plot(histo, '.')
    else:
        plt.plot(histo, '-')
    if mew != None:
        plt.annotate(text = 'mew={}'.format(mew), xy = (mew-1, 0), arrowprops=dict(facecolor='black', width=1, shrink=0.1, headwidth=1))
    if val != None:
        plt.annotate(text = 'val={}'.format((val[0]+1, val[1])), xy = val, arrowprops=dict(facecolor='black', width=1, shrink=0.1, headwidth=1))
    plt.show()
