#  Projet Rush Hour Solver – BFS & A*

# Description du projet
Ce projet implémente une **intelligence artificielle** capable de résoudre le célèbre puzzle **Rush Hour**, où le but est de libérer la voiture rouge ("X") bloquée par d’autres véhicules, en la faisant sortir du plateau.

Deux approches principales ont été implémentées :
- 🔹 **BFS (Breadth-First Search)** : recherche exhaustive en largeur.
- 🔹 **A\*** : algorithme de recherche informée utilisant des heuristiques.

Une interface graphique simple avec **Pygame** permet également de visualiser le plateau.

---

# Objectifs
- Représenter un plateau de Rush Hour à partir d’un fichier CSV.  
- Explorer les états possibles à l’aide de **BFS** et **A\***.  
- Comparer les performances des heuristiques.  
- Visualiser la solution étape par étape.

---

# Structure du projet

RushHourGame/
│
├── main.py # Fichier principal : exécution des algorithmes
├── rush_hour.py # Représentation du plateau et gestion des véhicules
├── node.py # Structure du nœud (état, parent, coût, etc.)
├── BFS.py # Implémentation de l’algorithme BFS
├── a.py # Implémentation de l’algorithme A* + heuristiques
├── ui.py # Interface graphique avec Pygame
├── examples/
│ └── 1.csv # Exemple de plateau de jeu
└── .gitignore # Fichiers à ignorer par Git

h1 : Distance du véhicule rouge à la sortie

Mesure le nombre de cases restantes avant que la voiture "X" atteigne la sortie.

h2 : Distance + blocages

h1 + le nombre de véhicules bloquant le passage vers la sortie.

h3 : Heuristique personnalisée

**Combine :**

la distance à la sortie (h1),

le nombre de véhicules bloquants (h2),

et le nombre de mouvements nécessaires pour dégager ces véhicules (pondéré).
