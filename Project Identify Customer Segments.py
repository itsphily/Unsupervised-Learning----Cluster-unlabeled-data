import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
plt.style.use('ggplot')

## Data Wrangling
# In this section we are loading, assessing, cleaning the datasets
##



# Importing the data
azdias = pd.read_csv('Udacity_AZDIAS_Subset.csv', delimiter=';')
# Inspect the dataframe
azdias.head()
azdias.info()

# Data Assessment

## Print the result of the assessment
def assessment_print(print_result = 'yes'):
    yes_list = ['yes', 'y']
    assessment_list_missing_values = [
        'CJT_GESAMTTYP has 4854 null values'
        'GFK_URLAUBERTYP  has 4854 null values'
        'LP_LEBENSPHASE_FEIN  has 4854 null values'
        'LP_LEBENSPHASE_GROB has 4854 null values'
        'LP_FAMILIE_FEIN has 4854 null values'
        'LP_FAMILIE_GROB has 4854 null values'
        'LP_STATUS_FEIN has 4854 null values'
        'LP_LEBENSPHASE_GROB has 4854 null values'
        'RETOURTYP_BK_S has 4854 null values'
        'SOHO_KZ has 73499 null values'
        'TITEL_KZ has 73499 null values'
        'ALTER_HH has 73499 null values'
        'ANZ_PERSONEN  has 73499 null values'
        'ANZ_TITEL has 73499 null values'
        'HH_EINKOMMEN_SCORE has 28343 null values'
        'KK_KUNDENTYP has 584612 null values'
        'W_KEIT_KIND_HH has 107602 null values'
        'ANZ_HAUSHALTE_AKTIV has 93148 null values'
        'ANZ_HH_TITEL has 97008 null values '
        'GEBAEUDETYP has 93148 null values'
        'KONSUMNAEHE has 73969 null values'
        'MIN_GEBAEUDEJAHR has 93148 null values'
        'OST_WEST_KZ has 93148 null values'
        'WOHNLAGE has 93148 null values'
        'CAMEO_DEUG_2015 has 98979 null values'
        'CAMEO_DEU_2015 has 98979 null values'
        'CAMEO_INTL_2015 has 98979 null values'
        'KBA05_ANTG1 has 133324 null values'
        'KBA05_ANTG2 has 133324 null values'
        'KBA05_ANTG3 has 133324 null values'
        'KBA05_ANTG4 has 133324 null values'
        'KBA05_BAUMAX has 133324 null values'
        'KBA05_GBZ has 133324 null values'
        'BALLRAUM has 93740 null values'
        'EWDICHTE has 93740 null values'
        'INNENSTADT has 93740 null values'
        'GEBAEUDETYP_RASTER 93155 has null values'
        'KKK has 121196 null values'
        'MOBI_REGIO has 133324 null values'
        'ONLINE_AFFINITAET has 4854 null values'
        'REGIOTYP has null values'
        'KBA13_ANZAHL_PKW has null values'
        'PLZ8_ANTG1 has 121196 null values'
        'PLZ8_ANTG2 has 116515 null values'
        'PLZ8_ANTG3 has 116515 null values'
        'PLZ8_ANTG4 has 116515 null values'
        'PLZ8_BAUMAX has 116515 null values'
        'PLZ8_HHZ has 116515 null values'
        'PLZ8_GBZ has 116515 null values'
        'ARBEIT has null 97216 values'
        'ORTSGR_KLS9 has 97216 null values'
        'RELAT_AB has null 97216 values'      
    ]

    if print_result.lower() in yes_list:
        print('*******Missing Values*******')
        for assessment in assessment_list_missing_values:
            print(assessment)
        print ('*'*30)


# Prompts the user to print the result of the assessment
answer_list=['yes', 'y','no', 'n']
print_result = input('Do you want to print the result of the assessment (yes/no) ? ')
# Makes sure we 
while print_result.lower()  not in answer_list:
    print_result = input('Do you want to print the result of the assessment (yes/no) ? ')
assessment_print(print_result)
