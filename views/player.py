from views.views import View
from controller.database import load_db


class CreatePlayer(View):

    def display_menu(self):

        name = input("""Nom du joueur:\n> """)

        first_name = input("""Prénom du joueur:\n> """)

        date_of_birth = self.get_user_entry(
            msg_display="Date de naissance (format DD/MM/YYYY):\n> ",
            msg_error="Veuillez entrer une date au format valide: DD/MM/YYYY",
            value_type="date"
        )

        gender = self.get_user_entry(
            msg_display="Sexe (H ou F):\n> ",
            msg_error="Veuillez entrer H ou F",
            value_type="selection",
            assertions=["H", "h", "F", "f"]
        ).upper()

        rank = self.get_user_entry(
            msg_display="Rang:\n> ",
            msg_error="Veuillez entrer une valeur numérique valide.",
            value_type="numeric"
        )

        print(f"Joueur {first_name} {name} créé.")

        return {
            "name": name,
            "first_name": first_name,
            "date_of_birth": date_of_birth,
            "gender": gender,
            "total_score": 0,
            "rank": rank,
        }


class LoadPlayer(View):

    def display_menu(self, nb_players_to_load):

        all_players = load_db("players")
        serialized_loaded_players = []
        unique_players = 0
        while unique_players < nb_players_to_load:
            print(f"Plus que {str(nb_players_to_load - unique_players)} joueurs à charger.")
            display_msg = "Choisir un joueur:\n"

            assertions = []
            for number_player, player in enumerate(all_players):
                display_msg = display_msg + f"{str(number_player+1)} - {player['first_name']} {player['name']}\n"
                assertions.append(str(number_player+1))

            user_input = int(self.get_user_entry(
                msg_display=display_msg,
                msg_error="Veuillez entrer un nombre entier.",
                value_type="selection",
                assertions=assertions
            ))
            if all_players[user_input-1] not in serialized_loaded_players:
                serialized_loaded_players.append(all_players[user_input-1])
                unique_players += 1
            else:
                print("Joueur déjà chargé. Merci de choisir un autre joueur.")

        return serialized_loaded_players
