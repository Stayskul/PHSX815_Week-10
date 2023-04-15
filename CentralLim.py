
import numpy as np
import matplotlib.pyplot as plt
from Random.Random import Random
import sys


if __name__ == "__main__":
    # number of sample
    num = [1, 10, 50, 100] 

    #seed
    seed = 5555
    # list of sample means
    means = [] 
    
    #sigx of log norm
    sigx = 5

    #mux of log norm
    mux = 20
    
    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-mux' in sys.argv:
        p = sys.argv.index('-mux')
        mutemp = float(sys.argv[p+1])
        if mutemp > 0:
            mux = mutemp
    if '-sigx' in sys.argv:
        p = sys.argv.index('-sigx')
        sigtemp = float(sys.argv[p+1])
        if sigtemp > 0:
            sigx = sigtemp
   
    # Generating 1, 10, 50, 100 random numbers according to lognormal dist
    # taking their mean and appending it to list means.
    for j in num:
        
        random=Random(seed)
        
        x=[np.mean(random.SkewNorm3(mux,sigx,Nmeas=j)) for _i in range(1000)]
        means.append(x)

    k = 0  
    # plotting all the means in one figure
    fig, ax = plt.subplots(2, 2, figsize =(8, 8))
    for i in range(0, 2):
        for j in range(0, 2):
            # Histogram for each x stored in means
            ax[i, j].hist(means[k], 50, density = True)
            ax[i, j].set_title(label = num[k])
            k = k + 1
    plt.show()
