from view import TournamentView
from model import Tournament, Player
from tinydb import TinyDB, Query


class TournamentController:
    def start_tournament(self):
        db = TinyDB('db.json')
        tournament_table = db.table('tournament')
        if len(tournament_table.all()) >= 1:
            answer = TournamentView().take_back_tournament()
            if answer == 0:
                self.create_tournament()
            else:
                serialized_tournament = tournament_table.get(doc_id=len(tournament_table))
                players_table = db.table('players')
                serialized_table = players_table.all()
                players_list = []
                for player in range(0, len(serialized_table)):
                    player = Player(nom_de_famille=serialized_table[player]['nom_de_famille'],
                                    prenom=serialized_table[player]['prenom'],
                                    date_de_naissance=serialized_table[player]['date_de_naissance'],
                                    sexe=serialized_table[player]['sexe'],
                                    points=serialized_table[player]['points'],
                                    classement=serialized_table[player]['classement'])
                    players_list.append(player)
                nom = serialized_tournament['nom']
                lieu = serialized_tournament['lieu']
                date = serialized_tournament['date']
                nombre_tours = serialized_tournament['nombre_tours']
                temps = serialized_tournament['temps']
                description = serialized_tournament['description']
                tournament = Tournament(nom=nom, lieu=lieu, date=date, nombre_tours=nombre_tours, joueurs=players_list,
                                        temps=temps, description=description, tournees=[])
                if len(players_list) > 0:
                    self.define_matches(tournament)
                else:
                    self.define_players(tournament)
                    # verif players
        else:
            self.create_tournament()

    def create_tournament(self):
        """
        Lance la création d'un tournoi.
        """
        tournament_data = TournamentView().create_tournament()

        tournament = Tournament(nom=tournament_data[0], lieu=tournament_data[1], date=tournament_data[2],
                                nombre_tours=tournament_data[3], temps=tournament_data[4],
                                description=tournament_data[5],
                                tournees=[], joueurs=[])

        # partie serialisation
        serialized_tournament = {
            'nom': tournament.nom,
            'lieu': tournament.lieu,
            'date': tournament.date,
            'nombre_tours': tournament.nombre_tours,
            'temps': tournament.temps,
            'description': tournament.description
        }

        db = TinyDB('db.json')
        players_table = db.table('tournament')
        players_table.truncate()
        players_table.insert(serialized_tournament)

        self.define_players(tournament)

    def define_players(self, tournament):
        """
        Définit le nombre de joueurs du tournoi et leurs informations.
        """

        serialized_players = []

        for i in range(0, 8):
            player = TournamentView().declare_a_player(i + 1)
            player = Player(nom_de_famille=player[0], prenom=player[1], date_de_naissance=player[2],
                            sexe=player[3], points=0, classement=0)
            tournament.joueurs.append(player)

            # partie serialisation
            serialized_player = {
                'nom_de_famille': player.nom_de_famille,
                'prenom': player.prenom,
                'date_de_naissance': player.date_de_naissance,
                'sexe': player.sexe,
                'points': player.points,
                'classement': player.classement
            }
            serialized_players.append(serialized_player)

        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.truncate()
        players_table.insert_multiple(serialized_players)

        self.define_matches(tournament)

    def define_matches(self, tournament):
        """
        Lancement des tournois entre les joueurs
        """
        players = tournament.joueurs

        middle = int(len(players) / 2)

        pairs = []

        # re ordonner les joueurs par leur classement
        if len(tournament.tournees) != 0:
            tour_number = len(tournament.tournees)
            print(tour_number)
            players.sort(key=lambda x: x.points, reverse=True)

        print(players)

        first_half = players[:middle]
        second_half = players[middle:]

        for i in range(0, middle):
            pair = [first_half[i], second_half[i]]
            pairs.append(pair)

        matches = []
        serialized_matches = []
        for i in range(0, len(pairs)):
            result = TournamentView().result_of_a_match(pairs[i][0], pairs[i][1])
            if result == 0:
                match = ([pairs[i][0], 1], [pairs[i][1], 0])
                pairs[i][0].points += 1
            elif result == 1:
                match = ([pairs[i][0], 0], [pairs[i][1], 1])
                pairs[i][1].points += 1
            else:
                match = ([pairs[i][0], 0.5], [pairs[i][1], 0.5])
                pairs[i][0].points += 0.5
                pairs[i][1].points += 0.5
            matches.append(match)
            # partie serialisation
            serialized_match = {
                'joueur1': match[0][0].__dict__,
                'points1': match[0][1],
                'joueur2': match[1][0].__dict__,
                'points2': match[1][1],
                'tour': len(tournament.tournees) + 1
            }
            serialized_matches.append(serialized_match)

        db = TinyDB('db.json')
        matches_table = db.table('matches')
        if len(tournament.tournees) == 0:
            matches_table.truncate()
        matches_table.insert_multiple(serialized_matches)

        # ajout de la liste a l'attribut tournee
        tournament.tournees.append(matches)

        # changer le classement des joueurs ? mettre une option 0 / 1
        if len(tournament.tournees) < int(tournament.nombre_tours):
            self.update_classement(tournament)
        else:
            print("finish")

    def update_classement(self, tournament):
        result = TournamentView().update_tournament()
        if result:
            for i in range(len(tournament.joueurs)):
                player = tournament.joueurs[i]
                player.classement = TournamentView().update_player(player, match)
        self.define_matches(tournament)

    def __str__(self):
        return self.name

    def __init__(self):
        self.name = "Controller"
