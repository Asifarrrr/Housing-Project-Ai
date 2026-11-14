import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
#---------------------------------- (Cleaning Data) --------------------------------------
df = None
try:
    df = pd.read_csv(r"C:\Users\pc\PycharmProjects\WelcomeScreen\Mini Projects\Housing_Project\data\housing.csv")
except FileNotFoundError:
    pass
df = df.dropna(subset = 'total_bedrooms')

df['total_rooms'] = df['total_rooms'].astype(int)
df['total_bedrooms'] = df['total_bedrooms'].astype(int)

df = pd.get_dummies(df,columns = ['ocean_proximity'],drop_first = True,dtype = int)
df = df.rename(
    columns = {
    'ocean_proximity_<1H OCEAN': 'ocean_proximity_1H_OCEAN',
    'ocean_proximity_NEAR BAY': 'ocean_proximity_NEAR_BAY',
    'ocean_proximity_NEAR OCEAN': 'ocean_proximity_NEAR_OCEAN'
})
#------------------------------------- (Ai Model) ----------------------------------------
x = df.drop(columns = ['median_house_value'])
y = df['median_house_value']

x_train,x_test,y_train,y_test = train_test_split(
    x,
    y,
    test_size = 0.2,
    random_state = 42
)
model = RandomForestRegressor(
    max_depth = 5,
    min_samples_leaf = 5,
    min_samples_split = 10,
    random_state = 42
)
model.fit(x_train,y_train)

joblib.dump(df,r"C:\Users\pc\PycharmProjects\WelcomeScreen\Mini Projects\Housing_Project\models\data_frame.pkl")
joblib.dump(model,r"C:\Users\pc\PycharmProjects\WelcomeScreen\Mini Projects\Housing_Project\data\house_model.pkl")
joblib.dump(list(x.columns),r"C:\Users\pc\PycharmProjects\WelcomeScreen\Mini Projects\Housing_Project\models\model_columns.pkl")