import tkinter as tk
from tkinter import ttk
from config.settings import GUI_SETTINGS
from gui.dialogs import (BellmanFordDialog, WelshPowellDialog, DijkstraDialog, KruskalDialog,
                        FordFulkersonDialog, PotentielMetraDialog,
                        TransportDialog)

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title(GUI_SETTINGS['WINDOW_TITLE'])
        self.root.geometry(GUI_SETTINGS['WINDOW_SIZE'])
        self.root.config(bg=GUI_SETTINGS['BACKGROUND_COLOR'])
        self.create_main_frame()

    def create_main_frame(self):
        # Efface d'abord tous les widgets existants
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Navbar
        navbar = tk.Frame(
            self.root,
            bg=GUI_SETTINGS['FRAME_COLOR'],
            height=50
        )
        navbar.pack(side="top", fill="x")

        logo = tk.PhotoImage(file="C:/RO/logo.png")
        logo = logo.subsample(2, 2)
        logo_label = tk.Label(navbar, image=logo, bg=GUI_SETTINGS['FRAME_COLOR'])
        logo_label.image = logo
        logo_label.pack(side="left", padx=10, pady=5)

        noms_frame = tk.Frame(navbar, bg=GUI_SETTINGS['FRAME_COLOR'])
        noms_frame.pack(side="right", padx=10, pady=5)

        encadrant_label = tk.Label(
            noms_frame,
            text="Encadrante : Dr. EL MKHALET Mouna",
            font=GUI_SETTINGS['SUBTITLE_FONT'],
            fg="black",
            bg=GUI_SETTINGS['FRAME_COLOR']
        )
        encadrant_label.pack(anchor="e")

        nom_label = tk.Label(
            noms_frame,
            text="Réalisé par : OUFARES Houda",
            font=GUI_SETTINGS['SUBTITLE_FONT'],
            fg="black",
            bg=GUI_SETTINGS['FRAME_COLOR']
        )
        nom_label.pack(anchor="e")

        title = tk.Label(
            self.root,
            text="Interface Graphique Tkinter GUI",
            font=GUI_SETTINGS['TITLE_FONT'],
            fg="#8B0000",
            bg=GUI_SETTINGS['BACKGROUND_COLOR']
        )
        title.pack(pady=20)

        frame = tk.Frame(
            self.root,
            bg=GUI_SETTINGS['FRAME_COLOR'],
            bd=3,
            relief="solid"
        )
        frame.pack(pady=20, padx=50)

        subtitle = tk.Label(
            frame,
            text="Algorithmes de Recherche Opérationnelle",
            font=GUI_SETTINGS['SUBTITLE_FONT'],
            fg="black",
            bg="#FFC0CB"
        )
        subtitle.pack(pady=10, padx=20)

        button_frame = tk.Frame(frame, bg="#FFC0CB")
        button_frame.pack(pady=20)

        btn_entree = tk.Button(
            button_frame,
            text="Entrée",
            font=GUI_SETTINGS['BUTTON_FONT'],
            bg=GUI_SETTINGS['BUTTON_COLOR'],
            fg="black",
            width=15,
            height=2,
            relief="groove",
            command=self.afficher_algorithmes
        )
        btn_entree.grid(row=0, column=0, padx=10)

        btn_sortie = tk.Button(
            button_frame,
            text="Sortie",
            font=GUI_SETTINGS['BUTTON_FONT'],
            bg=GUI_SETTINGS['BUTTON_COLOR'],
            fg="black",
            width=15,
            height=2,
            relief="groove",
            command=self.root.quit
        )
        btn_sortie.grid(row=0, column=1, padx=10)

    def afficher_algorithmes(self):
        # Efface tous les widgets existants
        for widget in self.root.winfo_children():
            widget.destroy()

        # Titre principal
        title = tk.Label(
            self.root,
            text="Liste des Algorithmes",
            font=GUI_SETTINGS['TITLE_FONT'],
            fg="#8B0000",
            bg=GUI_SETTINGS['BACKGROUND_COLOR']
        )
        title.pack(pady=20)

        # Cadre pour les boutons des algorithmes
        frame_algos = tk.Frame(
            self.root,
            bg=GUI_SETTINGS['FRAME_COLOR'],
            bd=3,
            relief="solid"
        )
        frame_algos.pack(pady=20, padx=50)

        algorithmes = {
            "Welsh Powell": lambda: WelshPowellDialog(self.root),
            "Dijkstra": lambda: DijkstraDialog(self.root),
            "Kruskal": lambda: KruskalDialog(self.root),
            "Bellman ford": lambda: BellmanFordDialog(self.root),
            "Ford Fulkerson": lambda: FordFulkersonDialog(self.root),
            "Potentiel METRA": lambda: PotentielMetraDialog(self.root),
            "Nord-Ouest": lambda: TransportDialog(self.root, "nord_ouest"),
            "Moindre Coût": lambda: TransportDialog(self.root, "moindre_cout"),
            "Stepping-Stone": lambda: TransportDialog(self.root, "stepping_stone")
        }

        # Ajouter les boutons dans une grille
        for i, (algo, command) in enumerate(algorithmes.items()):
            btn_algo = tk.Button(
                frame_algos,
                text=algo,
                font=GUI_SETTINGS['BUTTON_FONT'],
                bg=GUI_SETTINGS['BUTTON_COLOR'],
                fg="teal",
                width=20,
                height=2,
                relief="groove",
                command=command
            )
            btn_algo.grid(row=i//3, column=i%3, padx=10, pady=10)

        # Ajout du bouton Retour
        btn_retour = tk.Button(
            self.root,
            text="Retour",
            font=GUI_SETTINGS['BUTTON_FONT'],
            bg=GUI_SETTINGS['BUTTON_COLOR'],
            fg="black",
            width=15,
            height=2,
            relief="groove",
            command=self.create_main_frame
        )
        btn_retour.pack(pady=20)