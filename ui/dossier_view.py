from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from logic.models import AppState

class DossierView(QWidget):
    """Vue de gestion des dossiers."""
    def __init__(self, state: AppState):
        super().__init__()
        self.state = state
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Dossier"))