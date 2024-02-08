import utils
import os
from dotenv import load_dotenv


if __name__ =="__main__":
    
    load_dotenv()

    # Récupération des données du baro
    donnees_baro = utils.get_data("Base cible", os.environ.get('PG_URL'))
    # Export des données du baro dans un fichier séparé par indicateur
    OUT_DIR = "out/"
    utils.export_by_indic(donnees_baro, OUT_DIR)

    print('done')
