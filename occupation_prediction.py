# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 09:30:31 2016

@author: alsherman
"""

import requests
import pandas as pd

r = requests.get(r'http://api.datausa.io/api/?show=skill&sumlevel=all')
data_usa = r.json()

headers = data_usa['headers']
data = data_usa['data']

df = pd.DataFrame(data, columns=headers)
df.drop('value_rca', axis=1, inplace=True)
df.head()

df.skill.value_counts()
pd.get_dummies(df.skill, columns=df.value)

_pivot = df.pivot_table(index='cip', columns='skill', values='value')
type(pivot)
pivot = pivot.reset_index()
pivot.head()
pivot.columns
len(pivot.columns)

# X = pivot.drop('cip', axis=1)
X = pivot.['2.A.2.b']
y = pivot.cip

from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor()
knn.fit(X, y)
knn.predict()
