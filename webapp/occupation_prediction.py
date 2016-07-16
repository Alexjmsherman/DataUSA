# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 09:30:31 2016

@author: alsherman
"""

import requests
import pandas as pd


class predictive_models:

    def __init__(self):
        self.cip_names_and_ids = self.get_cip_names_and_ids()
        self.skill_names_and_ids = self.get_skill_names_and_ids()
        self.model = self.build_model()

    def predict(self, prediction):
        pred = self.model.predict_proba([prediction])

        skill_names = self.cip_names_and_ids['id']
        df = zip(skill_names, pred[0])
        df = pd.DataFrame(df, columns=['cip','prob'])
        df = df.sort_values('prob', ascending=False)

        df = pd.merge(df, self.cip_names_and_ids, left_on='cip', right_on='id')

        df.drop('id', axis=1, inplace=True)


        print df[0:5]
        return df[0:5]

    @staticmethod
    def build_model():
        # request data on college majors and relevant skills
        r = requests.get(r'http://api.datausa.io/api/?show=skill&sumlevel=all')
        data_usa = r.json()

        headers = data_usa['headers']
        data = data_usa['data']

        df = pd.DataFrame(data, columns=headers)
        df.drop('value_rca', axis=1, inplace=True)

        pivot = df.pivot_table(index='cip', columns='skill', values='value')
        pivot = pivot.reset_index()

        # todo: use all skills - first five for testing
        X = pivot[['2.A.1.a', '2.A.1.b', '2.A.1.c', '2.A.1.d', '2.A.1.e']]
        # X = pivot.drop('cip', axis=1)  # feature matrix
        y = pivot.cip  # response

        from sklearn.neighbors import KNeighborsClassifier
        knn = KNeighborsClassifier(n_neighbors=5)
        knn.fit(X, y)

        return knn

    @staticmethod
    def get_cip_names_and_ids():
        # get id to name matches
        r = requests.get(r'http://api.datausa.io/attrs/cip/')
        cip_course_data = r.json()

        cip_headers = cip_course_data['headers']
        cip_data = cip_course_data['data']

        skill_id_df = pd.DataFrame(cip_data, columns=cip_headers)
        cip_names_and_ids = skill_id_df[['id','name_long']]

        return cip_names_and_ids

    @staticmethod
    def get_skill_names_and_ids():
        r = requests.get(r'http://api.datausa.io/attrs/skill/')
        skill_data = r.json()

        headers = skill_data['headers']
        data = skill_data['data']

        skill_id_df = pd.DataFrame(data, columns=headers)
        skill_names_and_ids = skill_id_df[['id','name']]

        return skill_names_and_ids


if __name__ == "__main__":
    p = predictive_models()
    g = [1. for n in range(0,5)]
    p.predict(g)