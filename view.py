import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry, messagebox
from PIL import Image, ImageTk
from model import Partie1Model,Partie2Model,Partie3Model

class Partie1View:
    def __init__(self, controller):
        self.controller = controller
        self.img1 = None  # Références explicites pour éviter le garbage collector
        self.img2 = None

    def center_window(self, window, width, height):
        """Centre une fenêtre Toplevel sur l'écran."""
        window.update_idletasks()  # Assure que winfo_screenwidth() fonctionne correctement
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calculer la position x et y
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        window.geometry(f"{width}x{height}+{x}+{y}")

    
    
    def display(self):
        
        """Affiche la fenêtre principale pour la Partie 1."""
        window = Toplevel()
        window.title("Partie 1 : Coloriage Basique")
        window.configure(bg="#f0f0f0")  # Couleur de fond de la fenêtre

        # Centrer la fenêtre
        self.center_window(window, 500, 800)

        # Styles généraux
        title_font = ("Helvetica", 16, "bold")
        section_font = ("Helvetica", 12, "bold")
        button_font = ("Helvetica", 10)
        # ===================
        # Visualisation des graphes
        # ===================
        frame_visualisation = tk.Frame(window, bg="#e6f7ff", relief="groove", bd=2, padx=10, pady=10)
        frame_visualisation.pack(fill="x", padx=10, pady=10)

        Label(frame_visualisation, text="Visualisation des graphes", font=section_font, bg="#e6f7ff").pack(pady=5)
        Button(
            frame_visualisation,
            text="Visualiser les graphes",
            font=button_font,
            bg="#0073e6",
            fg="white",
            command=self.ouvrir_visualisation_graphes
        ).pack(pady=10)
         # ===================
        # Nombre chromatique
        # ===================
        frame_chromatic = tk.Frame(window, bg="#fbe4d5", relief="groove", bd=2, padx=10, pady=10)
        frame_chromatic.pack(fill="x", padx=10, pady=10)

        Label(frame_chromatic, text="Nombre chromatique", font=section_font, bg="#fbe4d5").pack(pady=5)
        Button(
            frame_chromatic,
            text="Calculer",
            font=button_font,
            bg="#e67300",
            fg="white",
            command=self.controller.calculer_nombre_chromatique
        ).pack(pady=5)
        Button(
            frame_chromatic,
            text="Colorier le graphe de Petersen",
            font=button_font,
            bg="#e67300",
            fg="white",
            command=self.controller.colorier_petersen
        ).pack(pady=5)
        # ===================
        # Vérification de la propriété de coloriage
        # ===================
        frame_coloring_check = tk.Frame(window, bg="#e6f7ff", relief="groove", bd=2, padx=10, pady=10)
        frame_coloring_check.pack(fill="x", padx=10, pady=10)

        Label(frame_coloring_check, text="Vérification de la propriété de coloriage", font=section_font, bg="#e6f7ff").pack(pady=5)
        Label(frame_coloring_check, text="Matrice d'adjacence :", bg="#e6f7ff").pack(pady=5)
        entry_graphe_2_col = Entry(frame_coloring_check, width=50)
        entry_graphe_2_col.pack(pady=5)
        Label(frame_coloring_check, text="Etiquetage :", bg="#e6f7ff").pack(pady=5)
        entry_etiquetage_2_col = Entry(frame_coloring_check, width=50)
        entry_etiquetage_2_col.pack(pady=5)
        Button(
            frame_coloring_check,
            text="Vérifier",
            font=button_font,
            bg="#0073e6",
            fg="white",
            command=lambda: self.controller.verifier_coloriage(entry_graphe_2_col.get(), entry_etiquetage_2_col.get())
        ).pack(pady=10)
        # ===================
        # Complexité exponentielle
        # ===================
        frame_complexity = tk.Frame(window, bg="#fbe4d5", relief="groove", bd=2, padx=10, pady=10)
        frame_complexity.pack(fill="x", padx=10, pady=10)

        Label(frame_complexity, text="Complexité exponentielle", font=section_font, bg="#fbe4d5").pack(pady=5)
        Button(
            frame_complexity,
            text="Expliquer",
            font=button_font,
            bg="#e67300",
            fg="white",
            command=self.controller.expliquer_complexite
        ).pack(pady=10)
        # ===================
        # Bouton de fermeture
        # ===================
        Button(
            window,
            text="Fermer",
            font=button_font,
            bg="#e67300",
            fg="white",
            command=window.destroy
        ).pack(pady=20)

       

    def ouvrir_visualisation_graphes(self):
        """Ouvre une nouvelle fenêtre avec des boutons pour visualiser les graphes."""
        window = Toplevel()
        window.title("Choix des graphes")

        # Centrer la fenêtre
        self.center_window(window, 400, 200)

        Label(window, text="Choisissez un graphe à visualiser").pack(pady=10)

        Button(
            window,
            text="Visualiser Graphe 1",
            command=self.afficher_graphe_1
        ).pack(pady=5)

        Button(
            window,
            text="Visualiser Graphe 2",
            command=self.afficher_graphe_2
        ).pack(pady=5)

    def afficher_graphe_1(self):
        """Ouvre une fenêtre pour afficher le Graphe 1."""
        window = Toplevel()
        window.title("Graphe 1")

        # Centrer la fenêtre
        self.center_window(window, 400, 400)

        # Charger et afficher l'image
        self.img1 = Image.open("resources/graphe1.png")
        self.img1 = self.img1.resize((300, 300), Image.Resampling.LANCZOS)
        self.img1 = ImageTk.PhotoImage(self.img1)

        Label(window, text="Graphe 1").pack(pady=10)
        Label(window, image=self.img1).pack()

        Button(
            window,
            text="Vérifier Graphe 1",
            command=lambda: self.controller.verifier_graphe(1)
        ).pack(pady=10)

    def afficher_graphe_2(self):
        """Ouvre une fenêtre pour afficher le Graphe 2."""
        window = Toplevel()
        window.title("Graphe 2")

        # Centrer la fenêtre
        self.center_window(window, 400, 400)

        # Charger et afficher l'image
        self.img2 = Image.open("resources/graphe2.png")
        self.img2 = self.img2.resize((300, 300), Image.Resampling.LANCZOS)
        self.img2 = ImageTk.PhotoImage(self.img2)

        Label(window, text="Graphe 2").pack(pady=10)
        Label(window, image=self.img2).pack()

        Button(
            window,
            text="Vérifier Graphe 2",
            command=lambda: self.controller.verifier_graphe(2)
        ).pack(pady=10)

    def afficher_graphe_colore(self, coloriage):
        """
        Affiche le graphe de Petersen coloré avec l'exemple de coloriage donné.
        """
        window = Toplevel()
        window.title("Graphe de Petersen Coloré")
        window.geometry("600x600")

        canvas = tk.Canvas(window, width=500, height=500)
        canvas.pack()

        # Positions des sommets (approximées pour un dessin propre)
        positions = [
            (250, 50), (400, 150), (350, 300), (150, 300), (100, 150),
            (250, 150), (325, 225), (250, 375), (175, 225), (250, 275)
        ]

        # Couleurs pour les sommets
        colors = {1: "red", 2: "green", 3: "blue"}

        # Dessiner les arêtes
        adj = Partie1Model.GRAPHE_PETERSEN["adjacency"]
        for i in range(len(adj)):
            for j in range(len(adj)):
                if adj[i][j]:
                    canvas.create_line(
                        positions[i][0], positions[i][1],
                        positions[j][0], positions[j][1],
                        fill="black"
                    )

        # Dessiner les sommets
        for i, (x, y) in enumerate(positions):
            canvas.create_oval(
                x - 10, y - 10, x + 10, y + 10,
                fill=colors[coloriage[i]],
                outline="black"
            )
            canvas.create_text(x, y - 15, text=str(i))

        Label(window, text="Graphe de Petersen coloré avec 3 couleurs").pack(pady=10)




class Partie2View:
    def __init__(self, controller):
        self.controller = controller

    def center_window(self, window, width, height):
        """Centre une fenêtre Toplevel sur l'écran."""
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")


    def display(self):
        """Affiche la fenêtre principale pour la Partie 2."""
        window = Toplevel()
        window.title("Partie 2 : 2-coloriabilité")
        window.configure(bg="#f0f0f0")  # Couleur de fond de la fenêtre

        # Centrer la fenêtre
        self.center_window(window, 500, 800)

        # Styles généraux
        title_font = ("Helvetica", 16, "bold")
        section_font = ("Helvetica", 12, "bold")
        button_font = ("Helvetica", 10)

        # ===================
        # Vérification de la 2-coloriabilité
        # ===================
        frame_check_2color = tk.Frame(window, bg="#e6f7ff", relief="groove", bd=2, padx=10, pady=10)
        frame_check_2color.pack(fill="x", padx=10, pady=10)

        Label(frame_check_2color, text="Vérification de la 2-coloriabilité", font=section_font, bg="#e6f7ff").pack(pady=5)
        Label(frame_check_2color, text="Matrice d'adjacence :", bg="#e6f7ff").pack(pady=5)
        entry_graphe = Entry(frame_check_2color, width=50)
        entry_graphe.pack(pady=5)
        Button(
            frame_check_2color,
            text="Vérifier",
            font=button_font,
            bg="#0073e6",
            fg="white",
            command=lambda: self.controller.verifier_2_coloriabilite(entry_graphe.get())
        ).pack(pady=10)

        # ===================
        # Résultats
        # ===================
        frame_results = tk.Frame(window, bg="#fbe4d5", relief="groove", bd=2, padx=10, pady=10)
        frame_results.pack(fill="x", padx=10, pady=10)

        Label(frame_results, text="Résultat de l'analyse", font=section_font, bg="#fbe4d5").pack(pady=5)
        self.text_result = tk.Text(frame_results, height=10, width=60, state="disabled", wrap="word", bg="#ffffff")
        self.text_result.pack(pady=10)

        # ===================
        # Bouton de fermeture
        # ===================
        Button(
            window,
            text="Fermer",
            font=button_font,
            bg="#e67300",
            fg="white",
            command=window.destroy
        ).pack(pady=20)


    def afficher_resultat(self, resultat):
        """Affiche un résultat dans la zone de texte des résultats."""
        self.text_result.configure(state="normal")
        self.text_result.delete(1.0, "end")
        self.text_result.insert("end", resultat)
        self.text_result.configure(state="disabled")


# view.py

import tkinter as tk
from tkinter import Toplevel, Label, Entry, Button, Text, Frame

class Partie3View:
    def __init__(self, controller):
        self.controller = controller

    def center_window(self, window, width, height):
        """Centre une fenêtre Toplevel sur l'écran."""
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def display(self):
        """Affiche la fenêtre principale pour la Partie 3 avec scrollbar."""
        window = Toplevel()
        window.title("Partie 3 : Algorithme Glouton")
        window.geometry("500x600")  # Taille compacte

        # Cadre principal pour la scrollbar
        main_frame = tk.Frame(window)
        main_frame.pack(fill="both", expand=True)

        # Canvas pour le contenu défilant
        canvas = tk.Canvas(main_frame, bg="#f0f0f0")
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")

        # Configuration du canvas
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Placement du canvas et de la scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Styles généraux
        section_font = ("Helvetica", 12, "bold")
        button_font = ("Helvetica", 10)

        # ===================
        # Question 7 : Exemples de numération
        # ===================
        frame_q7 = tk.Frame(scrollable_frame, bg="#e6f7ff", relief="groove", bd=2, padx=10, pady=10)
        frame_q7.pack(fill="x", padx=10, pady=10)

        Label(frame_q7, text="Question 7 : Exemples de numération", font=section_font, bg="#e6f7ff").pack(pady=5)

        # Numération 1
        frame_num1 = tk.Frame(frame_q7, bg="#d9f2d9", relief="solid", bd=1, padx=5, pady=5)
        frame_num1.pack(fill="x", pady=5)
        Label(frame_num1, text="Numération 1", bg="#d9f2d9").pack()
        Button(
            frame_num1,
            text="Afficher la liste des couleurs",
            font=button_font,
            bg="#4caf50",
            fg="white",
            command=lambda: self.controller.afficher_couleurs_petersen(1)
        ).pack(pady=5)
        Button(
            frame_num1,
            text="Afficher le nombre de couleurs",
            font=button_font,
            bg="#4caf50",
            fg="white",
            command=lambda: self.controller.afficher_nombre_couleurs(1)
        ).pack(pady=5)

        # Numération 2
        frame_num2 = tk.Frame(frame_q7, bg="#f2d9d9", relief="solid", bd=1, padx=5, pady=5)
        frame_num2.pack(fill="x", pady=5)
        Label(frame_num2, text="Numération 2", bg="#f2d9d9").pack()
        Button(
            frame_num2,
            text="Afficher la liste des couleurs",
            font=button_font,
            bg="#e53935",
            fg="white",
            command=lambda: self.controller.afficher_couleurs_petersen(2)
        ).pack(pady=5)
        Button(
            frame_num2,
            text="Afficher le nombre de couleurs",
            font=button_font,
            bg="#e53935",
            fg="white",
            command=lambda: self.controller.afficher_nombre_couleurs(2)
        ).pack(pady=5)

        # ===================
        # Résultats
        # ===================
        frame_results = tk.Frame(scrollable_frame, bg="#fbe4d5", relief="groove", bd=2, padx=10, pady=10)
        frame_results.pack(fill="x", padx=10, pady=10)

        Label(frame_results, text="Résultats", font=section_font, bg="#fbe4d5").pack(pady=5)
        self.text_result = tk.Text(frame_results, height=2, width=60, state="disabled", wrap="word", bg="#ffffff")
        self.text_result.pack(pady=10)

        # ===================
        # Calcul de la couleur minimale possible
        # ===================
        frame_min_color = tk.Frame(scrollable_frame, bg="#e6f7ff", relief="groove", bd=2, padx=10, pady=10)
        frame_min_color.pack(fill="x", padx=10, pady=10)

        Label(frame_min_color, text="Couleur minimale possible", font=section_font, bg="#e6f7ff").pack(pady=5)

        Label(frame_min_color, text="Matrice :", bg="#e6f7ff").pack(pady=5)
        entry_graphe = Entry(frame_min_color, width=40)
        entry_graphe.pack(pady=5)

        Label(frame_min_color, text="Étiquetage :", bg="#e6f7ff").pack(pady=5)
        entry_etiquetage = Entry(frame_min_color, width=40)
        entry_etiquetage.pack(pady=5)

        Label(frame_min_color, text="Sommet :", bg="#e6f7ff").pack(pady=5)
        entry_sommet = Entry(frame_min_color, width=10)
        entry_sommet.pack(pady=5)

        # Bouton pour calculer et afficher dans une nouvelle fenêtre
        Button(
            frame_min_color,
            text="Afficher le résultat",
            font=button_font,
            bg="#0073e6",
            fg="white",
            command=lambda: self.controller.afficher_resultat_min_couleur(
                entry_graphe.get(), entry_etiquetage.get(), entry_sommet.get()
            )
        ).pack(pady=10)
       
        # ===================
        # Coloration Gloutonne
        # ===================
        frame_glouton = tk.Frame(scrollable_frame, bg="#e6f7ff", relief="groove", bd=2, padx=10, pady=10)
        frame_glouton.pack(fill="x", padx=10, pady=10)

        Label(frame_glouton, text="Coloration Gloutonne", font=section_font, bg="#e6f7ff").pack(pady=5)

        Label(frame_glouton, text="Matrice d'adjacence :", bg="#e6f7ff").pack(pady=5)
        entry_graphe = Entry(frame_glouton, width=50)
        entry_graphe.pack(pady=5)

        Label(frame_glouton, text="Ordre de numérotation :", bg="#e6f7ff").pack(pady=5)
        entry_order = Entry(frame_glouton, width=50)
        entry_order.pack(pady=5)

        Button(
            frame_glouton,
            text="Appliquer l'algorithme glouton",
            font=button_font,
            bg="#0073e6",
            fg="white",
            command=lambda: self.controller.appliquer_algorithme_glouton(
                entry_graphe.get(), entry_order.get()
            )
        ).pack(pady=10)
        
        

        # ===================
        # Welsh-Powell
        # ===================
        frame_welsh_powell = tk.Frame(scrollable_frame, bg="#e6f7ff", relief="groove", bd=2, padx=10, pady=10)
        frame_welsh_powell.pack(fill="x", padx=10, pady=10)

        Label(frame_welsh_powell, text="Welsh-Powell", font=section_font, bg="#e6f7ff").pack(pady=5)

        Label(frame_welsh_powell, text="Matrice d'adjacence :", bg="#e6f7ff").pack(pady=5)
        entry_graphe_welsh = Entry(frame_welsh_powell, width=50)
        entry_graphe_welsh.pack(pady=5)

        Button(
            frame_welsh_powell,
            text="Appliquer Welsh-Powell",
            font=button_font,
            bg="#0073e6",
            fg="white",
            command=lambda: self.controller.appliquer_welsh_powell(entry_graphe_welsh.get())
        ).pack(pady=10)

        # ===================
        # Bouton de fermeture
        # ===================
        Button(
            scrollable_frame,
            text="Fermer",
            font=button_font,
            bg="#e67300",
            fg="white",
            command=window.destroy
        ).pack(pady=20)

    def afficher_resultat(self, resultat):
        """Affiche un résultat dans la zone de texte des résultats."""
        self.text_result.configure(state="normal")
        self.text_result.delete(1.0, "end")
        self.text_result.insert("end", resultat)
        self.text_result.configure(state="disabled")


class Partie4View:
    
    def __init__(self, controller):
        self.controller = controller

    def center_window(self, window, width, height):
        """Centre une fenêtre Toplevel sur l'écran."""
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def display(self):
        """Affiche la fenêtre principale pour la Partie 4."""
        window = Toplevel()
        window.title("Partie 4 : Algorithme de Wigderson")
        window.geometry("600x800")

        # Cadre principal pour le contenu scrollable
        main_frame = tk.Frame(window)
        main_frame.pack(fill="both", expand=True)

        # Canvas pour le défilement
        canvas = tk.Canvas(main_frame, bg="#f0f0f0")
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")

        # Configuration du canvas
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Placement du canvas et de la scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        button_font = ("Helvetica", 10)

        # ===================
        # Extraction du Sous-Graphe
        # ===================
        frame_sous_graphe = tk.Frame(scrollable_frame, bg="#e6f7ff", relief="groove", bd=2, padx=10, pady=10)
        frame_sous_graphe.pack(fill="x", padx=10, pady=10)

        Label(frame_sous_graphe, text="Extraction du Sous-Graphe", font=("Helvetica", 12, "bold"), bg="#e6f7ff").pack(pady=5)
        Label(frame_sous_graphe, text="Matrice d'adjacence :", bg="#e6f7ff").pack(pady=5)
        entry_graphe = Entry(frame_sous_graphe, width=50)
        entry_graphe.pack(pady=5)

        Label(frame_sous_graphe, text="Sommets à inclure (ex: [0, 2, 3]) :", bg="#e6f7ff").pack(pady=5)
        entry_sommets = Entry(frame_sous_graphe, width=50)
        entry_sommets.pack(pady=5)

        Button(
            frame_sous_graphe,
            text="Extraire le Sous-Graphe",
            font=("Helvetica", 10),
            bg="#0073e6",
            fg="white",
            command=lambda: self.controller.extraire_sous_graphe(entry_graphe.get(), entry_sommets.get())
        ).pack(pady=10)

        # ===================
        # Zone pour Résultats Généraux
        # ===================
        frame_results = tk.Frame(scrollable_frame, bg="#fbe4d5", relief="groove", bd=2, padx=10, pady=10)
        frame_results.pack(fill="x", padx=10, pady=10)

        Label(frame_results, text="Résultat :", font=("Helvetica", 12, "bold"), bg="#fbe4d5").pack(pady=5)
        self.text_result = tk.Text(frame_results, height=5, width=60, state="disabled", wrap="word", bg="#ffffff")
        self.text_result.pack(pady=10)


        # ===================
        # Voisins et Degré Non Colorés
        # ===================
        frame_voisins_degre = tk.Frame(scrollable_frame, bg="#e6f7ff", relief="groove", bd=2, padx=10, pady=10)
        frame_voisins_degre.pack(fill="x", padx=10, pady=10)

        Label(frame_voisins_degre, text="Voisins et degré non coloriés", font=("Helvetica", 12, "bold"), bg="#e6f7ff").pack(pady=5)
        Label(frame_voisins_degre, text="Matrice d'adjacence :", bg="#e6f7ff").pack(pady=5)
        entry_graphe_voisins = Entry(frame_voisins_degre, width=50)
        entry_graphe_voisins.pack(pady=5)

        Label(frame_voisins_degre, text="Étiquetage :", bg="#e6f7ff").pack(pady=5)
        entry_etiq_voisins = Entry(frame_voisins_degre, width=50)
        entry_etiq_voisins.pack(pady=5)

        Label(frame_voisins_degre, text="Sommet :", bg="#e6f7ff").pack(pady=5)
        entry_sommet_voisins = Entry(frame_voisins_degre, width=10)
        entry_sommet_voisins.pack(pady=5)

        Button(
            frame_voisins_degre,
            text="Afficher les résultats",
            font=button_font,
            bg="#0073e6",
            fg="white",
            command=lambda: self.controller.afficher_voisins_degre(
                entry_graphe_voisins.get(),
                entry_etiq_voisins.get(),
                entry_sommet_voisins.get()
            )
        ).pack(pady=10)

        # ===================
        # Sommets Non Colorés
        # ===================
        frame_non_colories = tk.Frame(scrollable_frame, bg="#e6f7ff", relief="groove", bd=2, padx=10, pady=10)
        frame_non_colories.pack(fill="x", padx=10, pady=10)

        Label(frame_non_colories, text="Sommets Non Colorés", font=("Helvetica", 12, "bold"), bg="#e6f7ff").pack(pady=5)
        Label(frame_non_colories, text="Matrice d'adjacence :", bg="#e6f7ff").pack(pady=5)
        entry_graphe_non_colories = Entry(frame_non_colories, width=50)
        entry_graphe_non_colories.pack(pady=5)

        Label(frame_non_colories, text="Étiquetage :", bg="#e6f7ff").pack(pady=5)
        entry_etiq_non_colories = Entry(frame_non_colories, width=50)
        entry_etiq_non_colories.pack(pady=5)

        Button(
            frame_non_colories,
            text="Afficher les sommets non coloriés",
            font=button_font,
            bg="#0073e6",
            fg="white",
            command=lambda: self.controller.afficher_non_colories(
                entry_graphe_non_colories.get(),
                entry_etiq_non_colories.get()
            )
        ).pack(pady=10)

        # ===================
        # Algorithme de Wigderson
        # ===================
        frame_wigderson = tk.Frame(scrollable_frame, bg="#e6f7ff", relief="groove", bd=2, padx=10, pady=10)
        frame_wigderson.pack(fill="x", padx=10, pady=10)

        Label(frame_wigderson, text="Algorithme de Wigderson", font=("Helvetica", 12, "bold"), bg="#e6f7ff").pack(pady=5)
        Label(frame_wigderson, text="Matrice d'adjacence :", bg="#e6f7ff").pack(pady=5)

        # Déclaration explicite de l'entrée
        self.entry_graphe_wigderson = Entry(frame_wigderson, width=50)
        self.entry_graphe_wigderson.pack(pady=5)
        Button(
            frame_wigderson,
            text="Appliquer l'algorithme de Wigderson",
            bg="#0073e6",
            fg="white",
            command=lambda: self.controller.afficher_resultat_wigderson(self.entry_graphe_wigderson.get())
        ).pack(pady=10)

        # Ajouter le bouton dans la section Wigderson
        Button(
            frame_wigderson,
            text="Afficher le graphe colorié",
            font=button_font,
            bg="#0073e6",
            fg="white",
            command=lambda: self.controller.afficher_graphe_colorie(self.entry_graphe_wigderson.get())
        ).pack(pady=10)

        # ===================
        # Bouton de Fermeture
        # ===================
        Button(
            scrollable_frame,
            text="Fermer",
            font=button_font,
            bg="#e67300",
            fg="white",
            command=window.destroy
        ).pack(pady=20)


    def afficher_resultat_sous_graphe(self, resultat):
        """Affiche le résultat du sous-graphe dans la zone de texte."""
        self.text_result.configure(state="normal")
        self.text_result.delete(1.0, "end")
        if isinstance(resultat, list):  # Si le résultat est une matrice
            resultat_str = "[\n"
            for row in resultat:
                resultat_str += "    [" + ", ".join(["True" if cell else "False" for cell in row]) + "],\n"
            resultat_str = resultat_str.rstrip(",\n") + "\n]"
            self.text_result.insert("end", resultat_str)
        else:  # Sinon, afficher l'erreur ou le message brut
            self.text_result.insert("end", resultat)
        self.text_result.configure(state="disabled")
    
    