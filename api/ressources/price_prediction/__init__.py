## Fichier d'init
## C'est dans ce dossier que l'on chargera nos modèles pour en faire une variable globale appelable dans notre API
## De ce fait, le modèle sera en RAM et n'aura pas besoin d'être chargé à chaque appel

## EXEMPLE
# import mlflow.sklearn

import mlflow.sklearn
import os
cwd = os.getcwd()

# afficher le répertoire courant
print(cwd)

# inserer l'ID du modèle à utiliser
model_id = "08e4968c7bfe405c8234504387cb8e8d"
sk_model = mlflow.sklearn.load_model("../train/mlruns/0/"+model_id+"/artifacts/model")
