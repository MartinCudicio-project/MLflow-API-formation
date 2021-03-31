import json

import falcon

# Chargement de fonctions spécifique d'un fichier (pour la clarté du code)
# from resources.dossierprojet.fonctions import fonction
from ressources.price_prediction import sk_model

class Predict:
    
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
            # content=body_json["content"]
            bedrooms=body_json["bedrooms"]
            bathrooms=body_json["bathrooms"]
            sqft_living=body_json["sqft_living"]
            floors=body_json["floors"]
            grade=body_json["grade"]
            yr_built=body_json["yr_built"]

        # except ValueError:
        except Exception:
            raise falcon.HTTPError(
                falcon.HTTP_400, "Missing Parameter", "Missing content parameter"
            )

        # On réalise notre predict issu du modèle chargé dans le __init__.py
        # Ex: prediction=model.predict(content)
        prediction = sk_model.predict([(bedrooms,bathrooms,sqft_living,floors,grade,yr_built)])
        print(prediction)
        # On renvoie la prédiction
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(
            {"content": prediction[0], "prediction": "Ceci est la prédiction"}
        )
