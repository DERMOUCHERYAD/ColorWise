from tkinter import Tk, Button, Label, PhotoImage, Frame
from controller import Partie1Controller, Partie2Controller, Partie3Controller, Partie4Controller
from view import Partie1View, Partie2View, Partie3View, Partie4View

def main():
    # Initialiser la fenêtre principale
    root = Tk()
    root.title("ColorWise")  # Titre de la fenêtre
    root.geometry("800x600")  # Taille initiale
    root.configure(bg="#f0f0f0")  # Couleur de fond

    # =======================
    # En-tête avec logo et titre
    # =======================
    header_frame = Frame(root, bg="#f0f0f0", pady=10)
    header_frame.pack(fill="x")

    # Cadre pour le logo et le texte côte à côte
    logo_text_frame = Frame(header_frame, bg="#f0f0f0")
    logo_text_frame.pack()

    try:
        # Charger et redimensionner le logo
        logo = PhotoImage(file="resources/logo.png")
        resized_logo = logo.subsample(3, 3)  # Ajuste la taille du logo
        logo_label = Label(logo_text_frame, image=resized_logo, bg="#f0f0f0")
        logo_label.grid(row=0, column=0, padx=10)
    except:
        resized_logo = None

    # Texte à côté ou sous le logo
    Label(
        logo_text_frame,
        text=" ColorWise",
        font=("Helvetica", 24, "bold"),
        bg="#f0f0f0",
        fg="#333",
    ).grid(row=0, column=1, sticky="w")

    # Sous-titre
    Label(
        header_frame,
        text="Explorez les couleurs des graphes et l'élégance des algorithmes de coloriage.",
        font=("Helvetica", 14),
        bg="#f0f0f0",
        fg="#555",
    ).pack(pady=10)

    # =======================
    # Section des boutons
    # =======================
    button_frame = Frame(root, bg="#ffffff", padx=20, pady=20, relief="groove", bd=2)
    button_frame.pack(fill="both", expand=True, padx=40, pady=20)

    button_font = ("Helvetica", 12)

    # Initialiser les contrôleurs et les vues
    controller_partie1 = Partie1Controller()
    view_partie1 = Partie1View(controller_partie1)
    controller_partie1.view = view_partie1

    controller_partie2 = Partie2Controller()
    view_partie2 = Partie2View(controller_partie2)
    controller_partie2.view = view_partie2

    controller_partie3 = Partie3Controller()
    view_partie3 = Partie3View(controller_partie3)
    controller_partie3.view = view_partie3

    controller_partie4 = Partie4Controller()
    view_partie4 = Partie4View(controller_partie4)
    controller_partie4.view = view_partie4

    # Boutons liés aux vues respectives
    Button(
        button_frame,
        text="Partie 1 : Coloriage Basique",
        font=button_font,
        bg="#0073e6",
        fg="white",
        command=view_partie1.display,
    ).pack(fill="x", pady=10)

    Button(
        button_frame,
        text="Partie 2 : 2-coloriabilité",
        font=button_font,
        bg="#4caf50",
        fg="white",
        command=view_partie2.display,
    ).pack(fill="x", pady=10)

    Button(
        button_frame,
        text="Partie 3 : Algorithme Glouton",
        font=button_font,
        bg="#e67e22",
        fg="white",
        command=view_partie3.display,
    ).pack(fill="x", pady=10)

    Button(
        button_frame,
        text="Partie 4 : Algorithme de Wigderson",
        font=button_font,
        bg="#e74c3c",
        fg="white",
        command=view_partie4.display,
    ).pack(fill="x", pady=10)

    # Bouton Quitter
    Button(
        button_frame,
        text="Quitter",
        font=button_font,
        bg="#ADD8E6",  # Bleu clair pastel
        fg="black",  
        command=root.quit,
    ).pack(fill="x", pady=20)

    # =======================
    # Pied de page
    # =======================
    footer_frame = Frame(root, bg="#f0f0f0", pady=10)
    footer_frame.pack(fill="x", side="bottom")

    Label(
        footer_frame,
        text="© 2024 - Réalisé par DERMOUCHE Mohammed Ryad",
        font=("Helvetica", 10),
        bg="#f0f0f0",
        fg="#aaa",
    ).pack()

    # Gérer l'affichage du logo (préserver l'image pour éviter le garbage collector)
    root.resized_logo = resized_logo if resized_logo else None

    # Démarrer la boucle principale
    root.mainloop()

if __name__ == "__main__":
    main()
