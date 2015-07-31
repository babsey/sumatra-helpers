from aux import *
project,record,parameters = sumatra_record(__file__)
vars().update(parameters)

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
