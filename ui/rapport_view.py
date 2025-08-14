from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from logic.models import AppState

class RapportView(QWidget):
    """Vue de génération du rapport PDF."""
    def __init__(self, state: AppState):
        super().__init__()
        self.state = state
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Rapport PDF"))