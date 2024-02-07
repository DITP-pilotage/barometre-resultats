# Récupération de données

Permet de retrouver l'URL d'un jeu de données d'un indicateur à l'aide de son ID.

## Usage

```python
import utils
url_found = utils.get_indic_dataset("IND-555")
# -> https://raw.githubusercontent.com/DITP-pilotage/barometre-resultats/main/data/ind-555.csv
```