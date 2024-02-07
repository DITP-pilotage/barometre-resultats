import requests
import re

from constants import BASE_URL_API


def get_indic_dataset(indic_id):
    """Permet d'obtenir l'url d'un fichier CSV à partir d'un numéro d'indicateur

    Args:
        indic_id (string): ID de l'indicateur

    Raises:
        RuntimeError: Si aucun CSV correspondant n'est trouvé pour cet indicateur
        RuntimeError: Si plus d'un CSV correspondant n'est trouvé pour cet indicateur

    Returns:
        string: URL du CSV correspondant à cet indicateur
    """

    # Try to match with following resource field
    SEARCH_IN_FIELD = 'name'
    # Try to match resource field using following function
    SEARCH_METHOD = lambda x : x.lower()

    # Github API response
    resources=[{"name":x['name'], "path":x['path'], "download_url":x['download_url'] } for x in requests.get(BASE_URL_API).json()]
    # matching datagouv resources
    matching_resources = list(filter(lambda x: bool(re.search(SEARCH_METHOD(indic_id), SEARCH_METHOD(x[SEARCH_IN_FIELD]))), resources))
    
    # Raise error if 0 or multiple resource match requested indic_id
    if (len(matching_resources)>1): raise RuntimeError('Multiple matching resources for', indic_id)
    if (len(matching_resources)<1): raise RuntimeError('No matching resources for', indic_id)
    
    # Return url to download the file
    return matching_resources[0]['download_url']
