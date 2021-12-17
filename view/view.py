class TournamentView:
    def __str__(self):
        return self.name

    def __init__(self):
        self.name = "View"

    def verify_integer(self):
        integer_to_verify = None
        status = False
        while not status:
            try:
                integer_to_verify = int(input())
                if integer_to_verify < 0:
                    print('Cette entrée doit être un entier positif')
                    status = False
                else:
                    status = True
            except (Exception,):
                print('Cette entrée doit être un entier positif')
        return integer_to_verify

    def verify_x_options(self, x):
        number_to_verify = None
        status = False
        while not status:
            try:
                number_to_verify = int(input())
                if 0 <= number_to_verify <= x - 1:
                    status = True
                else:
                    print('Cette entrée doit être un nombre entre 0 et ' + str(x - 1))
            except (Exception,):
                print('Cette entrée doit être un nombre entier')
        return int(number_to_verify)

    # Partie view

    def take_back_tournament(self):
        print('Reprendre le dernier tournoi?')
        print('Oui = 1, Non = 0')
        response = self.verify_x_options(2)
        return response

    def create_tournament(self):
        print('Création du tournoi')
        nom = input("Nom du tournoi: ")
        lieu = input("Lieu: ")
        date = input("Date: ")
        print("Nombre de tours: ")
        nombre_tours = self.verify_integer()
        print("Contrôle du temps: ")
        print("bullet=0, blitz=1, coup rapide=2")
        temps = self.verify_x_options(3)
        description = input("Description: ")
        # Créer un dictionnaire
        return nom, lieu, date, nombre_tours, temps, description

    def declare_a_player(self, player_nb):
        print(f"Déclaration du joueur numéro {player_nb}")
        nom_de_famille = input("Nom de famille: ")
        prenom = input("Prénom: ")
        date_de_naissance = input("Date de naissance: ")
        print("Sexe: ")
        print("homme = 0 et femme = 1")
        sexe = self.verify_x_options(2)
        if sexe == 0:
            sexe = 'Homme'
        else:
            sexe = 'Femme'
        return nom_de_famille, prenom, date_de_naissance, sexe

    def result_of_a_match(self, player1, player2):
        print(f"Qui est le gagnant du duel {player1} vs {player2}?")
        print(f"{player1} = 0, {player2} = 1, equality = 2")
        result = self.verify_x_options(3)
        return result

    def update_tournament(self):
        print("Voulez vous mettre à jour le classement des joueurs ?")
        print('Oui = 1, Non = 0')
        result = self.verify_x_options(2)
        if result == 0:
            return False
        else:
            return True

    def update_player(self, player, match):
        print(f"Le joueur {player} a {player.points} points ?")
        result = self.verify_integer()
        return result

    def menu(self):
        print("Menu principal")
