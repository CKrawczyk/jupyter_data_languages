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
        '#1f77b4',  # blue
        '#ff7f0e',  # orange
        '#2ca02c',  # green
        '#d62728',  # red
        '#9467bd',  # purple
        '#8c564b',  # brown
        '#e377c2',  # magenta
        '#7f7f7f',  # gray
        '#bcbd22',  # yellow
        '#17becf',  # cyan
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
