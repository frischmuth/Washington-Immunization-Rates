import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats


def read_vaccine_data(csv):
    data = pd.read_csv(csv)
    data = data[data['Reported'] == 'Y'].copy()
    data['School_District'] = data['School_District'].str.upper()
    data['School_Name'] = data['School_Name'].str.upper()
    data.set_index(['School_District', 'School_Name'], inplace=True)
    data.rename(columns={data.filter(like='enroll').columns[0]: 'Enrollment'}, inplace=True)
    data = data[data['Enrollment'] > 0].copy()
    data.sort_index()
    return(data)