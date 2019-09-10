import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


def read_data_remove_zeros(csv):
    data = pd.read_csv(csv)
    data = data[data['Reported'] == 'Y'].copy()
    # data.set_index('School_Name', inplace=True)
    #data.rename(columns={data.columns[1]: 'Enrollment'}, inplace=True)
    # data = data[data['Enrollment'] > 0].copy()
    data.sort_index()
    return(data)