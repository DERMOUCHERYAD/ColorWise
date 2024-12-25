from tkinter import messagebox
from model import Partie1Model,Partie2Model,Partie3Model,Partie4Model
import tkinter as tk
from tkinter import Toplevel, Label, Button,Text
import math

class Partie1Controller:
    def __init__(self, view=None):
        """Initialise le contrôleur avec une vue optionnelle."""
        self.view = view

    def verifier_graphe(self, graphe_id):
        """Vérifie si le graphe sélectionné est colorié correctement."""
        if graphe_id == 1:
            graphe = Partie1Model.GRAPHE1
        elif graphe_id == 2:
            graphe = Partie1Model.GRAPHE2
        else:
            messagebox.showerror("Erreur", "Graphe non valide.")
            return

        adjacency = graphe["adjacency"]
        coloring = graphe["coloring"]
        if Partie1Model.est_col(adjacency, coloring):
            messagebox.showinfo("Résultat", "Le coloriage est valide.")
        else:
            messagebox.showinfo("Résultat", "Le coloriage n'est pas valide.")

    def verifier_coloriage(self, graphe_input, etiquetage_input):
        """Vérifie un coloriage donné par l'utilisateur."""
        try:
            graphe = eval(graphe_input)  # Convertir la saisie en structure Python
            etiquetage = eval(etiquetage_input)
            if Partie1Model.est_col(graphe, etiquetage):
                messagebox.showinfo("Résultat", "Le coloriage est valide.")
            else:
                messagebox.showinfo("Résultat", "Le coloriage n'est pas valide.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Entrée invalide : {e}")

    def calculer_nombre_chromatique(self):
        """Calcule le nombre chromatique pour le graphe de Petersen."""
        nombre, coloriage = Partie1Model.nombre_chromatique_petersen()
        messagebox.showinfo("Résultat", f"Nombre chromatique : {nombre}\nColoriage : {coloriage}")

    def verifier_2_coloriable(self, graphe_input):
        """Vérifie si un graphe est 2-coloriable."""
        try:
            graphe = eval(graphe_input)
            if Partie1Model.est_2_coloriable(graphe):
                messagebox.showinfo("Résultat", "Le graphe est 2-coloriable.")
            else:
                messagebox.showinfo("Résultat", "Le graphe n'est pas 2-coloriable.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Entrée invalide : {e}")

    def expliquer_complexite(self):
        """Affiche une explication sur la complexité exponentielle."""
        messagebox.showinfo(
            "Complexité",
            "Calculer le nombre chromatique est un problème de complexité NP-complet. "
            "Cela implique qu’il n’existe pas d’algorithme connu en temps polynomial pour résoudre ce problème "
            "dans tous les cas."
        )

    def colorier_petersen(self):
        """
        Colorie le graphe de Petersen et affiche le résultat.
        """
        coloriage = Partie1Model.colorier_graphe_petersen()
        messagebox.showinfo("Résultat", f"Coloriage du graphe de Petersen : {coloriage}")
        self.view.afficher_graphe_colore(coloriage)



class Partie2Controller:
    def __init__(self, view=None):
        self.view = view

    def verifier_2_coloriabilite(self, graphe_input):
        """Vérifie si un graphe est 2-coloriable et met à jour le label résultat."""
        try:
            graphe = eval(graphe_input)  # Convertir l'entrée en une matrice Python
            is_2_coloriable, couleurs = Partie2Model.deux_col(graphe)
            if is_2_coloriable:
                self.view.afficher_resultat(f"Le graphe est 2-coloriable.\nÉtiquetage : {couleurs}")
            else:
                self.view.afficher_resultat("Le graphe n'est pas 2-coloriable.")
        except Exception as e:
            self.view.afficher_resultat(f"Erreur : Entrée invalide.\nDétail : {e}")

# controller.py

from model import Partie3Model

class Partie3Controller:
    def __init__(self, view=None):
        self.view = view

    def afficher_couleurs_petersen(self, num):
        """
        Affiche la liste des couleurs pour une numération donnée.
        """
        # Exemples de résultats pour les deux numérations
        if num == 1:
            order = [1, 3, 4, 0, 2, 6, 5, 9, 8, 7]
        elif num == 2:
            order = [0, 7, 2, 5, 4, 6, 8, 1, 3, 9]
        else:
            self.view.afficher_resultat("Numération invalide.")
            return

        adjacency_matrix = Partie1Model.GRAPHE_PETERSEN["adjacency"]
        colors = Partie3Model.glouton_coloriage(adjacency_matrix, order)
        self.view.afficher_resultat(f"Liste des couleurs pour numération {num} : {colors}")

    def afficher_nombre_couleurs(self, num):
        """
        Affiche le nombre de couleurs utilisées pour une numération donnée.
        """
        if num == 1:
            order = [1, 3, 4, 0, 2, 6, 5, 9, 8, 7]
        elif num == 2:
            order = [0, 7, 2, 5, 4, 6, 8, 1, 3, 9]
        else:
            self.view.afficher_resultat("Numération invalide.")
            return

        adjacency_matrix = Partie1Model.GRAPHE_PETERSEN["adjacency"]
        colors = Partie3Model.glouton_coloriage(adjacency_matrix, order)
        num_colors = Partie3Model.nombre_de_couleurs(colors)
        self.view.afficher_resultat(f"Nombre de couleurs utilisées pour numération {num} : {num_colors}")
    
    def executer_algorithme_glouton(self, graphe_input, ordre_input):
        """
        Exécute l'algorithme glouton avec un graphe et un ordre donnés.
        """
        try:
            graphe = eval(graphe_input)
            ordre = eval(ordre_input)
            coloriage = Partie3Model.glouton_coloriage(graphe, ordre)
            nombre_couleurs = Partie3Model.nombre_de_couleurs(coloriage)

            self.view.afficher_resultat(
                f"Résultat du coloriage glouton :\n{coloriage}\n"
                f"Nombre de couleurs utilisées : {nombre_couleurs}"
            )
        except Exception as e:
            self.view.afficher_resultat(f"Erreur : Entrée invalide.\nDétail : {e}")


    def calculer_min_couleur(self, graphe_input, etiquetage_input, sommet):
        """
        Calcule la plus petite couleur non utilisée par les voisins du sommet donné.
        """
        try:
            graphe = eval(graphe_input)  # Convertir en matrice
            etiquetage = eval(etiquetage_input)  # Convertir en liste d'étiquetage
            sommet = int(sommet)  # Convertir en entier
            min_color = Partie3Model.min_couleur_possible(graphe, etiquetage, sommet)
            self.view.afficher_resultat(f"La plus petite couleur possible pour le sommet {sommet} est : {min_color}")
        except Exception as e:
            self.view.afficher_resultat(f"Erreur : Entrée invalide.\nDétail : {e}")

    def afficher_resultat_min_couleur(self, graphe_input, etiquetage_input, sommet_input):
        """Affiche le résultat dans une nouvelle fenêtre."""
        try:
            graphe = eval(graphe_input)
            etiquetage = eval(etiquetage_input)
            sommet = int(sommet_input)

            # Calculer la couleur minimale possible
            couleur = Partie3Model.min_couleur_possible(graphe, etiquetage, sommet)

            # Créer une nouvelle fenêtre pour afficher le résultat
            result_window = Toplevel()
            result_window.title("Résultat : Couleur minimale possible")
            result_window.geometry("400x200")

            Label(result_window, text=f"Résultat pour le sommet {sommet} :", font=("Helvetica", 12, "bold")).pack(pady=10)
            Label(result_window, text=f"Couleur minimale possible : {couleur}", font=("Helvetica", 10)).pack(pady=20)

            Button(result_window, text="Fermer", command=result_window.destroy).pack(pady=10)

        except Exception as e:
            messagebox.showerror("Erreur", f"Entrée invalide.\nDétail : {e}")

    def appliquer_algorithme_glouton(self, graphe_input, order_input):
        """
        Applique l'algorithme glouton et affiche le résultat.
        """
        try:
            # Convertir les entrées en structures Python
            graphe = eval(graphe_input)
            order = eval(order_input)

            # Appeler la méthode glouton
            colors = Partie3Model.glouton(graphe, order)
            num_colors = Partie3Model.nombre_de_couleurs(colors)

            # Afficher le résultat dans une nouvelle fenêtre
            resultat = f"Coloriage glouton : {colors}\nNombre de couleurs utilisées : {num_colors}"
            messagebox.showinfo("Résultat", resultat)

        except ValueError as ve:
            messagebox.showerror("Erreur", str(ve))
        except Exception as e:
            messagebox.showerror("Erreur", f"Entrée invalide : {e}")
    

    def appliquer_welsh_powell(self, graphe_input):
        """
        Applique l'algorithme de Welsh-Powell et affiche les résultats dans une nouvelle fenêtre.
        """
        try:
            graphe = eval(graphe_input)  # Convertir l'entrée en une matrice Python
            tri_sommets = Partie3Model.tri_degre(graphe)  # Trier les sommets par degré décroissant
            coloriage = Partie3Model.welsh_powell(graphe)

            # Créer une nouvelle fenêtre pour afficher le résultat
            result_window = Toplevel()
            result_window.title("Résultat Welsh-Powell")
            result_window.geometry("400x400")

            Label(result_window, text="Résultat Welsh-Powell", font=("Helvetica", 14, "bold")).pack(pady=10)

            # Afficher les résultats du tri des sommets
            Label(result_window, text="Sommets triés par degré décroissant :", font=("Helvetica", 12)).pack(pady=5)
            tri_text = tk.Text(result_window, height=5, width=40, wrap="word")
            tri_text.pack(pady=5)
            tri_text.insert("end", f"{tri_sommets}")
            tri_text.configure(state="disabled")

            # Afficher les résultats du coloriage
            Label(result_window, text="Coloriage :", font=("Helvetica", 12)).pack(pady=5)
            coloriage_text = tk.Text(result_window, height=5, width=40, wrap="word")
            coloriage_text.pack(pady=5)
            coloriage_text.insert("end", f"{coloriage}\nNombre de couleurs : {Partie3Model.nombre_de_couleurs(coloriage)}")
            coloriage_text.configure(state="disabled")

            # Bouton pour fermer la fenêtre
            Button(result_window, text="Fermer", command=result_window.destroy, bg="#e67300", fg="white").pack(pady=10)
        except Exception as e:
            messagebox.showerror("Erreur", f"Entrée invalide : {e}")


class Partie4Controller:
    def __init__(self, view=None):
        self.view = view

    def extraire_sous_graphe(self, graphe_input, sommets_input):
        """
        Gère l'extraction d'un sous-graphe à partir des sommets spécifiés.
        :param graphe_input: Saisie utilisateur pour la matrice d'adjacence.
        :param sommets_input: Saisie utilisateur pour la liste de sommets.
        """
        try:
            gphe = eval(graphe_input)  # Convertir la saisie utilisateur en matrice
            sg = eval(sommets_input)  # Convertir la saisie utilisateur en liste
            result = Partie4Model.sous_graphe(gphe, sg)
            self.view.afficher_resultat_sous_graphe(result)
        except Exception as e:
            self.view.afficher_resultat_sous_graphe(f"Erreur : {e}")
    
    def get_voisins_non_colories(self, graphe, etiq, sommet):
        """
        Renvoie la liste des voisins non coloriés pour un sommet donné.
        """
        return Partie4Model.voisins_non_colories(graphe, etiq, sommet)

    def get_degre_non_colories(self, graphe, etiq, sommet):
        """
        Renvoie le degré des voisins non coloriés pour un sommet donné.
        """
        return Partie4Model.degre_non_colories(graphe, etiq, sommet)
    
    def afficher_voisins_degre(self, graphe_input, etiq_input, sommet_input):
        """
        Affiche les voisins non coloriés et le degré non colorié d'un sommet.
        """
        try:
            # Conversion des entrées
            graphe = eval(graphe_input)  # Convertit l'entrée en structure Python
            etiq = eval(etiq_input)
            sommet = int(sommet_input)

            # Calcul des voisins non coloriés et du degré
            voisins = Partie4Model.voisins_non_colories(graphe, etiq, sommet)
            degre = Partie4Model.degre_non_colories(graphe, etiq, sommet)

            # Création de la fenêtre des résultats
            result_window = Toplevel()
            result_window.title("Résultats : Voisins et Degré Non Coloriés")
            result_window.geometry("500x300")  # Taille initiale plus grande

            # Affichage des voisins non coloriés
            Label(result_window, text="Voisins non coloriés :", font=("Helvetica", 12, "bold")).pack(pady=5)
            text_voisins = Text(result_window, height=5, width=60, wrap="word", bg="#ffffff")
            text_voisins.insert("end", f"{voisins}")
            text_voisins.configure(state="disabled")  # Désactiver la modification
            text_voisins.pack(pady=5)

            # Affichage du degré non colorié
            Label(result_window, text="Degré non coloriés :", font=("Helvetica", 12, "bold")).pack(pady=5)
            text_degre = Text(result_window, height=2, width=20, wrap="word", bg="#ffffff")
            text_degre.insert("end", f"{degre}")
            text_degre.configure(state="disabled")  # Désactiver la modification
            text_degre.pack(pady=5)
 
        except Exception as e:
            # Affichage des erreurs dans une boîte de dialogue
            messagebox.showerror("Erreur", f"Entrée invalide : {e}")
        
    def get_non_colories(self, graphe, etiq):
        """
        Renvoie la liste des sommets non coloriés pour un graphe donné.
        """
        return Partie4Model.non_colories(graphe, etiq)
    
    def afficher_non_colories(self, graphe_input, etiq_input):
        """
        Affiche les sommets non coloriés pour un graphe donné et un étiquetage.
        """
        try:
            graphe = eval(graphe_input)  # Convertit la saisie en structure Python
            etiq = eval(etiq_input)

            non_colored = Partie4Model.non_colories(graphe, etiq)

            # Fenêtre pour afficher les résultats
            result_window = Toplevel()
            result_window.title("Résultats : Sommets non coloriés")
            result_window.geometry("400x200")  # Taille adaptée
            result_window.update_idletasks()

            # Centrer la fenêtre
            screen_width = result_window.winfo_screenwidth()
            screen_height = result_window.winfo_screenheight()
            window_width = 400
            window_height = 200
            position_x = (screen_width // 2) - (window_width // 2)
            position_y = (screen_height // 2) - (window_height // 2)
            result_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

            # Contenu de la fenêtre
            Label(result_window, text=f"Sommets non coloriés : {non_colored}", font=("Helvetica", 12)).pack(pady=20)

        except Exception as e:
            messagebox.showerror("Erreur", f"Entrée invalide : {e}")
    
    def appliquer_wigderson(self, graphe_input):
        """
        Applique l'algorithme de Wigderson à un graphe donné et affiche le résultat.

        Args:
            graphe_input (str): La matrice d'adjacence sous forme de chaîne de caractères.
        """
        try:
            gphe = eval(graphe_input)  # Convertir la chaîne en matrice
            etiq = Partie4Model.wigderson(gphe)

            # Affichage des résultats
            result_window = Toplevel()
            result_window.title("Résultat de l'algorithme de Wigderson")
            result_window.geometry("400x400")

            Label(result_window, text=f"Étiquetage des sommets : {etiq}").pack(pady=10)
            nb_colors = len(set(etiq))
            Label(result_window, text=f"Nombre de couleurs utilisées : {nb_colors}").pack(pady=10)

        except Exception as e:
            messagebox.showerror("Erreur", f"Entrée invalide : {e}")
    
    def afficher_graphe_colorie(self, graphe_input):
        """
        Affiche visuellement le graphe colorié par l'algorithme de Wigderson.
        """
        try:
            graphe = eval(graphe_input)
            etiq = Partie4Model.wigderson(graphe)

            # Ouvrir une nouvelle fenêtre pour afficher le graphe
            result_window = Toplevel()
            result_window.title("Graphe colorié par Wigderson")
            result_window.geometry("600x600")

            canvas = tk.Canvas(result_window, width=500, height=500)
            canvas.pack()

            # Positions des sommets (à adapter pour des graphes plus complexes)
            n = len(graphe)
            angle_step = 360 / n
            radius = 200
            center = (250, 250)

            positions = [
                (
                    center[0] + radius * math.cos(math.radians(i * angle_step)),
                    center[1] + radius * math.sin(math.radians(i * angle_step))
                )
                for i in range(n)
            ]

            # Dessiner les arêtes
            for i in range(n):
                for j in range(n):
                    if graphe[i][j]:  # S'il y a une arête
                        canvas.create_line(
                            positions[i][0], positions[i][1],
                            positions[j][0], positions[j][1],
                            fill="black"
                        )

            # Couleurs utilisées pour les sommets
            colors = {0: "red", 1: "green", 2: "blue", 3: "yellow", 4: "purple", 5: "orange"}

            # Dessiner les sommets
            for i, (x, y) in enumerate(positions):
                canvas.create_oval(
                    x - 10, y - 10, x + 10, y + 10,
                    fill=colors[etiq[i] % len(colors)],
                    outline="black"
                )
                canvas.create_text(x, y - 15, text=f"{i} ({etiq[i]})")

        except Exception as e:
            messagebox.showerror("Erreur", f"Entrée invalide : {e}")
    
    def afficher_resultat_wigderson(self, graphe_input):
        """
        Applique l'algorithme de Wigderson sur le graphe donné et affiche les résultats.
        """
        try:
            # Convertir la saisie en matrice d'adjacence
            graphe = eval(graphe_input)
            
            # Appliquer l'algorithme de Wigderson
            etiq = Partie4Model.wigderson(graphe)
            nb_couleurs = max(etiq) + 1  # Nombre de couleurs utilisées
            
            # Créer une fenêtre pour afficher les résultats
            result_window = Toplevel()
            result_window.title("Résultats : Algorithme de Wigderson")
            result_window.geometry("400x300")
            
            Label(result_window, text=f"Étiquetage des sommets : {etiq}").pack(pady=10)
            Label(result_window, text=f"Nombre de couleurs utilisées : {nb_couleurs}").pack(pady=10)

        except Exception as e:
            messagebox.showerror("Erreur", f"Entrée invalide ou problème : {e}")
