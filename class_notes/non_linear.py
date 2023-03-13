import pyximport
pyximport.install()
import numpy as np
from matplotlib.pyplot import figure, legend, plot, show, xlim, title, xlabel, ylabel, ylim
from landlab.plot.imshow import imshow_grid
from landlab import RasterModelGrid
from landlab.components import TaylorNonLinearDiffuser

mg = RasterModelGrid((41, 5), 5.0)
z_vals = mg.add_zeros("topographic__elevation", at="node")

# initialize some values for plotting
ycoord_rast = mg.node_vector_to_raster(mg.node_y)
ys_grid = ycoord_rast[:, 2]

# set boundary condition.
mg.set_closed_boundaries_at_grid_edges(True, False, True, False)

D = 0.01  # initial value of 0.01 m^2/yr
Sc = 0.5  # critical slope value, units of m/m
nonlin_diffuse = TaylorNonLinearDiffuser(mg, linear_diffusivity=D, slope_crit=Sc, dynamic_dt=True)