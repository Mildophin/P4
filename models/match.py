import random


class Match:
    """
    Classe Match
    """
    def __init__(self, name, players_pair):
        self.player1 = players_pair[0]
        self.score_player1 = 0
        self.color_player1 = ""
        self.player2 = players_pair[1]
        self.score_player2 = 0
        self.color_player2 = ""
        self.winner = ""
        self.name = name

    def __str__(self):
        return ([self.player1, self.score_player1],
                [self.player2, self.score_player2])

    def assign_colors(self):
        """
        Methode qui donne une couleur a chaque joueur d'un match
        """
        if random.choice([True, False]):
            self.color_player1 = "Blanc"
            self.color_player2 = "Noir"
        else:
            self.color_player1 = "Noir"
            self.color_player2 = "Blanc"

    def play_match(self, winner):
        """
        Methode qui permet de faire jouer les joueurs et assigner un score
        """
        if winner == "0":
            self.winner = self.player1.first_name
            self.score_player1 += 1
        elif winner == "1":
            self.winner = self.player2.first_name
            self.score_player2 += 1
        elif winner == "2":
            self.winner = "Égalité"
            self.score_player1 += 0.5
            self.score_player2 += 0.5

        # Mettre une exception
        else:
            raise Exception

        self.player1.tournament_score += self.score_player1
        self.player2.tournament_score += self.score_player2

    def get_serialized_match(self):
        """
        Methode qui permet de transformer les matchs sérialisés en instance
        """
        return {
            "player1": self.player1.get_serialized_player(save_tournament_score=True),
            "score_player1": self.score_player1,
            "color_player1": self.color_player1,
            "player2": self.player2.get_serialized_player(save_tournament_score=True),
            "score_player2": self.score_player2,
            "color_player2": self.color_player2,
            "winner": self.winner,
            "name": self.name
        }
