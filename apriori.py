# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv' , header = None) # header = none ; heading row becomes 1st row  and heading row becomes normal(ie 1,2,3,4 )
transactions = []                     # convert dataset into list
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])  # values - to extract values 
                                                                           # str - values will be in '' 

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)  
# min-length = least no of products required in bascket
# other values can be anything according to your dataset

# Visualising the results
results = list(rules)