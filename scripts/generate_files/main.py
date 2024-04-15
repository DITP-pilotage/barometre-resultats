import utils
import os
from dotenv import load_dotenv


if __name__ =="__main__":
    
    load_dotenv()

    # Récupération des données du baro
    donnees_baro = utils.get_data("Base cible", os.environ.get('PG_URL'))
    metadata_baro = utils.get_metadata("Base cible", os.environ.get('PG_URL'))
    #donnees_baro_dev = utils.get_data("Base de dev", os.environ.get('PG_URL_DEV'))
    # Export des données du baro dans un fichier séparé par indicateur
    utils.wipe_dir('../../data/')
    utils.export_by_indic(donnees_baro, "../../data/")
    utils.wipe_dir('../../metadata/')
    metadata_baro.to_csv("../../metadata/meta_indicateurs.csv", index=False)
    #utils.export_by_indic(donnees_baro_dev, "out_dev/")

    print('done')
