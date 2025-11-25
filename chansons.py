import psycopg
#DSN = "dbname=postgres user=admin password=admin host=localhost port=5432"
DSN = "dbname=postgres user=admin password=admin host=localhost port=5432"
# #### Chansons

# * Ajouter une nouvelle chanson avec `titre`, `artiste`, `album`, `duree`, `genre`, `annee_sortie`.
def ajouter_chanson(titre,artiste,album,duree,genre,annee_sortie) :

    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur = conn.cursor()
                cur.execute("insert into chansons(titre,artiste,album,duree,genre,annee_sortie) values(%s,%s,%s,%s,%s,%s)",(titre,artiste,album,duree,genre,annee_sortie))
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)

# OK -> ajouter_chanson('La tendresse', 'Bourvil', 'Les plus belles chansons', 180, 'Chanson française', '1963-01-01')
# ajouter_chanson('chanson de farid', 'farid', 'Les plus belles chansons de farid', 5, 'Chanson du nord', '2025-11-24')


def rechercher_chanson(id) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from chansons where id_chanson = %s ",(id,))
                row = cur.fetchall()
                #print(row)
                return row
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)

# OK -> rechercher_chanson(4)

def affiche_chanson(id) :
    try :

        print(rechercher_chanson(id))
        # with psycopg.connect(DSN) as conn:
        #     with conn.cursor() as cur:
        #         cur.execute("select * from chansons where id_chanson = %s ",(id,))
        #         row = cur.fetchall()
        #         print(row)
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)

# OK -> affiche_chanson(3)

# * Chansons : rechercher par `titre`, `artiste` ou `genre`.

def chanson_par_champs(champs, valeur) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                
                match champs :
                    case "titre" :
                        cur.execute("select * from chansons where titre = %s ",(valeur,))
                    case "artiste" :
                        cur.execute("select * from chansons where artiste = %s ",(valeur,))
                    case "genre" :
                        cur.execute("select * from chansons where genre = %s ",(valeur,))   
                    case _ :
                        pass     
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

# OK -> chanson_par_champs("titre","Bohemian Rhapsody")
# OK -> chanson_par_champs("artiste","Queen")
# OK -> chanson_par_champs("genre","Rock")

# * **Chansons** : modification de n'importe quel champ de la chanson.champ

def get_colonnes(nom_table):
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'chansons';")
                row = cur.fetchall()
                colonnes = [r[0] for r in row]
                return colonnes
    except Exception as e :
        print("Erreur colonnes", e)


def modifier_chanson(id_chanson,champ,valeur) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                colonnes = get_colonnes("chansons")
                if champ in colonnes :
                    requete = f"update chansons set {champ} = %s where id_chanson= %s"
                    #cur.execute("update chansons set %s = %s where id_chanson=%s ",(champ,valeur,id_chanson)) 
                    cur.execute(requete,(valeur,id_chanson))   
                else :
                    print("champ invalide")         
                
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)
# OK -> modifier_chanson(7,"titre or 1=1","La nouvelle chanson de boby")
# OK ->affiche_chanson(7)

#   * ajout de nouvelles chansons




#   * suppression de chansons existantes
   
def supprimer_chanson(id_chanson):
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("delete from chansons where id_chanson = %s returning *;",(id_chanson,))      
                        
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e) 

# OK -> supprimer_chanson(7)
