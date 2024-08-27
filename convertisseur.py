# Projet "Convertisseur d'unités"
# qui sera capable de convertir des pouces(inch) en centimètre(cm), et vice-versa
# 1 pouce = 2.54 cm
# 1 cm = 0.394 pouces

# Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
# Demander à l'utilisateur de rentrer la valeur à convertir (en reprécisant l'unité)
# Afficher la valeur convertie (et l'unité : cm ou pouces)
# fin de programme


"""
convertisseur : Cette fonction convertit les unités unit1 vers unit2
Return :
    True: L'utilisateur ne veut plus convertir
    False: L'utilisateur a donné une valeur à convertir
"""
def convertisseur(unit1: str, unit2: str, facteur: float):
    valeur_str = input(f"Conversion {unit1} -> {unit2}. Donnez la valeur en {unit1} ou 'q' pour quitter : ")
    if valeur_str == "q":
        return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("ERROR: Vous devez rentrer une valeur numérique\n Veuillez utiliser le point et non la virgule pour les décimales")
        return convertisseur(unit1, unit2, facteur)

    valeur_convertie = round(valeur_float * facteur, 2)
    print(f"Résultat de la conversion: {valeur_str} {unit1} = {valeur_convertie} {unit2}")
    return False

print("Ce programme vous permet d'effectuer des conversations d'unités")
print("1 - Pouces vers cm")
print("2 - cm vers pouces")
user_choice = input("Votre choix (1 ou 2) : ")

# Si l'utilisateur veut sortir du programme
while True:
    if user_choice == "1":
        if convertisseur("pouces", "cm", 2.54):
            print("fin de programme")
            break
    if user_choice == "2":
        if convertisseur("cm", "pouces", 0.394):
            print("fin de programme")
            break