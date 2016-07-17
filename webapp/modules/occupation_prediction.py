# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 09:30:31 2016

@author: alsherman
"""

import requests
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from data_usa_names_and_ids import DataUsaNamesAndIds


class PredictiveModels:
    """ creates a classification model using data from the DataUSA api to predict a college major based on an
    individuals personal ranking of ~30 of their own skills.

    Notes: There are ~2300 college majors with a single instance of each.
    """

    def __init__(self, names_and_ids):
        self.cip_names_and_ids = names_and_ids.cip_names_and_ids
        self.skill_names_and_ids = names_and_ids.skill_names_and_ids
        self.model = self.build_model()

    def predict(self, prediction):
        """ predict which college majors match a users skillset

        :param prediction: a list of users self-rated scores for all required skills

        :return: a dataframe of cips, college majors, and probabilities sorted acsending by  top probability matches
        """

        pred = self.model.predict_proba([prediction])

        career_ids = self.cip_names_and_ids['id']
        career_names = self.cip_names_and_ids['name_long']
        df = zip(career_ids, pred[0], career_names)
        df = pd.DataFrame(df, columns=['cip', 'prob', 'name_long'])

        df.sort_values('prob', ascending=False, inplace=True)

        print df[0:5]
        return df[0:5]

    @staticmethod
    def build_model():
        """ request cip and skill data from DataUSA and develop predictive model using scikit-learn

        :return: fit model ready to accept user input to make a prediction
        """

        # request data on college majors and relevant skills
        r = requests.get(r'http://api.datausa.io/api/?show=skill&sumlevel=all')
        data_usa = r.json()

        headers = data_usa['headers']
        data = data_usa['data']

        df = pd.DataFrame(data, columns=headers)
        df.drop('value_rca', axis=1, inplace=True)

        # reshape data so that each skill becomes a single column (i.e. feature for the model)
        pivot = df.pivot_table(index='cip', columns='skill', values='value')
        pivot = pivot.reset_index()

        # todo: use all skills - first five for testing
        X = pivot[['2.A.1.a', '2.A.1.b', '2.A.1.c', '2.A.1.d', '2.A.1.e']]
        # X = pivot.drop('cip', axis=1)  # feature matrix
        y = pivot.cip  # response

        knn = KNeighborsClassifier(n_neighbors=5)
        knn.fit(X, y)

        return knn


if __name__ == "__main__":
    names_and_ids = DataUsaNamesAndIds()
    p = PredictiveModels(names_and_ids)
    g = [1. for i in range(0, len(p.skill_names_and_ids))]
    p.predict(g)
