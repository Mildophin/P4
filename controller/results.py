from views.views import View


def result_match(match):

    # Match joué, on rentre les scores
    winner = View().get_user_entry(
        msg_display=f"{match.player1.first_name} ({match.color_player1}) VS " +
                    f"{match.player2.first_name} ({match.color_player2})\n"
                    f"Gagnant ?\n"
                    f"0 - {match.player1.first_name} ({match.color_player1})\n"
                    f"1 - {match.player2.first_name} ({match.color_player2})\n"
                    f"2 - Égalité\n> ",
        msg_error="Veuillez entrer 0, 1 ou 2.",
        value_type="selection",
        assertions=["0", "1", "2"]
    )

    return winner
