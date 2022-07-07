# CHANGELOG

## v0.0.1

- Acquisition d'un fichier test "Queen_Eliz_II"
- Acquisition de la librairie python-gedcom (https://pypi.org/project/python-gedcom/) pour le parsing du fichier GEDCOM

## v0.0.2

- Découverte de l'arbre généalogique et exploration des fonctionnalités python-gedcom
- Formalisation mathématique du problème et analyse de base de ce dernier
- Modélisation de l'arbre pour répondre au problème posé :
  - tentative n°1 : échec de la modélisation pour satisfaire les conditions du problème posé
  - tentative n°2 : pas de contrindication des conditions du problème

## v0.0.3

- Ajout d'un fichier "tree_builder.py" dont le but est de construire l'arbre sous forme de graphe pour pouvoir 
réaliser les calculs de relations.
- Définition d'une stratégie d'écriture du code, et de la structure pour former le graphe.

## v0.1.0 (01/06)

- Choix de la base de données sous la forme d'un dictionnaire de dictionnaires {'ID1' :
{'name' : ..., 'parent_1' : ..., ...}, 'ID2' : {}, ...}
- Création progressive de la base de données à partir du fichier GedCom
- Création de l'algorithme de parcours *basique* du graphe : trouve l'ancêtre commun et donne la 
longueur des liens directs seulement pour le moment

## v1.0.0 (09/06)

- Implémentation d'un algorithme de transcription de la base de donnée GEDCOM en fichier .json (base de donnée 
"homemade") plus faciliment lisible contenant l'ensemble des données du fichier GEDCOM
- Implémentation d'un algorithme de transcription de la base de donnée 'homemade' en base de donnée 'calculus' sous
format .json pour le calcul
- Implémentation de l'algorithme de calcul de Dijkstra pour calculer le plus court chemin entre deux individus
de la base de donnée

## v1.1.0 (12/06)

- Séparation de l'analyseur d'arbre pour compléter les liens de la base de donnée de l'algorithme
de création de la base de donnée
- Implémentation de l'analyse de l'arbre pour ajouter les liens de grand-parents, petits enfants, oncles et tantes
- Implémentation d'un algorithme donnant le lien sémantique entre les deux individus à partir des résultats obtenus par l'algorithme de Dijkstra

## v1.2.0 (15/06)

- Création d'un fichier gedcom "maison" simplifié (5 générations) permettant de tester l'algorithme et s'assurer de sa fiabilité
- Création d'un visualisateur de l'arbre à l'aide d'un module graphique afin que l'utilisateur puisse avoir une représentation claire de l'arbre généalogique
- Création d'un algorithme indépendant ("photo_occurences") qui ajoute la possibilité dans le logiciel d'identifier des individus sur des photos et de modifier ainsi leur lien. Plus ils apparaissent ensemble sur de nombreuses photos plus leurs liens sont forts.
- Essai de prise en compte d'une potentielle consanguinité dans l'algorithme déterminant les relations secondaires

## v1.2.1 (17/06)

- Ajout sur le visualisateur de l'arbre le lien privilégié entre deux individus trouvé par notre algorithme. Il s'affiche alors en rouge afin de permettre à l'utilisateur de remonter clairement ce lien
- Affinage du calcul de la relation entre deux personnes identifées sur une photographie dans "photo_occurences"