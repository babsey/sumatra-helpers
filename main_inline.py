from aux import *
project,record,parameters = sumatra_record(__file__)

# PARAMS
seed = 65785        # seed for random number generator
distr = "uniform"   # statistical distribution to draw values from
n = 1000             # number of values to draw
# END OF PARAMS

# MAIN SCRIPT
import numpy as np
import pylab as pl

np.random.seed(seed)
distr = getattr(np.random, distr)
data = distr(size=n)

fig,ax = pl.subplots(1)
ax.hist(data)
# END OF MAIN SCRIPT

if record:
    np.savetxt('Data/%s.dat' %record.label, data)
    pl.savefig('Data/%s.png' %record.label)
    sumatra_save(project,record)

pl.show()
