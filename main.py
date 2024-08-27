###
# PREMIERE PAS EN POO (PROGRAMMATION ORIENTE OBJET)
###

# Classe Parent
class EtreVivant:
    ESPECE_ETRE_VIVANT = "(Etre vivant non identifié)"

    def AfficherInfoEspeceEtreVivant(self):
        print("Info être vivant : " + self.ESPECE_ETRE_VIVANT)

class Chat(EtreVivant):
    ESPECE_ETRE_VIVANT = "Chat (Mammifère félin)"


# ---- DEFINITION ----
class Personne(EtreVivant):
    ESPECE_ETRE_VIVANT = "Humain (Mammifère Homo sapiens)"   # variable de classe (i pour toutes les Personnes)

    def __init__(self, nom: str = "", age: int = 0):    # self = objet (this)
        self.nom = nom  # Crée une variable d'instance : nom
        self.age = age
        if nom == "":
            self.DemanderNom()
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        info_personne = "Bonjour, permettez-moi de se présenter, je m'appelle " + self.nom
        if(self.age != 0):
            info_personne += ". J'ai " + str(self.age) + " ans."
            print(info_personne)
            if (self.EstMajeur() == True):
                print("Je suis majeur")
            else:
                print("Je suis mineur")
        else:
            print(info_personne)


    def AutreFonction(self):
        print("Nom : " + self.nom + " / Age : " + str(self.age))

    def EstMajeur(self):
        if(self.age >= 18):
            return True
        else:
            return False

    def DemanderNom(self):
        self.nom = input("Nom de la personne : ")


class Etudiant(Personne):
    def __init__(self, nom: str, age: int, etudes: str):    # self = objet (this)
        super().__init__(nom, age)
        self.etudes = etudes

    def SePresenter(self):  # Surchargé ma méthode SePresenter
        super().SePresenter() # Recupérer tous les caractéristiques de classe Personne
        print("je suis étudiant en " + self.etudes)

"""

#Personne.SePresenter(personne1)
personne1.SePresenter()
personne2.SePresenter()  # Method instance

#Personne.AutreFonction()  # Method de classe without 'self' in def
personne1.AutreFonction()
personne2.AutreFonction()

"""


#tupple

liste_personnes = [Personne("Jean", 30),  Personne("Paul", 15), Personne("Zoé", 33)]

#Personne.ESPECE_ETRE_VIVANT = "Mutant"
liste_personnes[0].ESPECE_ETRE_VIVANT = "Mutant"

for personne in liste_personnes:
    personne.SePresenter()
    personne.AfficherInfoEspeceEtreVivant()
    print()


chat = Chat()
chat.AfficherInfoEspeceEtreVivant()

etreVivant = EtreVivant()
etreVivant.AfficherInfoEspeceEtreVivant()

etudiant =Etudiant("Marc", 22, "Ecole d'ingénieur informatique")
etudiant.SePresenter()
