# 🧮 Valuexpert – Logiciel d’expertise immobilière

**Valuexpert** est une application de bureau professionnelle développée en Python.  
Elle permet aux experts immobiliers de réaliser des **expertises en valeur vénale** grâce à des méthodes complètes, personnalisables, et rigoureuses.  
L’application fonctionne **hors-ligne**, est **exécutable localement**, et propose une **interface 100 % en français**.

---

## 🎯 Objectifs du projet

- Créer un **logiciel autonome et modulable** pour les expertises en valeur vénale
- Fournir plusieurs **méthodes de calcul professionnelles**
- Générer des **rapports PDF clairs et personnalisables**
- Permettre une utilisation simple ou experte (formulaires adaptatifs)
- Prévoir un système de **comptes, licences, et accès** pour une future commercialisation
- Intégrer des données du marché (via API) et des suggestions IA dans les versions futures

---

## 🧱 Technologies utilisées

| Composant             | Technologie                         |
|------------------------|-------------------------------------|
| Interface Graphique    | Python + PyQt5                      |
| PDF                    | ReportLab                           |
| Stockage local         | JSON ou SQLite                      |
| Authentification Cloud | Firebase (future intégration)       |
| IA & automatisation    | (prévu via modèles locaux + prompts) |

---

## 🧩 Méthodes d’évaluation prévues

Chaque méthode est modulaire, personnalisable, et accessible depuis l’interface.  
Elles sont intégrées dans des fichiers séparés dans le dossier `logic/`.

| Méthode                                 | Description |
|-----------------------------------------|-------------|
| ✅ Méthode comparative simple            | Moyenne pondérée de biens similaires |
| ✅ Régression statistique                | Estimation via modèle de régression multivariée |
| ✅ Méthode hédoniste                     | Analyse fine via critères qualitatifs et quantitatifs |
| ✅ Capitalisation du revenu              | Valeur via rendement locatif net |
| ✅ Sol + construction – vétusté          | Estimation terrain + reconstruction – vétusté |
| ✅ Bilan promoteur inversé               | Valorisation en coût de revient promotionnel |
| ✅ Discounted Cash-Flow (DCF)            | Actualisation de flux nets futurs |

---

## 🖥️ Interface utilisateur (UI)

- Interface en **français uniquement**
- Barre de navigation verticale : Accueil / Nouveau dossier / Méthodes / Rapport PDF / Mon compte
- Navigation dynamique via `QStackedWidget`
- Modes d’affichage : **simplifié** ou **expert** selon le niveau d'utilisateur
- Design sobre, clair, avec une option de thème sombre/claire (à venir)

---

## 📁 Structure du projet

```text
valuexpert/
├── main.py                        # Point d’entrée
├── ui/                            # Interface graphique
│   ├── main_window.py
│   ├── accueil_view.py
│   ├── dossier_view.py
│   ├── methodes_view.py
│   ├── rapport_view.py
│   └── compte_view.py
├── logic/                         # Méthodes de calcul
│   ├── comparative.py
│   ├── revenu.py
│   ├── dcf.py
│   └── ...
├── pdf/                           # Génération des rapports
│   └── exporter.py
├── auth/                          # Connexion / licences (future version)
│   └── firebase_auth.py
├── data/                          # Stockage local
│   └── storage.py
├── assets/                        # Logos, modèles PDF, icônes
├── requirements.txt               # Dépendances
├── .gitignore                     # Fichiers ignorés par Git
└── README.md                      # Documentation du projet



---

## 📄 Rapports PDF

- Générés automatiquement selon les données saisies
- Personnalisables (logo, mentions légales, structure du rapport)
- Format professionnel, prêt à être utilisé dans un cadre légal
- Intégration de graphiques, tableaux, observations, signatures

---

## 🔐 Fonctionnalités à venir (version commerciale)

- 🔑 Système de **licence et activation**
- 👤 Connexion utilisateur via Firebase
- 🔄 Sauvegarde cloud des expertises (Firestore)
- 📤 Synchronisation entre appareils
- 💼 Différents niveaux d’accès (Gratuit, Pro, Cabinet)
- 🤖 Suggestions IA (comparables, rédaction automatique, scoring)

---

## 🚀 Lancement de l’application

1. Crée un environnement virtuel Python :
   ```bash
   python -m venv env
   env\Scripts\activate       # Windows
   source env/bin/activate    # macOS/Linux

2. Installe les dépendances :

    pip install -r requirements.txt

3. Lance l'application : 

    python main.py


📅 Roadmap

X Définition du projet

X Création de l’architecture de base

X Génération automatique de la structure par script

 Interface graphique complète (toutes vues)

 Intégration de chaque méthode de calcul

 Génération de PDF dynamique

 Intégration Firebase (auth + sync)

 Commercialisation (licence, compte, clé d’accès)

 Version Web (optionnel)




 🧑‍💼 Auteur

Développé avec passion par Franck Croisic / Coconut971,
à destination des professionnels de l’immobilier.


Ce projet est en cours de développement actif.