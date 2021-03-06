from controller.database import save_db, update_player_rank
from models.player import Player
from views.player import CreatePlayer


def create_player():
    """
    Methode qui permet la création d'un instance de joueur
    """
    # Récupération des infos du joueur
    user_entries = CreatePlayer().display_menu()

    # Création du joueur
    player = Player(
        user_entries['name'],
        user_entries['first_name'],
        user_entries['date_of_birth'],
        user_entries['gender'],
        user_entries['total_score'],
        user_entries['rank'])

    # serialization:
    serialized_player = player.get_serialized_player()

    # Sauvegarde du joueur dans la database
    save_db("players", serialized_player)

    return player


def update_rankings(player, rank, score=True):
    """
    Methode qui permet la mise a jour du classement d'un joueur
    """
    if score:
        player.total_score += player.tournament_score
    player.rank = rank
    serialized_player = player.get_serialized_player(save_tournament_score=True)
    print(serialized_player['name'])
    update_player_rank("players", serialized_player)
    print(f"Mise à jour du rang de {player}:\nScore total: {player.total_score}\nRang: {player.rank}")
