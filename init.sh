# ----------------------------------
# bash file d'initialisation
# ----------------------------------

# créer nos env conda avec les environement file dans /train et /api

conda env create -f ./train/environment.yml
# conda env create -f ./api/environment.yml

# activer notre environement de training, 
# run init.py pour 
# initialiser le télechargement transformation et sauvegarde du dataset : home_data.csv
# 

conda activate env_modeling

python3 init.py
