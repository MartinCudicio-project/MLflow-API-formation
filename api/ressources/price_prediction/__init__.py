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

model_id = "e6dc28fbd8264db59799a91f4a700b4c"
sk_model = mlflow.sklearn.load_model("../train/mlruns/1/"+model_id+"/artifacts/model")
