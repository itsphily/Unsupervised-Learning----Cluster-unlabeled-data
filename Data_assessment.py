import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## 
# This function prompts the user to print the result of the assessment
##
def assessment_print( description, print_data):
    yes_list = ['yes', 'y']
    answer_list=['yes', 'y','no', 'n']
    # Gets a yes or no answer
    answer = input('Do you want to print the {} (yes/no) ? '.format(description))
    # Makes sure we get the right input
    while answer.lower()  not in answer_list:
        answer = input('Do you want to print the {} (yes/no) ? '.format(description))
    if answer.lower() in yes_list:
        print('*******{}*******'.format(description))
        print(print_data)            
        print ('*'*30)
