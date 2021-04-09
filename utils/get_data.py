import numpy as np
import pandas as pd

# import Data
# https://raw.githubusercontent.com/rashida048/Datasets/master/home_data.csv

raw_data = pd.read_csv('https://raw.githubusercontent.com/rashida048/Datasets/master/home_data.csv')

# on convertit en datetime notre colonne de date
raw_data["date"] = pd.to_datetime(raw_data["date"])

# on definit un nouveau df, une date = un coefficient d'ajustement de prix
df_transfo = raw_data[["date"]].drop_duplicates().sort_values('date').reset_index().drop(['index'],axis=1)

# transformation prix final : 1.03 soit 103% 
# creation d'un vecteur pour chaque date, avec transformation lineaire de +5%
coef_augmentation_final = 1.15
vect_ajust = [ float(x) for x in np.linspace(start = 1, stop = coef_augmentation_final, num = df_transfo["date"].count())]

# ajout colonne au dataFrame transfo
df_transfo["coef_ajustement"] = vect_ajust
df_transfo

# merge sur les dates du dataset original
modif_raw_data= raw_data.merge(df_transfo,how='left',on='date').sort_values('date')

# on cree un nouveau dataFrame avec des nouveaux prix de ventes ajustes
data = modif_raw_data.copy()
data['price'] = data['price']*data['coef_ajustement']

data.to_csv('./data/home_data.csv')
print("home_data.csv created")
