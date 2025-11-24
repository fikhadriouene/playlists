import psycopg
# <!-- 
# # Exercice 11 – Playlist

# ## Objectif

# Créer une application Python utilisant `psycopg` pour gérer les données d’une plateforme de streaming musical. L’application doit permettre de réaliser des opérations CRUD (Créer, Lire, Mettre à jour, Supprimer) sur les tables `utilisateurs`, `chansons` et `playlists`.

# ## 1. Tables utilisées

# L’exercice repose sur les tables suivantes (vous pouvez reprendre la structure depuis l’exercice 4).

# > Remarque : la table `playlists` stocke une association entre **une playlist**, **un utilisateur**, et **une chanson**.
# > Une playlist contenant plusieurs chansons possédera donc plusieurs lignes dans la table `playlists`.

# ### Table `utilisateurs`

# * `id_utilisateur` : identifiant unique (clé primaire)
# * `nom_utilisateur` : texte, obligatoire
# * `email` : texte, unique
# * `date_inscription` : date/heure par défaut actuelle

# ### Table `chansons`

# * `id_chanson` : identifiant unique (clé primaire)
# * `titre` : texte
# * `artiste` : texte
# * `album` : texte
# * `duree` : nombre ou texte
# * `genre` : texte
# * `annee_sortie` : entier

# ### Table `playlists`

# * `id_playlist` : identifiant unique (clé primaire)
# * `nom_playlist` : texte
# * `id_utilisateur` : clé étrangère vers `utilisateurs`
# * `id_chanson` : clé étrangère vers `chansons`
# * `date_creation` : date/heure par défaut actuelle


# ## 2. Fonctions à implémenter

# Pour chacune des tables, l’application doit permettre les opérations CRUD, avec des détails spécifiques selon la table.

# ### 1. Création d’un enregistrement

# #### Utilisateurs







# ### 2. Lecture / recherche

# #### Recherche par ID






        


     



# #### Recherche par champs












  

        













# * Les mises à jour se font à partir de l’ID.

# ---

# ### 4. Suppression d’un enregistrement

# #### Utilisateur

# * Suppression par `id_utilisateur`.
# * La suppression doit entraîner automatiquement la suppression des playlists associées.

# #### Chanson

# * Suppression par `id_chanson`.
# * Si une chanson appartient à une playlist, seules les lignes correspondantes dans `playlists` doivent être supprimées.

# #### Playlist

# * Suppression par `nom_playlist` ou par son ID. -->
