import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Data_assessment import assessment_print

## Data Wrangling
# In this section we are loading, assessing, cleaning the datasets
##

# Importing the data
azdias = pd.read_csv('Udacity_AZDIAS_Subset.csv', delimiter=';')


# Data Assessment
# print the result of the assessment
assessment_print('Head of the dataframe', azdias.head())
assessment_print('Dataframe info', azdias.info())
assessment_print('General description of the dataframe', azdias.describe())
assessment_print('Null values', pd.DataFrame(azdias.isnull().sum()))

# Need to print a conclusion of the assessment