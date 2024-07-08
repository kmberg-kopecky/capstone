# -*- coding: utf-8 -*-
"""final final final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oh7RAKdGCUoYal22h9bD9YHdv315rUVO

# Decision Tree Regression

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics


#from google.colab import files

#uploaded = files.upload()

"""## Importing the dataset"""

from google.colab import drive
drive.mount('/content/drive')

dataset = pd.read_csv('/content/drive/MyDrive/final proj/mushroom data final.csv')

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
dataset['cap-shape'] = label_encoder.fit_transform(dataset['cap-shape'])
dataset['cap-shape'].unique()
print(dataset['cap-shape'])

# 0 -> b = bell
# 1 -> f = flat
# 2 -> s = sunken
# 3 -> x = convex

label_encoder = LabelEncoder()
dataset['cap-surface'] = label_encoder.fit_transform(dataset['cap-surface'])
dataset['cap-surface'].unique()
print(dataset['cap-surface'])

# 0 -> f = fibrous
# 1 -> s = smooth
# 2 -> y = scaly
label_encoder = LabelEncoder()
dataset['cap-color'] = label_encoder.fit_transform(dataset['cap-color'])
dataset['cap-color'].unique()
print(dataset['cap-color'])

# 0 -> g = grey
# 1 -> n = brown
# 2 -> w = white
# 3 -> y = yellow
label_encoder = LabelEncoder()
dataset['odor'] = label_encoder.fit_transform(dataset['odor'])
dataset['odor'].unique()
print(dataset['odor'])

# 0 -> a = almond
# 1 -> l = anise
# 2 -> n = none
# 3 -> p = pungent

label_encoder = LabelEncoder()
dataset['gill-spacing'] = label_encoder.fit_transform(dataset['gill-spacing'])
dataset['gill-spacing'].unique()
print(dataset['gill-spacing'])

# 0 -> c = close
# 1 -> w = crowded
label_encoder = LabelEncoder()
dataset['gill-color'] = label_encoder.fit_transform(dataset['gill-color'])
dataset['gill-color'].unique()
print(dataset['gill-color'])


# 0 -> g = grey
# 1 -> h = chocolate
# 2 -> k = black
# 3 -> n = brown
# 4 -> p = pink
# 5 -> w = white

label_encoder = LabelEncoder()
dataset['stalk-shape'] = label_encoder.fit_transform(dataset['stalk-shape'])
dataset['stalk-shape'].unique()
print(dataset['stalk-shape'])

# 0 -> e = enlarging
# 1 -> t = tapering

label_encoder = LabelEncoder()
dataset['population'] = label_encoder.fit_transform(dataset['population'])
dataset['population'].unique()
print(dataset['population'])

# 0 -> a = abundant
# 1 -> n = numerous
# 2 -> s = scattered
# 3 -> v = several
# 4 -> y = solitary

label_encoder = LabelEncoder()
dataset['habitat'] = label_encoder.fit_transform(dataset['habitat'])
dataset['habitat'].unique()
print(dataset['habitat'])

# 0 -> d = woods
# 1 -> g = grasses
# 2 -> m = meadows
# 3 -> p = paths
# 4 -> u = urban

label_encoder = LabelEncoder()
dataset['class'] = label_encoder.fit_transform(dataset['class'])
dataset['class'].unique()
print(dataset['class'])

# 0 -> e = edible
# 1 -> p = poisonous

from google.colab import drive
drive.mount('/content/drive')

"""## Training the Decision Tree Regression model on the whole dataset"""

x = dataset.iloc[:, 0:9].values
y = dataset.iloc[:, 9].values

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(x,y)

"""## Predicting a new result"""

#Test with unseen data
#Answer should be 0

regressor.predict([[3,2,2,0,0,3,0,2,1]])

#Test with unseen data
#Answer should be 0

regressor.predict([[0,1,3,1,0,5,0,1,2]])

#Test with unseen data
#Answer should be 0

regressor.predict([[3,1,3,0,0,5,0,1,1]])

#Test with unseen data
#Answer should be 0

regressor.predict([[0,2,3,0,0,0,0,1,1]])

#Test with unseen data
#Answer should be 0

regressor.predict([[3,2,2,0,0,3,0,2,1]])

#Test with unseen data
#Answer should be 0

regressor.predict([[3,1,2,1,0,0,0,1,2]])

#Test with unseen data
#Answer should be 0

regressor.predict([[0,1,3,0,0,5,0,2,2]])

#Test with unseen data
#Answer should be 0

regressor.predict([[0,2,3,0,0,5,0,2,1]])

#Test with unseen data
#Answer should be 1
regressor.predict([[3,1,1,3,0,3,0,3,1]])

#Test with unseen data
#Answer should be 1

regressor.predict([[3,2,1,3,0,2,0,2,4]])

#Test with unseen data
#Answer should be 1

regressor.predict([[3,1,1,3,0,2,0,3,4]])

input1 = input("What is the cap shape?\n 0 -> bell\n 1 -> flat\n 2 -> sunken\n 3 -> convex:")

input2 = input("What is the cap surface?\n 0 -> fibrous\n 1 -> smooth\n 2 -> scaly:")

input3 = input("What is the cap color?\n 0 -> grey\n 1 -> brown\n 2 -> white\n 3 -> yellow:")

input4 = input("What is the odor?\n 0 -> almond\n 1 -> anise\n 2 -> none\n 3 -> pungent:")

input5 = input("What is the gill spacing?\n 0 -> close\n 1 -> crowded:")

input6 = input("What is the gill color?\n 0 -> grey\n 1 -> chocolate\n 2 -> black\n 3 -> brown\n 4 -> pink\n 5 -> white:")

input7 = input("What is the stalk shape?\n 0 -> enlarging\n 1 -> tapering:")

input8 = input("What is the population?\n 0 -> abundant\n 1 -> numerous\n 2 -> scattered\n 3 -> several\n 4 -> solitary:")

input9 = input("What is the habitat?\n 0 -> woods\n 1 -> grasses\n 2 -> meadows\n 3 -> paths\n 4 -> urban:")


new_row = pd.DataFrame([[input1, input2, input3, input4, input5, input6, input7, input8, input9]], columns=['cap-shape','cap-surface','cap-color','odor','gill-spacing','gill-color','stalk-shape','population','habitat']) # Create a new DataFrame from the input
dataset = pd.concat([dataset, new_row], ignore_index=True) # Concatenate the new row to the existing DataFrame


print(dataset)

if(regressor.predict([[input1, input2, input3, input4, input5, input6, input7, input8, input9]])==1):
  print("Poisonous")
else:
  print("Edible")