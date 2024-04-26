import utils
import os
from dotenv import load_dotenv


if __name__ =="__main__":
    
    load_dotenv()

    db_url = os.environ.get('PG_URL_qualif_227')

    # 1- Données quanti des indicateurs
    donnees_baro = utils.get_data("Base cible", db_url)
    utils.wipe_dir('../../data/')
    ##  Export des données dans un fichier séparé par indicateur
    utils.export_by_indic(donnees_baro, "../../data/")

    # 2- Données quali

    utils.wipe_dir('../../metadata/')
    # 2.1- Metadonnées indicateurs
    baro_meta_indicateurs = utils.get_metadata("Base cible", db_url)
    baro_meta_indicateurs.to_csv("../../metadata/meta_indicateurs.csv", index=False)

    # 2.2- Metadonnées chantiers
    baro_meta_chantiers = utils.get_metadata_ch("Base cible", db_url)
    baro_meta_chantiers.to_csv("../../metadata/meta_chantiers.csv", index=False)

    # 2.3- Metadonnées chantiers
    baro_meta_engagement = utils.get_metadata_engagement("Base cible", db_url)
    baro_meta_engagement.to_csv("../../metadata/meta_engagement.csv", index=False)

    print('done')
