import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


plt.style.use('ggplot')


def read_data_remove_zeros(csv):
    data = pd.read_csv(csv)
    return(data)