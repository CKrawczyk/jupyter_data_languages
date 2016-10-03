from cycler import cycler

# see http://matplotlib.org/users/customizing.html for all options

style1 = {
    # Line styles
    'lines.linewidth': 1.5,
    'lines.antialiased': True,

    # Font
    'font.size': 16.0,

    # Axes
    'axes.linewidth': 1.5,
    'axes.titlesize': 'x-large',
    'axes.labelsize': 'large',
    'axes.prop_cycle': cycler('color', [
        '#1f78b4',  # blue
        '#33a02c',  # green
        '#e31a1c',  # red
        '#ff7f00',  # orange
        '#6a3d9a',  # purple
        '#b15928'   # brown
    ]),

    # Ticks
    'xtick.major.size': 6,
    'xtick.minor.size': 4,
    'xtick.major.width': 1.5,
    'xtick.minor.width': 1.5,
    'xtick.major.pad': 6,
    'xtick.minor.pad': 6,
    'xtick.labelsize': 'medium',

    'ytick.major.size': 6,
    'ytick.minor.size': 4,
    'ytick.major.width': 1.5,
    'ytick.minor.width': 1.5,
    'ytick.major.pad': 6,
    'ytick.minor.pad': 6,
    'ytick.labelsize': 'medium',

    # Legend
    'legend.fancybox': True,
    'legend.fontsize': 'large',
    'legend.scatterpoints': 5,
    'legend.loc': 'best',

    # Figure
    'figure.figsize': [8, 6],
    'figure.titlesize': 'large',

    # Images
    'image.cmap': 'magma',
    'image.origin': 'lower',

    # Saving
    'savefig.bbox': 'tight',
    'savefig.format': 'png',
}
