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

    def current_tour(self, tour):
        print(f"Tour N°{tour + 1}")

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

    def update_player(self, player):
        print(f"Le joueur {player} a {player.points} points ?")
        result = self.verify_integer()
        return result

    def menu_home(self):
        print("Menu principal")
        print("0: Commencer un nouveau tournoi, 1: Reprendre le dernier tournoi, 2: Voir les rapports")
        result = self.verify_x_options(3)
        return result

    def menu_report(self):
        print("Menu principal")
        print("0: Liste de tout les acteurs, 1: Liste de tout les joueurs d'un tournoi, 2: Liste de tous les tournois,"
              "3: Liste de tous les tours d'un tournoi, 4: Liste de tous les matchs d'un tournoi, 5: Retour menu")
        result = self.verify_x_options(6)
        return result

    def order_players(self):
        print("0: Ordonner par ordre alphabétique, 1: Ordonner par classemment")
        result = self.verify_x_options(2)
        return result

    def view_players(self, players_list):
        print("Rapport de tous les joueurs")
        for player in players_list:
            print(f"{player['prenom']} {player['nom_de_famille']}")
        print("Write 0 to leave the report")
        result = self.verify_x_options(1)
        return result

    def view_tournaments(self, tournaments_list):
        print("Rapport de tous les tournois")
        for tournament in tournaments_list:
            print(f"{tournament['nom']}")
        print("Write 0 to leave the report")
        result = self.verify_x_options(1)
        return result

    def pick_tournament(self, tournaments_list):
        print("Choisissez le tournoi")
        i = 0
        for tournament in tournaments_list:
            print(f"{i}: {tournament['nom']}")
            i = + 1
        result = self.verify_x_options(len(tournaments_list))
        return result
