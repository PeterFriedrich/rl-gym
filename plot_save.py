# saving and plotting functions

import numpy
import os
import sys
import matplotlib.pyplot as plt

# from hands_on_ml:
# saving figures
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "r"

def save_fig(fig_id, tight_layout=True):
    """ takes in a fig id and layout, and saves the figure
        to the images directory
    """
    path = os.path.join(PROJECT_ROOT_DIR, "images", fig_id + ".png")
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format='png', dpi=300)
