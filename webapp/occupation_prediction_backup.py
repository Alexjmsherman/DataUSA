# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 09:30:31 2016

@author: alsherman
"""

import requests
import pandas as pd

def predict(prediction):
    r = requests.get(r'http://api.datausa.io/api/?show=skill&sumlevel=all')
    data_usa = r.json()

    headers = data_usa['headers']
    data = data_usa['data']

    df = pd.DataFrame(data, columns=headers)
    df.drop('value_rca', axis=1, inplace=True)

    pivot = df.pivot_table(index='cip', columns='skill', values='value')
    pivot = pivot.reset_index()

    # X = pivot.drop('cip', axis=1)
    X = pivot[['2.A.1.a',
                '2.A.1.b',
                '2.A.1.c',
                '2.A.1.d',
                '2.A.1.e'
                ]]

    y = pivot.cip

    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier()
    knn.fit(X, y)

    pred = knn.predict_proba([prediction])

    df = zip(y, pred[0])
    df = pd.DataFrame(df, columns=['cip','prob'])

    # get id to name matches
    r = requests.get(r'http://api.datausa.io/attrs/cip/')
    data_usa = r.json()
    headers = data_usa['headers']
    data = data_usa['data']
    skill_id_df = pd.DataFrame(data, columns=headers)
    id_match = skill_id_df[['id','name_long']]

    df = pd.merge(df, id_match, left_on='cip', right_on='id')
    df.drop('id', axis=1, inplace=True)
    df = df.sort_values('prob', ascending=False)

    return df[0:5]

if __name__ == "__main__":
    p = predict(prediction=[1,2])
    print p
