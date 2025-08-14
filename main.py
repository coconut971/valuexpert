"""Application Valuexpert.

Ce module initialise la fenêtre principale de l'application avec une
barre de navigation verticale et un QStackedWidget central pour afficher
les différentes vues.
"""

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QStackedWidget,
)
from PyQt5.QtCore import Qt, QCoreApplication

from logic.models import AppState

# Importation des vues
from ui.accueil_view import AccueilView
from ui.dossier_view import DossierView
from ui.methodes_view import MethodesView
from ui.rapport_view import RapportView
from ui.compte_view import CompteView


QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)


class FenetrePrincipale(QMainWindow):
    """Fenêtre principale de l'application."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Valuexpert – Logiciel d'expertise immobilière")
        self.resize(1200, 800)

        # Création de l'état partagé de l'application
        self.state = AppState(
            utilisateur=None, expertise_courante=None, dossiers={}
        )

        # Création du widget central et de son agencement horizontal
        widget_central = QWidget()
        agencement_horizontal = QHBoxLayout(widget_central)
        agencement_horizontal.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(widget_central)

        # --- Barre de navigation latérale ---
        self.barre_laterale = QWidget()
        self.barre_laterale.setObjectName("barreLaterale")
        self.barre_laterale.setFixedWidth(220)
        layout_barre = QVBoxLayout(self.barre_laterale)
        layout_barre.setContentsMargins(0, 0, 0, 0)
        layout_barre.setSpacing(0)

        # Liste des boutons et de leurs titres
        boutons = [
            ("Accueil", lambda: self.pages.setCurrentIndex(0)),
            ("Dossier", lambda: self.pages.setCurrentIndex(1)),
            ("Méthodes", lambda: self.pages.setCurrentIndex(2)),
            ("Rapport PDF", lambda: self.pages.setCurrentIndex(3)),
            ("Mon Compte", lambda: self.pages.setCurrentIndex(4)),
        ]

        for texte, action in boutons:
            bouton = QPushButton(texte)
            bouton.setObjectName("boutonBarre")
            bouton.setFixedHeight(40)
            bouton.clicked.connect(action)
            layout_barre.addWidget(bouton)

        layout_barre.addStretch()

        # --- Zone centrale avec QStackedWidget ---
        self.pages = QStackedWidget()
        self.pages.addWidget(AccueilView(self.state))
        self.pages.addWidget(DossierView(self.state))
        self.pages.addWidget(MethodesView(self.state))
        self.pages.addWidget(RapportView(self.state))
        self.pages.addWidget(CompteView(self.state))

        # Ajout des widgets à l'agencement principal
        agencement_horizontal.addWidget(self.barre_laterale)
        agencement_horizontal.addWidget(self.pages, 1)

        # --- Barre de statut ---
        self.statusBar().showMessage("Prêt")

        # --- Feuille de style externe ---
        try:
            with open("assets/style.qss", "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            pass


def lancer_application() -> None:
    """Point d'entrée de l'application."""
    application = QApplication(sys.argv)
    fenetre = FenetrePrincipale()
    fenetre.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    lancer_application()