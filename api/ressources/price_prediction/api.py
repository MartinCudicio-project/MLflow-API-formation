import json

import falcon
import pandas as pd
# Chargement de fonctions spécifique d'un fichier (pour la clarté du code)
# from resources.dossierprojet.fonctions import fonction
from ressources.price_prediction import sk_model

# class pour les prédictions stream
class PredictStream:
    
    def on_post(self, req, resp):
        # On traite les arguments envoyé par le POST, et on traite correctement l'erreur si le JSON n'est pas correct
        # A ne pas changer
        try:
            body_raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, "Error", ex.message)
        try:
            body_json = json.loads(body_raw_json, encoding="utf-8")
        except ValueError:
            raise falcon.HTTPError(
                falcon.HTTP_400,
                "Malformed JSON",
                "Could not decode the request body. The " "JSON was incorrect.",
            )
        # On traite les erreurs bloquantes comme un paramètre manquant
        # Rapporte toi au schéma pour savoir les features entrantes
        try:
            # content=body_json["content"]
            # content1=body_json["content1"]
            

        # except ValueError:
        except Exception as e:
            print(e)
            raise falcon.HTTPError(
                falcon.HTTP_400, "Missing Parameter", "Missing content parameter"
            )

        # On réalise notre predict issu du modèle chargé dans le __init__.py
        # prediction=sk_model.predict([content,content1])
        
        
        # On renvoie la prédiction
        resp.status = falcon.HTTP_200
        #resp.body = json.dumps(prediction[0])

# Class pour les prédictions batch
class PredictBatch:
    
    def on_post(self, req, resp):
        # On traite les arguments envoyé par le POST, et on traite correctement l'erreur si le JSON n'est pas correct
        # A ne pas changer
        try:
            body_raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, "Error", ex.message)
        try:
            body_json = json.loads(body_raw_json, encoding="utf-8")
        except ValueError:
            raise falcon.HTTPError(
                falcon.HTTP_400,
                "Malformed JSON",
                "Could not decode the request body. The " "JSON was incorrect.",
            )
        # On traite les erreurs bloquantes comme un paramètre manquant
        try:
            x = pd.DataFrame.from_dict(body_json)
        # except ValueError:
        except Exception as e:
            print(e)
            raise falcon.HTTPError(
                
                falcon.HTTP_400, "Missing Parameter", "Missing content parameter"
            )
            
        predictions = list(sk_model.predict(x))

        # On renvoie la prédiction
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(predictions)
