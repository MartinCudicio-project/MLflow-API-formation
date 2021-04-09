# ----------------------------------
# Makefile - Workshop MLOps
# ----------------------------------

.DEFAULT_GOAL := help

create-envs: ## crée env conda pour /train et /api
	conda env create --force -f ./train/environment.yml
	conda env create --force -f ./api/environment.yml

get-data: ## Télécharge et transforme les données
	python3 utils/get_data.py

all: ## Déroule create-envs et get-data
	$(MAKE) create-envs
	$(MAKE) get-data
