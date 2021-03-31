import falcon

from ressources.price_prediction.api import Predict as Predict

api = falcon.API()

# Déclaration de la route qui sera utilisé lors de l'appel du web service
# exemple : http://serveur:port/modele/predict
api.add_route("/predict", Predict())
