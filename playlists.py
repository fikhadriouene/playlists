import psycopg
DSN = "dbname=postgres user=postgres password=admin host=localhost port=5432"
# #### Playlists

# * Ajouter une playlist avec :

#   * `nom_playlist`
#   * `id_utilisateur` (créateur)
#   * un ou plusieurs `id_chanson`
# * Une playlist contenant plusieurs chansons doit créer plusieurs lignes dans la table `playlists`.

def ajouter_playlist(nom_playlist,id_utilisateur,liste_chansons) :
    try :
        val = ""
        
        for c in liste_chansons :
            val = val + f"({nom_playlist},{id_utilisateur},c),"
        val = val.rstrip(",")
        
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur = conn.cursor()                
                cur.execute(f"insert into utilisateurs(nom_playlist,id_utilisateur) values {val}")
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)


# #### Playlists

# * Ajouter une playlist avec :

#   * `nom_playlist`
#   * `id_utilisateur` (créateur)
#   * un ou plusieurs `id_chanson`
# * Une playlist contenant plusieurs chansons doit créer plusieurs lignes dans la table `playlists`.

def ajouter_playlist(nom_playlist,id_utilisateur,liste_chansons) :
    try :
        val = ""
        
        for c in liste_chansons :
            val = val + f"({nom_playlist},{id_utilisateur},c),"
        val = val.rstrip(",")
        
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur = conn.cursor()                
                cur.execute(f"insert into utilisateurs(nom_playlist,id_utilisateur) values {val}")
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)
# ---


def rechercher_playlist(id) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from playlists where id_playlist = %s ",(id,))
                row = cur.fetchall()
                print(row)
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)


def affiche_playlist(id) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from playlists where id_playlist = %s ",(id,))
                row = cur.fetchall()
                print(row)
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)    


def playlist_par_champs(champs, valeur) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                match champs :
                    case 'nom_playlist' :
                        requete = f"select * from playlists where nom_playlist = %s "
                    case 'nom_utilisateur' :
                        requete = """
                                    select * 
                                    from playlists as p 
                                    join utilisateurs as u
                                    on p.id_utlisateur = 
                                    where nom_utilisateur = %s 
                                  """  
                    case _ :
                        print("erreur champs")
                cur.execute(requete,(valeur,))      
                row = cur.fetchall()         
                print(row)
                
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)


# #### Affichage spécifique pour les playlists

# Lorsqu’une playlist est récupérée, afficher :

# * Le nom de l’utilisateur qui l’a créée.

def createur_playlist(id_playlist) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from utilisateur as u join playlist as p on u.id_utilisateur = p.id_utilisateur where nom_playlist = %s ",(id_playlist,))
                row = cur.fetchall()
                print(row)
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)

# * La liste complète des chansons contenues dans la playlist (titre et artiste)


def createur_playlist(id_playlist) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from chanson as c join playlists as p on c.id_chanson = p.id_chanson where id_playlist = %s ",(id_playlist,))
                row = cur.fetchall()
                print(row)
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)

# * **Playlists** :
#   * modification du nom de la playlist

def modifier_nom_playlist(id_playlist,nom):
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                requete = f"update chanson set nom_playlist = %s where id_playlist=%s "
                cur.execute(requete,(nom,id_playlist))      
                row = cur.fetchall()         
                print(row)
                
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)    