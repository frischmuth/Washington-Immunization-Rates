import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import math


def read_vaccine_data(csv):
    data = pd.read_csv(csv,low_memory=False)
    data = data[data['Reported'] == 'Y'].copy()
    data['School_District'] = data['School_District'].str.upper()
    data['School_Name'] = data['School_Name'].str.upper()
    data.set_index(['School_District', 'School_Name'], inplace=True)
    data.rename(columns={data.filter(like='enroll').columns[0]: 'Enrollment'}, inplace=True)
    data = data[data['Enrollment'] > 0].copy()
    data.sort_index(inplace=True)
    return(data)



def filter_percentages(data):
    columns_percent = ['Enrollment', 'ESD', 'City', 'County', 'Percent_complete_for_all_immunizations', 'Percent_conditional', 'Percent_out_of_compliance', 
                        'Percent_with_any_exemption', 'Percent_with_medical_exemption', 'Percent_with_personal_exemption', 'Percent_with_religious_exemption', 'Percent_with_religious_membership_exemption']
    return(data[data[columns_percent]])



def filter_counts(data):
    columns_counts = ['Enrollment', 'ESD', 'City', 'County', 'Number_complete_for_all_immunizations', 'Number_conditional', 'Number_out_of_compliance', 
                        'Number_with_any_exemption', 'Number_with_medical_exemption', 'Number_with_personal_exemption', 'Number_with_religious_exemption', 'Number_with_religious_membership_exemption']
    return(data[data[columns_counts]])

def read_demographic_data(csv):
    '''
    Read in the csv and create multiindex with school district and school name. Also removes unneeded columns
    '''
    data = pd.read_csv(csv, low_memory=False)
    data = data[data['OrganizationLevel']=='School'].copy()
    data['DistrictName'] = data['DistrictName'].str.upper()
    data['SchoolName'] = data['SchoolName'].str.upper()
    data.rename({'DistrictName':'School_District', 'SchoolName':'School_Name'}, axis='columns',inplace=True)
    data.set_index(['School_District', 'School_Name'], inplace=True)
    data.sort_index(inplace=True)
    data.drop(columns=data.columns[4:9],inplace=True)
    return(data)

def convert_to_fractions(data):
    '''
    Take the count of all of the different demographics and converts it to fractions by dividing by the total number of students
    '''
    all_students_index = data.columns.get_loc('All Students')
    data.iloc[:,all_students_index+1:] = data.iloc[:,all_students_index+1:].fillna(0)
    counts = data.columns[all_students_index+1:]
    for count in counts:
        data[count] = data[count]/data['All Students']
    return(data)

def all_kindergarten(data):
    kindergarten_data = data[(data['Gradelevel']=='Full Day Kindergarten') | (data['Gradelevel']=='Half Day Kindergarten')].groupby(['School_District', 'School_Name']).sum()
    return(kindergarten_data)

def all_sixth(data):
    six_data = data[data['Gradelevel']=='Sixth Grade']
    return(six_data)
