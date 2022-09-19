def pendu(mot):
    """
    Le jeu du pendu dans la console python
    Syntaxe:
        pendu("motSecret")
    """
    motSecret = mot.lower()
    win = 0
    longeurMot = len(motSecret)
    lettresTrouve = []
    chances = 10
    print("Le mot à trouver est long de ", longeurMot,  " lettres !")
    while win == 0:
        lettre = input("Veuillez rentrer une lettre !").lower()
        if lettre in motSecret and lettre not in lettresTrouve:
            print("Bien joué ! Plus que ", longeurMot-(len(lettresTrouve)+1), " lettres à trouver !")
            lettresTrouve.append(lettre)
            print("Vous avez trouvé ", lettresTrouve)

            if len(lettresTrouve) == longeurMot:
                win = 1

        elif lettre in lettresTrouve:
            print("Vous avez déjà dit cette lettre !")

        elif lettre not in motSecret:
            chances = chances - 1
            print("Eh non ! Mauvaise lettre, plus que ", chances, " chances !")

            if chances == 0:
                return "Perdu !"
    return "Gagné !"
