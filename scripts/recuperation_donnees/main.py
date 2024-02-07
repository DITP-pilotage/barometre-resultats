import utils

if __name__ =="__main__":
    
    # On tente de retrouver l'url du CSV associé à cet indicateur
    indic = 'IND-555'
    url_fichier_indic_555 = utils.get_dataset_indic(indic)
    print("L'url du fichier associé à", indic, "est", url_fichier_indic_555)

    # Liste de tous les fichiers et indic_id correspondant
    tous_fichiers = utils.get_all_dataset_with_indicId()
    for i in range(3):
        print("Le fichier de l'indicateur", tous_fichiers[i]['indic_id'], "se trouve ici: ", tous_fichiers[i]['download_url'])
