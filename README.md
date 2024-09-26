# Rogue Guess

## Introduction

Ce projet est une application web qui propose plusieurs fonctionnalités relatives au matériel d'une école.
Elle permet entre autre de réserver du matériel pour un élève, de suggérer l'achat d'un matériel à l'administration, ou de signaler un problème au sujet d'un matériel défectueux.
Elle permet aux administrateurs de gérer les tickets de signalement, de juger les suggestions et de voir les matériels réservés.

## Fonctionnalités

Utilisateur

- Réserver un matériel
- Signaler un problème
- Suggérer un achat
- Aimer une suggestion
- Voir les derniers problèmes signalés

Administrateur

- Voir les objets réservés ainsi que l'élève concerné
- Voir les problèmes suggérés et les gérer
- Gérer les suggestions d'achats
- Gérer le stock du matériel

## Installation

- Clonez le dépôt
  git clone https://github.com/YoussefSNK/Epsi-Matos.git

- Installez les dépendances
  ???

- Démarrer le serveur

```bash
  python __init__.py
```

## Utilisation

Voir les derniers signalements

- Depuis la page de connexion, connectez-vous avec votre adresse epsi (théoriquement)
- Vous serez ensuite redirigez à l'accueil et verrez les signalements sur votre gauche
- Utilisez la barre de recherche pour mettre le nom d'une salle et voir les problèmes relatifs à la salle

Signaler un problème

- Depuis la page d'accueil, cliquez sur "Signaler du matériel défaillant"
- Renseignez la salle possédant le matériel défectueux
- Renseignez le type du matériel
- Décrivez le problème si nécessaire et envoyez le formulaire

Réserver du matériel

- Depuis la page d'accueil, cliquez sur "Réserver du matériel"
- Sélectionnez le jour de votre réservation
- Sélectionnez le matériel que vous souhaitez emprunter
- Appuyez sur le bouton "Valider" pour confirmer votre emprunt

Suggestion de matériel

- Depuis la page d'accueil, cliquez sur "Suggestion de matériel"
- Renseignez le nom du matériel que vous souhaitez suggérer
- Indiquez le nombre de stock qui serait nécessaire
- Inscrivez la description du matériel ainsi qu'un éventuel lien avec une fiche produit
- Envoyer le formulaire pour valider votre suggestion

Outils utilisés

- Outil de versionning : Github
- Commits conventionnels
- Outil de gestion de ticket : Trello

Auteurs

- [Youssef](https://github.com/YoussefSNK)
- [Sandra](https://github.com/ssndrss)
- [Martin](https://github.com/Nawaank)
- [Martin²](https://github.com/Martin1335)
- [Lina](https://github.com/linnaa-a)
