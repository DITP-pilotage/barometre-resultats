import utils

if __name__ =="__main__":
    
    # On tente de retrouver l'url du CSV associé à cet indicateur
    indic = 'IND-555'
    res= utils.get_indic_dataset(indic)
    print("Le fichier associé à", indic, "est", res)

