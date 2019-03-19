from autofeat import AutoFeatRegression
import numpy as np
import pandas as pd
import sklearn.linear_model as lm

X = np.load('data/X.npy')
target = np.load('data/y.npy')

afreg = AutoFeatRegression(n_jobs=4)
try:
    df = afreg.fit_transform(X, target)
except:

    eps = 1e-08
    X = np.load('/tmp/X_error.npy')
    target = np.load('/tmp/target_error.npy')

    reg = lm.LassoLarsCV(eps=eps)
    reg.fit(X, target)
