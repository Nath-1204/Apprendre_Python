# POO EXERCICE DE MISE EN SITUATION 1

class Personne :
    def __init__(self, nom: str, age: int):
        self.nom = nom  # crée une variable d'instance nom
        self.age = age
        print("Constructeur personne " + self.nom)

    def Se_presenter(self):
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans.")

        if (self.Estmajeur()):
            print("Je suis majeur")
        else:
            print("Je suis mineur")
        print()

    def Estmajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25)
personne2 = Personne("Emilie", 17)

personne1.Se_presenter()
personne2.Se_presenter()