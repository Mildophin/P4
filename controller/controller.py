from view import TournamentView
from model import Tournament, Player
import tinydb


class TournamentController:
    def create_tournament(self):
        """
        Lance la création d'un tournoi.
        """
        tournament_data = TournamentView().create_tournament()

        tournament = Tournament(nom=tournament_data[0], lieu=tournament_data[1], date=tournament_data[2],
                                nombre_tours=tournament_data[3], temps=tournament_data[4],
                                description=tournament_data[5],
                                tournees=[], joueurs=[])

        self.define_players(tournament)

    def define_players(self, tournament):
        """
        Définit le nombre de joueurs du tournoi et leurs informations.
        """
        max_players = 8
        for i in range(0, max_players):
            player = TournamentView().declare_a_player(i + 1)
            player = Player(nom_de_famille=player[0], prenom=player[1], date_de_naissance=player[2],
                            sexe=player[3], classement=0)
            tournament.joueurs.append(player)

        self.define_matches(tournament)

    def define_matches(self, tournament):
        """
        Lancement des tournois entre les joueurs
        """
        players = tournament.joueurs

        middle = int(len(players)/2)

        # re ordonner les joueurs par leur classement
        if len(tournament.tournees) != 0:
            pass

        pairs = []

        first_half = players[:middle]
        second_half = players[middle:]

        for i in range(0, middle):
            pair = [first_half[i], second_half[i]]
            pairs.append(pair)

        # si une pair est déjà existante au dernier tour, changer les pairs

        for i in range(0, len(pairs)):
            result = TournamentView().result_of_a_match(pairs[i][0], pairs[i][1])
            if result == 0:
                pass
            elif result == 1:
                pass
            else:
                pass

        """
        match_exemple = (['joueur1', 'joueurs2'], ['1','0'])
        """

        # changer le classement des joueurs ? mettre une option 0 / 1

        # ajouter instance du tournoi à la tournee -> créer attribut tour actuel

        if len(tournament.tournees) < int(tournament.nombre_tours):
            self.define_matches(tournament)
        else:
            self.show_result(tournament)

    def show_result(self, tournament):
        pass

    def __str__(self):
        return self.name

    def __init__(self):
        self.name = "Controller"
