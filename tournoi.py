# tournoi.py

from joueur import Joueur
from match import Match
from utils import lire_csv
from utils import sauvegarder_json
from utils import ecrire_texte

class Tournoi:
    def __init__(self, nom):
        """
        Initialise un tournoi avec son nom.
        Initialise aussi une liste vide pour les joueurs et pour les matchs.
        """
        self.nom = nom
        self.joueurs = []
        self.matchs = []

    def charger_joueurs(self, chemin_csv):
        lignes = lire_csv(chemin_csv)
        for element in lignes:
            pseudo = element[0]
            joueur = Joueur(pseudo)
            self.joueurs.append(joueur)



    def charger_matchs(self, chemin_csv):
        lignes = lire_csv(chemin_csv)
        for element1, element2 in lignes:
            joueur1 = element1[0]
            joueur2 = element2[0]
            match = Match(joueur1, joueur2)


    def saisir_scores(self):
        """
        Pour chaque match dans la liste des matchs :
        - Afficher le match (afficher les pseudos des deux joueurs)
        - Demander à l'utilisateur d'entrer les deux scores (score du joueur 1, score du joueur 2)
        - Enregistrer les scores dans l'objet Match
        - Déterminer le gagnant du match
        - Si un gagnant existe (pas d'égalité), appeler enregistrer_victoire() sur le joueur gagnant.
        """
        for match in self.matchs:
            print(f"Match: {match.joueur1} vs {match.joueur2}")
            try:
                score1 = int(input(f"Entrez le score de {match.joueur1}: "))
                score2 = int(input(f"Entrez le score de {match.joueur2}: "))
                match.definir_scores(score1, score2)
                if score1 > score2:
                    gagnant = next((j for j in self.joueurs if j.pseudo == match.joueur1), None)
                    if gagnant:
                        gagnant.enregistrer_victoire()
                elif score2 > score1:
                    gagnant = next((j for j in self.joueurs if j.pseudo == match.joueur2), None)
                    if gagnant:
                        gagnant.enregistrer_victoire()
            except ValueError:
                print("Erreur : Veuillez entrer des scores valides.")

    def afficher_classement(self):
        """
        Afficher le classement des joueurs.
        Classer les joueurs du plus grand nombre de victoires au plus petit.
        Afficher leur pseudo et leur nombre de victoires.
        """
        self.joueurs.sort(key=lambda j: j.victoires, reverse=True)
        print("Classement des joueurs :")
        for joueur in self.joueurs:
            print(f"{joueur.pseudo} - Victoires : {joueur.victoires}")

    def sauvegarder(self, chemin_json):
        tournoi = {"nom": self.nom, "joueur": [Joueur.to_dict() for element in self.joueurs]}
        sauvegarder_json(tournoi, chemin_json)

    def generer_rapport(self, chemin_texte):
        """
        Générer un rapport du tournoi sous forme de fichier texte.
        Le rapport doit contenir :
        - Le nom du tournoi
        - La liste des matchs joués avec leurs scores
        - Le classement final
        Utiliser la fonction ecrire_texte() du fichier utils.py.
        """
        pass
