import psycopg
DSN = "dbname=postgres user=admin password=admin host=localhost port=5432"
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
            val = val + f"(\'{nom_playlist}\',{id_utilisateur},{c}),"
        val = val.rstrip(",")
        
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur = conn.cursor()                
                cur.execute(f"insert into playlists(nom_playlist,id_utilisateur,id_chanson) values {val}")
                #print ("insert into utilisateurs(nom_playlist,id_utilisateur) values",val)
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)



def rechercher_playlist(id) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
                cur.execute("select * from playlists where id_playlist = %s ",(id,))
                row = cur.fetchone()
                print(row)
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)


#OK -> rechercher_playlist(22)

def affiche_row(row : dict) :
    print ()
    print (f"------ playslist {row[0]['nom_playlist']} ------- ")
    print(f"taille = {len(row)}")
    for i in range (len(row)) :    
            print (f"titre : ",row[i]['titre'])
            print (f"artiste : ",row[i]['artiste'])
            print (f"album : ",row[i]['album'])
            print (f"genre : ",row[i]['genre'])
            print (f"annee de sortie : ",row[i]['annee_sortie'])
            print (f"------------------------------- ")
            print ()



def affiche_playlist(id) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
                cur.execute("""
                                select * from 
                                playlists p
                                join chansons c
                                on p.id_chanson = c.id_chanson 
                                where nom_playlist = (select nom_playlist from playlists where id_playlist = %s) 
                            """,
                            (id,))
                row = cur.fetchall()
                #print("TYPE : ",type(row).__name__)
                affiche_row(row)
                print("TAILLE DE ROW : ", len(row))
                
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)    

# OK -> affiche_playlist(22)


def playlist_par_champs(champs, valeur) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
                match champs :
                    case 'nom_playlist' :
                        requete = """select * 
                                     from playlists p
                                     join chansons c
                                     on c.id_chanson = p.id_chanson
                                     where nom_playlist = %s 
                                  """
                    case 'nom_utilisateur' :
                        requete = """
                                    select * 
                                    from playlists as p 
                                    join utilisateurs as u
                                    on p.id_utilisateur = u.id_utilisateur 
                                    JOIN chansons as c
                                    on p.id_chanson = c.id_chanson
                                    where nom_utilisateur = %s 
                                  """  
                    case _ :
                        print("erreur champs")
                cur.execute(requete,(valeur,))      
                row = cur.fetchall() 
                #print("TAILLE DE ROW : ",len(row))   
                affiche_row(row)     
                #print(row)
                
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)

playlist_par_champs("nom_utilisateur","Jean Marais")

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