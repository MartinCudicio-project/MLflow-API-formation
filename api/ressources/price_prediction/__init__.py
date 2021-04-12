## Fichier d'init
## C'est dans ce dossier que l'on chargera nos modèles pour en faire une variable globale appelable dans notre API
## De ce fait, le modèle sera en RAM et n'aura pas besoin d'être chargé à chaque appel

## EXEMPLE
# import mlflow.sklearn

import mlflow.sklearn
import sklearn
import os
cwd = os.getcwd()

# afficher le répertoire courant
print(cwd)

# inserer l'ID du modèle à utiliser
# sk_model = mlflow.sklearn.load_model("relativePathToYour/mlruns/experienceNumber/ModelId/artifacts/model")

# --------------------------------------
#               corection 
# --------------------------------------

# model lin
# model_id = "ff68023169ce4d1fb7599b0b1ada57a3"
# model RF 1
# model_id = "90abfce2c59b4b16a1689dbdc1a1788a"
# model RF 2
model_id = "76a289fb1350438786347d35e5972498"

sk_model = mlflow.sklearn.load_model("../train/mlruns/1/"+model_id+"/artifacts/model")