# Gestionnaire de Tâches (Architecture MVC)

Ce projet est une application CLI (interface en ligne de commande) simple pour la gestion des tâches, implémentée en utilisant l'architecture MVC (Modèle-Vue-Contrôleur).

## Fonctionnalités

- Ajouter une nouvelle tâche.
- Afficher toutes les tâches avec leur statut (complété ou non).
- Mettre à jour le statut d'une tâche (compléter ou marquer comme incomplète).

## Structure du Projet

- **Modèle** : Gestion des données des tâches (fichier `tasks.py`).
- **Vue** : Interface utilisateur pour l'affichage et la saisie des entrées (fichier `task_view.py`).
- **Contrôleur** : Logique de gestion et interaction entre le modèle et la vue (fichier `task_controller.py`).

## Utilisation

1. Clonez le répertoire du projet.
2. Exécutez le fichier `main.py` :

   ```bash
   python main.py
   ```

3. Suivez les instructions affichées pour ajouter, afficher ou mettre à jour les tâches.

## Exemple d'Exécution

```text
1. Ajouter une tâche ?
2. Afficher les tâches ?
3. Mettre à jour les tâches ?
4. Quitter le programme ?

Choix : 1
Quel est le nom de la tâche à créer ? Apprendre Python
"Apprendre Python" ajoutée.
```
