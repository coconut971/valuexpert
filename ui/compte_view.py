from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from logic.models import AppState


class CompteView(QWidget):
    """Vue des informations du compte utilisateur."""
    def __init__(self, state: AppState):
        super().__init__()
        self.state = state
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Mon Compte"))