# Récupération de données

Permet de retrouver l'URL d'un jeu de données d'un indicateur à l'aide de son ID.

Pour rechercher un jeu de données sur une branche spécifique, modifier la valeur de la variable d'environnement `BRANCH_GITHUB_REPO`. Les valeurs autorisées pour les branches sont dans [constants.py](./constants.py) (`GITHUB_BRANCH_ALLOWED`).

## Usage

```python
import utils

utils.get_dataset_indic("IND-555")
# -> https://raw.githubusercontent.com/DITP-pilotage/barometre-resultats/main/data/ind-555.csv
utils.get_all_dataset_with_indicId()[0]
# -> {'indic_id': 'IND-218', 'download_url': 'https://raw.githubusercontent.com/DITP-pilotage/barometre-resultats/main/data/ind-218.csv', 'name': 'ind-218.csv', 'path': 'data/ind-218.csv'}
```