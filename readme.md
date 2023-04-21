
# Projet 7 : Résolvez des problèmes en utilisant des algorithmes en Python 

*Ce projet à pour but la manipulation, la compréhension des mécanismes de constructions des algorithmes ainsi que l'importance de la notion de complexité*

## Mise en situation: 

<img align="left" width="100" height="100" src="data/algo&trade.png">AlgoInvest&Trade, doit fournir à ses clients, pour un montant d’investissement donné, le meilleur choix d’actions, en fonction de leur rentabilité en % sur deux ans. 

  Un Algorithme de **Brute-Force** est demandé sur un jeu de **20 actions**. Puis un algorithme **optimisé** sur 2 jeux de **1000 actions**.

*Un jeu résultats sur les set 1000 actions, est communiqué par l'entreprise, afin d'effectuer une comparaison vis à vis de notre algorithme optimisé*
    
## Mise en place du projet: 

Pré-requis: se placer depuis le terminal dans le dossier où l'on exécute le script:

Avant toute chose on clone le répository git:

    git clone https://github.com/LGD-P/P7_Open_C.git

Une fois le projet cloné on crée et on active l'environnement virtuel:

    python3 -m venv env

suivi de:

    source env/bin/activate
  

Puis on lance l'installation des modules nécessaires au fonctionnement du script:

    pip install -r requirements.txt


Il n'y a plus qu'à exécuter les script:

    python3 brutefoce.py    "exécutera l'algo de brute force sur le set de 20 actions contenu dans le dossier data"

    python3 optimized.py    "exécutera l'algo optimisé dit glouton, sur les set de 1000 actions." 


## Le dossier "analyse" contient:
*  Un pdf traitant des algorithmes en général.
*  De ceux utilisés dans le cadre de ce projet.
*  Une analyse comparative des résultats obtenus.