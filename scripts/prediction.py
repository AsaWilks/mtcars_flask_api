#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn import linear_model

data = pd.read_csv("scripts/mtcars.csv")

labels = data['mpg']
train1 = data.drop(['model', 'mpg', 'gear',	'carb'],axis=1)

col_imp = ["cyl", "disp", "hp", "drat", "wt", "qsec", "vs"]

lm = LinearRegression()
lm.fit(train1, y)

def predict(dict_values, col_imp=col_imp, lm=lm):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1,-1)
    y_pred = lm.predict(x)[0]
    return y_pred
