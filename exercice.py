# POO EXERCICE DE MISE EN SITUATION 1
# genre
# False : Femme
# True : Homme

class Personne :
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom  # crée une variable d'instance nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def Se_presenter(self):
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans.")

        genre_str = "Masculin" if self.genre else "Feminin"
        print("Genre : " + genre_str)

        e_optionnel = "" if self.genre else "e"

        if (self.Estmajeur()):
            print("Je suis majeur" + e_optionnel)
        else:
            print("Je suis mineur" + e_optionnel)

        print()

    def Estmajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25, True)
personne1.Se_presenter()

personne2 = Personne("Emilie", 17, False)
personne2.Se_presenter()