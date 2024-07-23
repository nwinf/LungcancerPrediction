import numpy as np
import pandas as pd
import pickle
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, LabelEncoder

dataset = pd.read_csv('survey lung cancer.csv')
dataset['GENDER'] = LabelEncoder().fit_transform(dataset['GENDER'])
# Male = 1 , Female = 0
dataset['LUNG_CANCER'] = LabelEncoder().fit_transform(dataset['LUNG_CANCER'])
# YES = 1, NO = 0

X = dataset.drop('LUNG_CANCER', axis=1)
y = dataset['LUNG_CANCER']

# Creating the pipeline
pipeline = Pipeline([
    ('scale', StandardScaler(with_mean=True, with_std=True)),  # Standard scaling on 'age' column
    ('model', SVC())
])

# Fitting the pipeline on the entire dataset
pipeline.fit(X, y)


# Save the model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(pipeline, f)