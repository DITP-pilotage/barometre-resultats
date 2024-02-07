import requests
import re
import os
import urllib
from dotenv import load_dotenv

from constants import BASE_URL_API, GITHUB_BRANCH_DEFAULT, GITHUB_BRANCH_ALLOWED

load_dotenv()


branch = os.environ.get('BRANCH_GITHUB_REPO') if (os.environ.get('BRANCH_GITHUB_REPO') in GITHUB_BRANCH_ALLOWED) else GITHUB_BRANCH_DEFAULT
print('Selected branch is:', branch)


def get_all_dataset_with_indicId():
    """Retourne la liste de tous les fichiers du dossier data et l'indic_id correspondant

    Returns:
        list: Liste de dict {name, path, download_url, indic_id} pour chaque fichier du dossier
    """
    return [{
        "indic_id": _get_indicId_from_string(x['name']),
        "download_url":x['download_url'], 
        "name":x['name'], 
        "path":x['path'], 
    } for x in requests.get(BASE_URL_API + "?ref="+branch).json()]


def get_dataset_indic(indic_id):
    """Permet d'obtenir l'url d'un fichier CSV à partir d'un numéro d'indicateur

    Args:
        indic_id (string): ID de l'indicateur

    Raises:
        RuntimeError: Si aucun CSV correspondant n'est trouvé pour cet indicateur
        RuntimeError: Si plus d'un CSV correspondant est trouvé pour cet indicateur

    Returns:
        string: URL du CSV correspondant à cet indicateur
    """

    # matching files
    matching_resources = list(filter(lambda x: indic_id==x['indic_id'], get_all_dataset_with_indicId()))
    
    # Raise error if 0 or multiple resource match requested indic_id
    if (len(matching_resources)>1): raise RuntimeError('Multiple matching resources for', indic_id)
    if (len(matching_resources)<1): raise RuntimeError('No matching resources for', indic_id)
    
    # Return url to download the file
    return matching_resources[0]['download_url']

def _get_indicId_from_string(str_):
    """Try to find indic_id in a string

    Args:
        str_ (string): String to inspect

    Raises:
        RuntimeError: Multiple indic_id found in str
        RuntimeError: No indic_id found in str

    Returns:
        string: Guessed indic_id
    """
    PATTERN="IND-\d\d\d"
    pre_transform = lambda x : x.upper()

    matching = re.findall(PATTERN, pre_transform(str_))

    # Raise error if 0 or multiple PATTERN are found in str_
    if (len(matching)>1): raise RuntimeError('Multiple pattern >'+PATTERN+'< found in >'+ str_+'<')
    if (len(matching)<1): raise RuntimeError('No pattern >'+PATTERN+'< found in >'+ str_+'<')

    return matching[0]
