import tkinter as tk
from tkinter import Toplevel, Label, Button, Entry, messagebox
from PIL import Image, ImageTk
from view import Partie1View
if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    view = Partie1View(None)  # Aucun contrôleur pour ce test
    coloriage_test = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    view.afficher_graphe_colore(coloriage_test)
    root.mainloop()
