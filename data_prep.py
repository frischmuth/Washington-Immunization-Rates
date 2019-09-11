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

def read_demographic_data(csv):
    data = pd.read_csv(csv)
    data['School_District'] = data['DistrictName'].str.upper()
    data['School_Name'] = data['SchoolName'].str.upper()
    data.set_index(['School_District', 'School_Name'], inplace=True)
    data.sort_index()
    return(data)

def filter_percentages(data):
    columns_percent = ['Enrollment', 'ESD', 'City', 'County', 'Percent_complete_for_all_immunizations', 'Percent_conditional', 'Percent_out_of_compliance', 
                        'Percent_with_any_exemption', 'Percent_with_medical_exemption', 'Percent_with_personal_exemption', 'Percent_with_religious_exemption', 'Percent_with_religious_membership_exemption']
    return(data[data[columns_percent]])



def filter_counts(data):
    columns_counts = ['Enrollment', 'ESD', 'City', 'County', 'Number_complete_for_all_immunizations', 'Number_conditional', 'Number_out_of_compliance', 
                        'Number_with_any_exemption', 'Number_with_medical_exemption', 'Number_with_personal_exemption', 'Number_with_religious_exemption', 'Number_with_religious_membership_exemption']
    return(data[data[columns_counts]])
