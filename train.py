import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# load Dataset
df= pd.read_csv("dataset/movies.csv")

# Features & Target
x= df[["Age", "Action", "Comedy"]]
y= df["Genre"]

#Split
x_train, x_test, y_train, y_test = train_test_split(
    x,y, test_size=0.2, random_state=42
)

#train
model = DecisionTreeClassifier(random_state=42)
model.fit(x_train, y_train)

#save model
joblib.dump(model, "model.pkl")

print("Project1 Trained Successfully ✅")