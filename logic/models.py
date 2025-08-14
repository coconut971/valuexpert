"""Modèles de données de l'application Valuexpert.

Ce module définit les structures de données principales utilisées pour
partager l'état de l'application entre les différentes vues. Les
classes sont sérialisables grâce aux méthodes ``to_dict`` et
``from_dict``.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List


@dataclass
class BienImmobilier:
    """Informations sur un bien immobilier."""

    adresse: str
    surface_habitable: float
    surface_terrain: float | None
    type_bien: str
    annee_construction: int | None
    notes: str = ""

    def to_dict(self) -> dict:
        """Retourne une représentation dictionnaire du bien."""
        return {
            "adresse": self.adresse,
            "surface_habitable": self.surface_habitable,
            "surface_terrain": self.surface_terrain,
            "type_bien": self.type_bien,
            "annee_construction": self.annee_construction,
            "notes": self.notes,
        }

    @staticmethod
    def from_dict(d: dict) -> "BienImmobilier":
        """Crée une instance de ``BienImmobilier`` depuis un dictionnaire."""
        return BienImmobilier(
            adresse=d["adresse"],
            surface_habitable=d["surface_habitable"],
            surface_terrain=d.get("surface_terrain"),
            type_bien=d["type_bien"],
            annee_construction=d.get("annee_construction"),
            notes=d.get("notes", ""),
        )


@dataclass
class Expertise:
    """Représente une expertise immobilière."""

    id: str
    bien: BienImmobilier | None
    methodes_selectionnees: List[str]
    resultats: Dict[str, float]
    date_creation: datetime

    def to_dict(self) -> dict:
        """Retourne une représentation dictionnaire de l'expertise."""
        return {
            "id": self.id,
            "bien": self.bien.to_dict() if self.bien else None,
            "methodes_selectionnees": list(self.methodes_selectionnees),
            "resultats": dict(self.resultats),
            "date_creation": self.date_creation.isoformat(),
        }

    @staticmethod
    def from_dict(d: dict) -> "Expertise":
        """Crée une ``Expertise`` à partir d'un dictionnaire."""
        return Expertise(
            id=d["id"],
            bien=BienImmobilier.from_dict(d["bien"]) if d.get("bien") else None,
            methodes_selectionnees=list(d.get("methodes_selectionnees", [])),
            resultats=dict(d.get("resultats", {})),
            date_creation=datetime.fromisoformat(d["date_creation"]),
        )


@dataclass
class AppState:
    """État global de l'application."""

    utilisateur: str | None
    expertise_courante: Expertise | None
    dossiers: Dict[str, Expertise]

    def to_dict(self) -> dict:
        """Retourne une représentation dictionnaire de l'état."""
        return {
            "utilisateur": self.utilisateur,
            "expertise_courante": self.expertise_courante.to_dict()
            if self.expertise_courante
            else None,
            "dossiers": {k: v.to_dict() for k, v in self.dossiers.items()},
        }

    @staticmethod
    def from_dict(d: dict) -> "AppState":
        """Crée un ``AppState`` à partir d'un dictionnaire."""
        return AppState(
            utilisateur=d.get("utilisateur"),
            expertise_courante=Expertise.from_dict(d["expertise_courante"])
            if d.get("expertise_courante")
            else None,
            dossiers={
                k: Expertise.from_dict(v) for k, v in d.get("dossiers", {}).items()
            },
        )