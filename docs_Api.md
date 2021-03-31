# API

Nous allons voir ici comment APIser un modèle.

## Cas d'usage

![API](img/api.png)

Les modèles sous forme d'API sont donc bien pour les cas d'usages unitaires. Par exemple, c'est idéal quand nous voulons faire du temps réel ou en backend d'une application web.

Il faut néanmoins de méfier des cas d'usage BATCH. Par exemple une mise à jour mensuelle des prédiction pour 20M de produits.

## Récupération du template pour le TD

Pour ce TD, nous allons nous baser sur un template. Vous allez devoir créer votre propre repository sur Gitlab. (Faites le sur votre espace personnel pour ne pas pourrir le repo Saegus...).

Lors de la création, nous allons utiliser l'import permis par Gitlab, suivez l'image ci dessous (lien du projet à import : https://gitlab.com/saegus/data/formations/dataops-api-td.git):

![create project](img/create_project.png)

Le lien pour l'import

## Création des environnements virtuels

Souvenez-vous ce qu'on a vu dans les bases. Nouveau projet, nouvel environnement virtuel.
Dans notre cas, nous avons un seul projet pour l'entrainement et l'api. En règle générale, nous aurons 2 projets distincts, donc 2 environnements virtuels. En effet, les librairies dont nous avons besoin dans l'api sont plus restreintes que celles lors de la phase d'entrainement, qui peuvent comporter jupyter etc ...

Le 1er environnement virtuel se base sur le requirements.txt que l'on trouve dans le dossier *train*.

Le 2ème environnement virtuel se base sur le requirements.txt situé dans le dossier *api*

**Exercice**: Créer les 2 environnements virtuels avec Python 3.6

## Le format pickle

Le module pickle permet de sauvegarder dans un fichier, au format binaire, n'importe quel objet Python.
Il va donc nous servir, dans notre cas, à enregistrer notre modèle entraîné ainsi que le mapping des résultats pour permettre de récupérer un résultat fonctionnel (en l'occurence, le nom de l'iris plutôt que sa classe en integer)

Le fichier train.py permet d'entrainer le modèle.

**Exercice**: Lancer le fichier train.py. N'oubliez pas d'activer votre environnement virtuel.

## L'API

Plusieurs frameworks python existent dont:

- Flask
- Falcon
- Tornado
- Django

Pour des soucis de simplicité et performance, nous utilisons Falcon dans notre TD.

Regardez le dossier api et essayez de le comprendre.

Commande pour lancer le serveur web
```python
gunicorn -b 0.0.0.0:8000 main:api
```

Pour tester l'API, nous allons utiliser Postman.
![test api](img/test-api.png)

**Exercice**:

- Localisez l'import des fichiers pickles. Comprenez-vous pourquoi ?
- Adaptez le code pour en faire une API fonctionnelle
- Testez avec POSTMAN

