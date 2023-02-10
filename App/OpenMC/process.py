import openmc
from IPython.display import Image
import numpy as np
import matplotlib.pyplot as plt

sp = openmc.StatePoint("statepoint.100.h5")
tally = sp.get_tally()
flux = tally.get_slice(scores=['flux'])
localHeat = tally.get_slice(scores=['heating-local'])
#heat = tally.get_slice(scores=['heating'])
#print(flux)
#print(fission)
flux.std_dev.shape = (100, 100)
flux.mean.shape = (100, 100)
localHeat.mean.shape = (100,100)
# heat.mean.shape = (100,100)
fig = plt.subplot(121)
fig.imshow(flux.mean)
fig2 = plt.subplot(122)
fig2.imshow(localHeat.mean)
# fig3 = plt.subplot(133)
# fig3.imshow(heat.mean)
plt.show()
# flux.std_dev.shape = (8000, 8000)
# flux.mean.shape = (8000, 8000)


#openmc.openmc-plot-mesh-tally("statepoint.100.h5")