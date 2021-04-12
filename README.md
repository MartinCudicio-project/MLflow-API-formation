# FINImmo, agence immobilière du futur 

FINImmo est une agence immobilière qui veut utiliser un modèle de prédiction afin de déterminer le prix de vente d'appartements à Saint-Martin. 
En mettant en place un modèle de prédiction de prix de vente, l'agence aimerait avoir une estimation de la valeur des logements basée sur une intelligence artificielle. Cela permettrait à l'agence de proposer aux futurs acheteurs/vendeurs une première estimation instantannée de leur bien sur leur site internet. 

## À disposition

1) beaucoup de courage, puisqu'il n'est jamais facile d'extraire de la valeur de ses données. Cela est vrai pour la visualisation, mais encore plus si on veut utiliser la puissance du Machine Learning. 

2) par chance FINImmo a gardé un registre de ses ventes dans un tableur excel.
En exportant ce tableur, nous obtenons un .csv exploitable

3) des ML Ingenieurs leur proposant d'opérationnaliser des modèles de prédiction, inspirés d'une philosophie MLOps (dans le meilleur des mondes)


# API
 
Nous allons voir ici comment APIser un modèle.

## Cas d'usage

![API](img/api.png)

Les modèles sous forme d'API sont donc bien pour les cas d'usages unitaires. Par exemple, c'est idéal quand nous voulons faire du temps réel ou en backend d'une application web.

Il faut néanmoins de méfier des cas d'usage BATCH. Par exemple une mise à jour mensuelle des prédiction pour 20M de produits.

## Récupération du template pour le TD

Pour ce TD, nous allons nous baser sur un template. Vous allez devoir créer votre propre repository sur Gitlab. (Faites le sur votre espace personnel...).

Lors de la création, nous allons utiliser l'import permis par Gitlab, suivez l'image ci dessous (lien du projet à import : mettre le bon lien):

![create project](img/create_project.png)


## Partie 1 - Création/utilisation des environnements virtuels

Nouveau projet, nouvel environnement virtuel.
Dans notre cas, nous avons un seul projet pour l'entrainement et l'api. 
En règle générale, nous aurons 2 projets distincts, donc 2 environnements virtuels. En effet, les librairies dont nous avons besoin dans l'api sont plus restreintes que celles lors de la phase d'entrainement, qui peuvent comporter jupyter etc ...

Le 1er environnement virtuel se base sur le environment.yml que l'on trouve dans le dossier *train*.

Le 2ème environnement virtuel se base sur le environment.yml situé dans le dossier *api*

**Exercice**: Créer les 2 environnements virtuels

- utiliser la commande (compilateur GNU nécessaire pour lancer des commandes make)

`make create-envs`

## Partie 2 - Entrainement du modèle

Accéder au notebook situé à /train/home_data_Model.ipynb avec votre IDE préféré (JupyterLab, VScode, ...)
S'assurer d'utiliser comme kernel l'environement _env_train_ crée précédement

### 2.1 - 1er modèle : Régression Linéaire

Visualiser le premier modèle créé et comprendre le fonctionnement de MLflow et la commande MLflow UI.

Toutes les informations concernant vos runs seront enregistrées localement sur votre machine dans le dossier mlruns, situé dans le répertoire _/train_.
Pour votre information, d'autres méthodes de stockage sont possibles. Cf doc officiel - https://mlflow.org/docs/latest/tracking.html#how-runs-and-artifacts-are-recorded

Après avoir fit votre modèle, et log les résultats dans mlflow, observer les résultats avec l'User Interface de MLflow.
Pour cela, vous devez exécuter la commande ' mlflow ui ' depuis le répertoire train.


### 2.2 - 2e modèle : Random Forest

Après avoir compris la Partie 2.1, vous devez utiliser Mlflow afin de save le modèle avec ses performances.
Repérer les infos disponibles du modèle (param,metrics,artifacts)

Ajoute donc le code manquant ! 

Apres avoir ajouté le code manquant, run la cellule et visualise ensuite avec mlflow ui

PS : On a laissé quelques indices



## Partie 3 - L'API

Plusieurs frameworks python existent dont:

- Flask
- Falcon
- Tornado
- Django

Pour des soucis de simplicité et performance, nous utilisons Falcon dans notre TD.

Regardez le dossier api et essayez de le comprendre.

Après t'être placé dans le dossier api, exécute la commande pour lancer le serveur web en utilisant l'environement env_api
```python
waitress-serve --port=8000 main:api
```

Pour tester l'API, nous allons utiliser Postman.
![test api](img/test-api.png)

MLflow va donc nous servir à pouvoir visualiser les différents modèles entraînés et à pouvoir le charger dans notre API. 

**Exercice**:

- Localisez l'import du modèle. Comprenez-vous pourquoi ?
- Adaptez le code pour en faire une API fonctionnelle en ajoutant le meilleur modèle
- Testez avec POSTMAN

## Partie 4 - Simulation des prédictions

Maintenant que votre API est fonctionnele avec une bonne version du modèle, nous allons simuler les prédictions. 

À la fin de chaque mois, nous connaissons le prix réel de vente des appartements. Nous allons donc pouvoir suivre la performance de notre modèle en fonction des mois.

### 4.1 - affichage des performance du meilleur modèle entrainé (RandomForest)

vous trouverez dans le dossier /test un notebook de test qui comprend les fonctions de calcul de performances et d'affichage sous forme graphique. 

**Exercice**:

- Requete l'API, pour obtenir les prédictions du mois XXX à XXX
- Récuperer les réelles prix, calculer les performances, et les afficher

On observe que notre modèle, baisse de performance à partir du mois de XXX

### 4.2 - réentrainement du modèle

Nous observons un drift du modèle. Afin de garantir aux clients un prix de vente optimal, FINImmo veut que son modèle soit le plus peformant possible. 

Nous disposons donc de nouvelles données (données déja existantes pour le training initial + données jusqu'au mois de baisse de prédiction) 

Suite à la baisse de précision à partir du mois de XXX, tu dois alors recréer/réentrainer le modèle RandomForest avec les nouvelles données. 

**Exercice**: 

- à partir du notebook dans /train, réentrainer une RandomForest avec les nouvelles données
- save le model avec mlflow
- observer avec mlflow ui

### 4.3 - utilisation du nouveau modèle

Maintenant que nous avons créer un nouveau modèle, ca serait bien de l'utiliser ! 

**Exercice**: 

- charger le nouveau modèle dans l'API
- à partir du notebook dans /test, faire de nouveaux des prédictions sur le mois de XXX à XXX
- calculer les performances, et les afficher




