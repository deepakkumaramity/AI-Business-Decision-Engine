import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.DataFrame({
    "income": [20000, 50000, 30000, 70000],
    "loan": [10000, 20000, 15000, 30000],
    "default": [0, 1, 0, 1]
})

X = df[["income", "loan"]]
y = df["default"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

os.makedirs("../models", exist_ok=True)
pickle.dump(model, open("../models/model.pkl", "wb"))

print("Model trained and saved")
