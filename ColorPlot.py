import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def ColorLimits(fig: mpl.figure.Figure, N, vmin, vmax, cmap: str = 'viridis'):
    '''
    INPUT
    fig:  Figure handle
    N:    Number of bounds on colorbar. If you want 10 colors, N=11.
    vmin: Min value on colorbar
    vmax: Max value on colorbar
    cmap: Name of colormap as a string, e.g., "plasma" (optional)
    
    OUTPUT
    cmap:   The colormap 
    norm:   The normalized boundaries
    bounds: Boundaries between colors in the colorbar
    
    '''
    
    cmap = getattr(plt.cm,cmap)
    #cmap = plt.cm.plasma  # define the colormap
    cmaplist = [cmap(i) for i in range(cmap.N)]
    cmap = mpl.colors.LinearSegmentedColormap.from_list(
        'Custom cmap', cmaplist, cmap.N)
    bounds = np.linspace(vmin, vmax, N)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    
    cax = fig.add_axes([0.95, 0.1, 0.035, 0.8])
    cb=mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm,
                                 spacing='proportional', ticks=bounds, 
                                 boundaries=bounds)
    
    return cmap, norm, bounds, cb

def ColorLimitsPlot(axs,X,Y,Z,vmin,vmax,cmap,norm,bounds):
    
    axs.contourf(X,Y,Z,
                 vmin=vmin,vmax=vmax, 
                 cmap=cmap, norm=norm, levels=bounds,
                 extend='both') # There are values below -2!



#https://matplotlib.org/stable/tutorials/colors/colorbar_only.html
#https://stackoverflow.com/questions/14777066/matplotlib-discrete-colorbar
#https://stackoverflow.com/questions/46768028/how-does-pyplot-contourf-choose-
#colors-from-a-colormap
#https://matplotlib.org/stable/tutorials/colors/colormaps.html