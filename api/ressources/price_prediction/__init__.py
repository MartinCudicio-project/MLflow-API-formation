## Fichier d'init
## C'est dans ce dossier que l'on chargera nos modèles pour en faire une variable globale appelable dans notre API
## De ce fait, le modèle sera en RAM et n'aura pas besoin d'être chargé à chaque appel

## EXEMPLE
# import pandas as pd
# from sklearn.externals import joblib
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.preprocessing import LabelEncoder,OneHotEncoder
# from sklearn.decomposition import TruncatedSVD
# from sklearn.ensemble import RandomForestClassifier

import mlflow.sklearn
import os
cwd = os.getcwd()
# display currend directory
print(cwd)
sk_model = mlflow.sklearn.load_model("../train/mlruns/0/96b71f5653f9494496a63bbd54628877/artifacts/model")
# StatAuteurPASSE = pd.read_pickle('resources/ressoc/ComptageAuteur.pkl')
