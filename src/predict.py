import pickle
import numpy as np

model = pickle.load(open("../models/model.pkl", "rb"))

def predict(income, loan):
    data = np.array([[income, loan]])
    return model.predict(data)
