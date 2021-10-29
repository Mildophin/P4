
class TournamentView:
    def __str__(self):
        return self.name

    def __init__(self):
        self.name = "View"

    def verify_2_options(self):
        while True:
            data = input()
            if data == "0" or data == "1":
                break
            else:
                print('Cette entrée doit être soit 0 ou 1')
                continue
        return data

    def verify_3_options(self):
        while True:
            data = input()
            if data == "0" or data == "1" or data == "2":
                break
            else:
                print('Cette entrée doit être soit 0, 1 ou 2')
                continue
        return data

    def verify_integer(self):
        while True:
            data = input()
            try:
                int(data)
            except ValueError:
                print("Cette entrée doit être un chiffre positif(1,2,3,4, etc...)")
                continue
            if data == "0":
                print("Cette entrée doit être un chiffre positif(1,2,3,4, etc...)")
                continue
            else:
                break
        return data

    # Partie view
    def create_tournament(self):
        print('Création du tournoi')
        nom = input("Nom du tournoi: ")
        lieu = input("Lieu: ")
        date = input("Date: ")
        print("Nombre de tours: ")
        nombre_tours = self.verify_integer()
        print("Contrôle du temps: ")
        print("bullet=0, blitz=1, coup rapide=2")
        temps = self.verify_3_options()
        description = input("Description: ")
        return nom, lieu, date, nombre_tours, temps, description

    def declare_a_player(self, player_nb):
        print(f"Déclaration du joueur numéro {player_nb}")
        nom_de_famille = input("Nom de famille: ")
        prenom = input("Prénom: ")
        date_de_naissance = input("Date de naissance: ")
        print("Sexe: ")
        print("homme = 0 et femme = 1")
        sexe = self.verify_2_options()
        return nom_de_famille, prenom, date_de_naissance, sexe

    def result_of_a_match(self, player1, player2):
        print(f"Qui est le gagnant du duel {player1} vs {player2}?")
        print(f"{player1} = 0, {player2} = 1, equality = 2")
        result = self.verify_3_options()
        return result
