## Architecture générale
L'application suit le modèle MVC (Modèle-Vue-Contrôleur), qui sépare les responsabilités en trois composants principaux :

Modèle (model.py) :

Gère les données et la logique métier.
Contient les algorithmes de coloriage et les structures de données des graphes.
Vue (view.py) :

Gère l'interface utilisateur.
Utilise Tkinter pour afficher les fenêtres, les boutons, les entrées, et les graphes.
Contrôleur (controller.py) :

Fait le lien entre le modèle et la vue.
Réagit aux événements déclenchés dans l'interface et invoque les fonctions appropriées du modèle.

## Détail des composants
1. Modèle : model.py
Responsabilité : Le modèle contient la logique métier et les données statiques des graphes. Chaque graphe est défini par :

Une matrice d'adjacence.
Une liste de couleurs pour les sommets.
Principales fonctionnalités :

Vérification de coloriage avec est_col.
Calcul du nombre chromatique pour le graphe de Petersen avec nombre_chromatique_petersen.

2. Vue : view.py
Responsabilité : La vue gère l'interface utilisateur. Elle affiche les fenêtres et recueille les entrées utilisateur.

Principales fonctionnalités :

Affichage principal (display) : Fenêtre principale avec les questions.
Visualisation des graphes :
Ouvre une fenêtre dédiée pour chaque graphe avec leurs images et options de vérification.
Notes :

La méthode center_window permet de centrer dynamiquement les fenêtres sur l'écran.
Les images des graphes sont affichées en utilisant Pillow.
3. Contrôleur : controller.py
Responsabilité : Le contrôleur relie la vue et le modèle. Il répond aux actions utilisateur (clics sur les boutons) en appelant les fonctions appropriées du modèle.


Voici une proposition de Documentation Technique Détaillée à ajouter dans votre projet. Elle décrit comment le modèle, la vue et le contrôleur sont structurés et interagissent.

2. Documentation Technique Détaillée
Architecture générale
L'application suit le modèle MVC (Modèle-Vue-Contrôleur), qui sépare les responsabilités en trois composants principaux :

Modèle (model.py) :

Gère les données et la logique métier.
Contient les algorithmes de coloriage et les structures de données des graphes.
Vue (view.py) :

Gère l'interface utilisateur.
Utilise Tkinter pour afficher les fenêtres, les boutons, les entrées, et les graphes.
Contrôleur (controller.py) :

Fait le lien entre le modèle et la vue.
Réagit aux événements déclenchés dans l'interface et invoque les fonctions appropriées du modèle.
Détail des composants
1. Modèle : model.py
Responsabilité : Le modèle contient la logique métier et les données statiques des graphes. Chaque graphe est défini par :

Une matrice d'adjacence.
Une liste de couleurs pour les sommets.
Structure :

python
Copier le code
class Partie1Model:
    GRAPHE1 = {
        "adjacency": [
            [False, True, False, False, True],  # Sommet 0 connecté à 1 et 4
            [True, False, True, False, False],  # Sommet 1 connecté à 0 et 2
            ...
        ],
        "coloring": [0, 1, 2, 1, 2]  # Couleurs des sommets (0=Bleu, 1=Rouge, 2=Vert)
    }

    @staticmethod
    def est_col(graphe, etiquettes):
        """
        Vérifie si un graphe est correctement colorié.
        """
        n = len(graphe)
        for i in range(n):
            for j in range(n):
                if graphe[i][j] and etiquettes[i] == etiquettes[j]:
                    return False
        return True

    @staticmethod
    def nombre_chromatique_petersen():
        """
        Retourne le nombre chromatique du graphe de Petersen et un exemple de coloriage.
        """
        return 3, [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
Principales fonctionnalités :

Vérification de coloriage avec est_col.
Calcul du nombre chromatique pour le graphe de Petersen avec nombre_chromatique_petersen.
2. Vue : view.py
Responsabilité : La vue gère l'interface utilisateur. Elle affiche les fenêtres et recueille les entrées utilisateur.

Structure :

python
Copier le code
class Partie1View:
    def __init__(self, controller):
        self.controller = controller
        self.img1 = None  # Références pour les images
        self.img2 = None

    def display(self):
        """
        Affiche la fenêtre principale pour la Partie 1.
        """
        window = Toplevel()
        window.title("Partie 1 : Coloriage Basique")
        self.center_window(window, 800, 800)

        # Interface des questions
        Label(window, text="Question 1 : Vérifier un coloriage").grid(...)
        Button(window, text="Visualiser les graphes", command=self.ouvrir_visualisation_graphes).grid(...)

    def ouvrir_visualisation_graphes(self):
        """
        Affiche une fenêtre secondaire pour choisir un graphe à visualiser.
        """
        window = Toplevel()
        self.center_window(window, 400, 200)

        Button(window, text="Graphe 1", command=self.afficher_graphe_1).pack(...)
        Button(window, text="Graphe 2", command=self.afficher_graphe_2).pack(...)

    def afficher_graphe_1(self):
        """
        Affiche le graphe 1 dans une nouvelle fenêtre.
        """
        window = Toplevel()
        self.center_window(window, 400, 400)

        self.img1 = ImageTk.PhotoImage(Image.open("resources/graphe1.png"))
        Label(window, image=self.img1).pack()
Principales fonctionnalités :

Affichage principal (display) : Fenêtre principale avec les questions.
Visualisation des graphes :
Ouvre une fenêtre dédiée pour chaque graphe avec leurs images et options de vérification.
Notes :

La méthode center_window permet de centrer dynamiquement les fenêtres sur l'écran.
Les images des graphes sont affichées en utilisant Pillow.
3. Contrôleur : controller.py
Responsabilité : Le contrôleur relie la vue et le modèle. Il répond aux actions utilisateur (clics sur les boutons) en appelant les fonctions appropriées du modèle.

Structure :

python
Copier le code
class Partie1Controller:
    def __init__(self, view=None):
        self.view = view

    def verifier_graphe(self, graphe_id):
        """
        Vérifie si le graphe sélectionné est correctement colorié.
        """
        graphe = Partie1Model.GRAPHE1 if graphe_id == 1 else Partie1Model.GRAPHE2
        adjacency = graphe["adjacency"]
        coloring = graphe["coloring"]

        if Partie1Model.est_col(adjacency, coloring):
            messagebox.showinfo("Résultat", "Le coloriage est valide.")
        else:
            messagebox.showinfo("Résultat", "Le coloriage n'est pas valide.")

    def calculer_nombre_chromatique(self):
        """
        Calcule le nombre chromatique pour le graphe de Petersen.
        """
        nombre, coloriage = Partie1Model.nombre_chromatique_petersen()
        messagebox.showinfo("Résultat", f"Nombre chromatique : {nombre}\nColoriage : {coloriage}")
Principales fonctionnalités :

verifier_graphe(graphe_id) : Vérifie si un graphe (1 ou 2) est colorié correctement en appelant le modèle.
calculer_nombre_chromatique : Appelle le modèle pour calculer le nombre chromatique.
expliquer_complexite : Affiche une boîte d'information sur la complexité.

Interactions entre les composants
Flux d'interaction :

L'utilisateur interagit avec l'interface dans view.py.
Les actions déclenchent des appels aux méthodes du contrôleur dans controller.py.
Le contrôleur invoque les fonctions du modèle dans model.py.
Les résultats du modèle sont renvoyés à la vue pour affichage.
Exemple d'interaction :

Action utilisateur : Cliquer sur "Vérifier Graphe 1".
Appel du contrôleur : La méthode verifier_graphe(1) est appelée.
Appel du modèle : La méthode est_col est utilisée pour vérifier le coloriage.
Affichage des résultats : La vue affiche une boîte de dialogue avec le résultat.