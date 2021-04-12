import falcon

from ressources.price_prediction.api import PredictBatch as PredictBatch
from ressources.price_prediction.api import PredictStream as PredictStream

api = falcon.API()

# Déclaration de la route qui sera utilisé lors de l'appel du web service
api.add_route("/batch",PredictBatch())
api.add_route("/stream", PredictStream())