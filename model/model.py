
class Tournament:
    nom: str
    lieu:str
    date: str
    nombre_tours: int
    joueurs: str
    temps: str
    description: str
    tournees: int

    def __str__(self):
        return {self.nom}

    def __init__(self, nom, lieu, date, joueurs, temps, description, tournees, nombre_tours=4):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nombre_tours = nombre_tours
        self.joueurs = joueurs
        self.temps = temps
        self.description = description
        self.tournees = tournees


class Player:
    nom_de_famille: str
    prenom: str
    date_de_naissance: str
    sexe: int
    classement: int

    def __str__(self):
        return f'{self.prenom} {self.nom_de_famille}'

    def __init__(self, nom_de_famille, prenom, date_de_naissance, sexe, classement):
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement
