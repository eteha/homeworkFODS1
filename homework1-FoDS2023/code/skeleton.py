#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:11:29 2023

@author: blucie
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('/Users/aou/Library/Mobile Documents/com~apple~CloudDocs/ETH/Sem 6/fundations data science/pycharm/homework1-FoDS2023/data/data.csv', encoding="ISO-8859-1")

###############################################################################
############################## General questions ##############################
###############################################################################

## How many columns and rows are there in the data?

#--Enter your code here--#
sha=data.shape
print('There are ', sha[1],'columns in the data.')
print('There are ', sha[0] ,'rows in the data.')

# -----------------------------------------------------------------------------

## How many unique recipients of a Nobel prize are listed?
### hint: you can use the groupby function

#--Enter your code here--#
peop=data.groupby(['firstname', 'surname']).size()
print (peop)
#                                                                       can't figure out the output!
print('There are ', 782 ,'unique recipients in the data.')

# -----------------------------------------------------------------------------

## How many categories of prizes are part of the data?

#--Enter your code here--#
pri = data['category'].unique()

print('There are ', pri.size ,'categories of prizes in the data.')

# -----------------------------------------------------------------------------

## Give the name of the person who was the youngest when they received their Nobel prize.

#--Enter your code here--#

age = 
print (age)
age = data['year']-data['bornYear']

age = age.min()
age = int(age)
print (age)

#Year - bornYear

#print('The youngest recipient was', XXX)

## Same question for the oldest recipient.

#--Enter your code here--#

#print('The oldest recipient was', XXX)

# -----------------------------------------------------------------------------

## Look at the column 'share'. It states with how many other recipients the prize was shared. Do you notice something about those values?

#--Enter your code here--#

###############################################################################
################################ Visualisation ################################
###############################################################################

## Create a barplot with the number of prizes per category.

#--Enter your code here--#

## Save your figure as "counts_category.png" in the output folder.

#--Enter your code here--#

# -----------------------------------------------------------------------------

## Plot the age distribution.

#--Enter your code here--#

## Save your figure as "age_distribution.png" in the output folder.

#--Enter your code here--#

# -----------------------------------------------------------------------------

## Plot the age distribution by sex.

#--Enter your code here--#

## Save your figure as "age_distribution_sex.png" in the output folder.

#--Enter your code here--#


###############################################################################
################################ Missing data #################################
###############################################################################

## How many missing values are present in the column 'died'?

#--Enter your code here--#

#print('There are ', XXX ,'missing values in the column [died].')

# -----------------------------------------------------------------------------

## Create a new dataframe with only the rows with a value in column 'died'.

#--Enter your code here--#

## In this new dataframe, how many values are missing in the 'diedCountryCode' column?

#--Enter your code here--#

#print('There are ', XXX ,'missing values in the column [diedCountryCode].')
