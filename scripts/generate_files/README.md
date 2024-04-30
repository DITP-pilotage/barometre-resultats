# Générer les fichiers

Génère les fichiers de données pour alimenter le baromètre.

## Usage

Voir le fichier d'exemple `main.py`. Pour l'exécuter:

```sh
pipenv run python3 main.py
```

## Installation environnement

Pour installer l'environnement, exécuter `pipenv lock && pipenv sync`.

*Erreur Installation `psycopg2`:* En cas de problème pour avec l'installation du module `psycopg2`, exécuter :

```sh
sudo apt install libpq-dev # Voir https://unix.stackexchange.com/a/583547
```
