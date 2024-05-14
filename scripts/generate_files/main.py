import utils
import os
from dotenv import load_dotenv
import utils_git


if __name__ =="__main__":
    
    load_dotenv()

    # 1- Données quanti des indicateurs
    donnees_baro = utils.get_data("Base cible", os.environ.get('PG_URL'))
    utils.wipe_dir('../../data/')
    ##  Export des données dans un fichier séparé par indicateur
    utils.export_by_indic(donnees_baro, "../../data/")

    # 2- Données quali des indicateurs
    metadata_baro = utils.get_metadata("Base cible", os.environ.get('PG_URL'))
    utils.wipe_dir('../../metadata/')
    ##  Export des données dans metadata/meta_indicateurs.csv
    metadata_baro.to_csv("../../metadata/meta_indicateurs.csv", index=False)

    # Si GIT_DO_PUSH=true, on exécute les commandes git
    if bool(os.environ.get('GIT_DO_PUSH')):
        utils_git.git_add_commit_push()
    else:
        print("Skipping git push: GIT_DO_PUSH="+os.environ.get('GIT_DO_PUSH'))
    
    print('done')
