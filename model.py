import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pickle

df = pd.read_excel('Задача.xlsx')

df.rename(columns={"Возраст, лет":"Возраст", "Стаж вождения, лет":"Стаж вождения", "Убыточность, %":"Убыточность",
                  "Уровень заработной платы, руб/год":"Уровень заработной платы"}, inplace=True)

df = df.drop('Персона', axis=1)

X = df.values
scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=100)
kmeans.fit(scaled_X)
predict = kmeans.predict(scaled_X)

pickle.dump(kmeans, open('model.pkl','wb'))