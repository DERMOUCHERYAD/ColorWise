# model.py
class Partie1Model:

     # Matrices d'adjacence et coloriages des graphes
    GRAPHE1 = {
    "adjacency": [
        [False, True, False, False, True],  # Sommet 0 connecté à 1 et 4
        [True, False, True, False, False],  # Sommet 1 connecté à 0 et 2
        [False, True, False, True, False],  # Sommet 2 connecté à 1 et 3
        [False, False, True, False, True],  # Sommet 3 connecté à 2 et 4
        [True, False, False, True, False]   # Sommet 4 connecté à 0 et 3
    ],
    "coloring": [1, 1, 2, 0, 2]  # 0=Bleu, 1=Rouge, 2=Vert
}


    GRAPHE2 = {

     "adjacency": [
        [False, True, False, False, True],  # Sommet 0 connecté à 1 et 4
        [True, False, True, False, False],  # Sommet 1 connecté à 0 et 2
        [False, True, False, True, False],  # Sommet 2 connecté à 1 et 3
        [False, False, True, False, True],  # Sommet 3 connecté à 2 et 4
        [True, False, False, True, False]   # Sommet 4 connecté à 0 et 3
    ],
    "coloring": [0, 1, 2, 1, 2]  # 0=Bleu, 1=Rouge, 2=Vert   
        
    
}
    # Matrices d'adjacence et coloriages pour le graphe de Petersen
    GRAPHE_PETERSEN = {
        "adjacency": [
            [False, True, True, False, True, False, False, False, False, False],
            [True, False, True, True, False, True, False, False, False, False],
            [True, True, False, False, False, False, True, False, False, False],
            [False, True, False, False, True, False, False, True, False, False],
            [True, False, False, True, False, False, False, False, True, False],
            [False, True, False, False, False, False, True, True, False, False],
            [False, False, True, False, False, True, False, False, True, True],
            [False, False, False, True, False, True, False, False, True, False],
            [False, False, False, False, True, False, True, True, False, True],
            [False, False, False, False, False, False, True, False, True, False],
        ]
    }
    
    @staticmethod
    def est_col(gphe, etiq):
        n = len(gphe)
        if len(etiq) < n:
            return False
        for i in range(n):
            for j in range(n):
                if gphe[i][j] and etiq[i] == etiq[j]:
                    return False
        return True

    @staticmethod
    def nombre_chromatique_petersen():
        return 3, [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]

    @staticmethod
    def est_2_coloriable(g):
        n = len(g)
        couleurs = [-1] * n

        def dfs(u, c):
            couleurs[u] = c
            for v in range(n):
                if g[u][v]:
                    if couleurs[v] == c:
                        return False
                    if couleurs[v] == -1 and not dfs(v, 1 - c):
                        return False
            return True

        for i in range(n):
            if couleurs[i] == -1 and not dfs(i, 0):
                return False
        return True
    
    @staticmethod
    def colorier_graphe_petersen():
        """
        Retourne un coloriage valide pour le graphe de Petersen.
        """
        return [1, 2, 3, 1, 2, 3, 2, 2, 3, 1]  # Exemple de coloriage (1=Rouge, 2=Vert, 3=Bleu)

# models.py
class Partie2Model:
    @staticmethod
    def deux_col(graphe):
        """
        Vérifie si un graphe est 2-coloriable.
        Si oui, retourne le coloriage (0, 1).
        Si non, retourne None.
        """
        n = len(graphe)
        couleurs = [-1] * n

        def dfs(u, c):
            couleurs[u] = c
            for v in range(n):
                if graphe[u][v]:
                    if couleurs[v] == c:  # Conflit détecté
                        return False
                    if couleurs[v] == -1 and not dfs(v, 1 - c):  # Colorier avec l'autre couleur
                        return False
            return True

        for i in range(n):
            if couleurs[i] == -1:  # Si un sommet n'est pas encore colorié
                if not dfs(i, 0):
                    return False, None  # Pas 2-coloriable
        return True, couleurs  # 2-coloriable et étiquetage

class Partie3Model:
    @staticmethod
    def glouton_coloriage(adjacency_matrix, order):
        """
        Applique l'algorithme glouton pour colorier le graphe selon l'ordre donné.
        """
        n = len(adjacency_matrix)
        colors = [-1] * n  # Toutes les couleurs sont initialement non assignées (-1)
        for node in order:
                # Trouver les couleurs des voisins
                neighbor_colors = set(
                    colors[neighbor]
                    for neighbor in range(n)
                    if adjacency_matrix[node][neighbor] and colors[neighbor] != -1
                )

                # Assigner la plus petite couleur disponible
                for color in range(n):
                    if color not in neighbor_colors:
                        colors[node] = color
                        break

        return colors
    
    @staticmethod
    def nombre_de_couleurs(colors):
        """
        Retourne le nombre de couleurs utilisées dans le coloriage.
        """
        return len(set(colors))
    
    @staticmethod
    def min_couleur_possible(gphe, etiq, s):
        """
        Trouve la plus petite couleur non utilisée par les voisins du sommet s.
        """
        n = len(gphe)
        used_colors = set()

        # Collecter les couleurs des voisins
        for t in range(n):
            if gphe[s][t] and etiq[t] != -1:
                used_colors.add(etiq[t])

        # Trouver la première couleur non utilisée
        color = 0
        while color in used_colors:
            color += 1

        return color
    
    @staticmethod
    def glouton(gphe, order):
        """
        Applique l'algorithme glouton pour colorier le graphe.
        Vérifie que l'ordre est une permutation valide des sommets.
        """
        n = len(gphe)
        # Vérifier que l'ordre contient exactement les sommets de 0 à n-1
        if sorted(order) != list(range(n)):
            raise ValueError("L'ordre donné n'est pas une permutation valide des sommets.")

        # Appeler la méthode existante glouton_coloriage
        colors = Partie3Model.glouton_coloriage(gphe, order)
        return colors
   

    @staticmethod
    def tri_degre(gphe):
        """
        Retourne les sommets triés par ordre décroissant de leurs degrés.
        """
        n = len(gphe)
        degres = [(i, sum(gphe[i])) for i in range(n)]
        # Tri des sommets par degré décroissant
        degres.sort(key=lambda x: x[1], reverse=True)
        return [sommet[0] for sommet in degres]
    
    @staticmethod
    def welsh_powell(gphe):
        """
        Implémente l'algorithme de Welsh-Powell pour colorier le graphe.
        """
        n = len(gphe)
        sommets_tries = Partie3Model.tri_degre(gphe)
        couleurs = [-1] * n  # Couleurs initialement non assignées (-1)

        # Parcourir les sommets triés et assigner la plus petite couleur disponible
        for sommet in sommets_tries:
            # Récupérer les couleurs utilisées par les voisins
            couleurs_voisins = set(
                couleurs[voisin]
                for voisin in range(n)
                if gphe[sommet][voisin] and couleurs[voisin] != -1
            )

            # Trouver la plus petite couleur non utilisée
            couleur = 0
            while couleur in couleurs_voisins:
                couleur += 1
            couleurs[sommet] = couleur

        return couleurs
    
class Partie4Model:
    @staticmethod
    def sous_graphe(gphe, sg):
        """
        Extrait le sous-graphe induit par les sommets spécifiés dans `sg`.
        :param gphe: Liste de listes représentant la matrice d'adjacence du graphe.
        :param sg: Liste d'indices des sommets à inclure dans le sous-graphe.
        :return: Matrice d'adjacence du sous-graphe.
        """
        # Vérifier la validité des sommets dans sg
        n = len(gphe)
        if any(v < 0 or v >= n for v in sg):
            raise ValueError("Les sommets dans `sg` doivent être compris entre 0 et n-1.")
        if len(sg) != len(set(sg)):
            raise ValueError("La liste `sg` ne doit pas contenir de doublons.")

        # Créer la matrice d'adjacence pour le sous-graphe
        sous_graphe = [[gphe[i][j] for j in sg] for i in sg]
        return sous_graphe
    
    @staticmethod
    def voisins_non_colories(gphe, etiq, s):
        """
        Renvoie la liste des voisins de s qui ne sont pas encore coloriés.
        """
        return [t for t in range(len(gphe)) if gphe[s][t] and etiq[t] == -1]

    @staticmethod
    def degre_non_colories(gphe, etiq, s):
        """
        Renvoie le degré (nombre) de voisins non coloriés pour le sommet s.
        """
        return len(Partie4Model.voisins_non_colories(gphe, etiq, s))
   
    @staticmethod
    def non_colories(gphe, etiq):
        """
        Renvoie la liste des sommets du graphe qui ne sont pas coloriés.
        """
        return [s for s in range(len(etiq)) if etiq[s] == -1]

    @staticmethod
    @staticmethod
    def wigderson(gphe):
        """
        Applique l'algorithme de Wigderson pour colorier un graphe 3-coloriable.

        Args:
            gphe (list[list[bool]]): Matrice d'adjacence du graphe.

        Returns:
            list[int]: Étiquetage des sommets avec les couleurs.
        """
        import math

        n = len(gphe)
        etiq = [-1] * n  # Initialisation : tous les sommets sont non coloriés
        c = 0  # Couleur initiale

        for s in range(n):
            voisins_nc = Partie4Model.voisins_non_colories(gphe, etiq, s)
            if len(voisins_nc) >= math.sqrt(n):
                # Sous-graphe induit par les voisins non coloriés
                sous_g = Partie4Model.sous_graphe(gphe, voisins_nc)
                sous_etiq = [-1] * len(voisins_nc)
                if Partie1Model.est_2_coloriable(sous_g):
                    sous_etiq = Partie2Model.deux_col(sous_g)[1]
                    for i, sommet in enumerate(voisins_nc):
                        etiq[sommet] = c + sous_etiq[i]
                    c += 2
        # Compléter avec un coloriage glouton
        restants = Partie4Model.non_colories(gphe, etiq)
        if restants:
            sous_g_restants = Partie4Model.sous_graphe(gphe, restants)
            restants_etiq = Partie3Model.glouton_coloriage(sous_g_restants, list(range(len(restants))))
            for i, sommet in enumerate(restants):
                etiq[sommet] = c + restants_etiq[i]

        return etiq
