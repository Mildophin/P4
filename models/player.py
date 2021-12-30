

class Player:
    def __init__(self, name, first_name, date_of_birth, sex, total_score, rank=0):
        self.name = name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.total_score = total_score
        self.tournament_score = 0
        self.rank = rank
        self.played_with = []

    def __str__(self):
        return f"{self.first_name} {self.name} [{self.tournament_score} pts]"

    def get_serialized_player(self, save_tournament_score=False):
        serialized_player = {
            "name": self.name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "sex": self.sex,
            "total_score": self.total_score,
            "rank": self.rank,
        }
        if save_tournament_score:
            serialized_player["tournament_score"] = self.tournament_score

        return serialized_player