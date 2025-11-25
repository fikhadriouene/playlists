import psycopg
# * Ajouter un nouvel utilisateur avec `nom_utilisateur`, `email`.
# * La date d’inscription est ajoutée automatiquement.
DSN = "dbname=postgres user=admin password=admin host=localhost port=5432"

def ajouter_utilisateur(nom_utilisateur,email) :

    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur = conn.cursor()
                cur.execute("insert into utilisateurs(nom_utilisateur,email) values(%s,%s)",(nom_utilisateur,email))
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)

# OK -> ajouter_utilisateur("Jean Marais","jean@marais.com")
ajouter_utilisateur("Jean Marais","jean@marais.com")


# * Afficher toutes les informations de l’enregistrement correspondant à l’ID fourni.

def rechercher_utilisateur(id) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from utilisateurs where id_utilisateur = %s ",(id,))
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

# OK -> rechercher_utilisateur(7)

def affiche_row(row : dict) :
    print ()
    print (f"------ utilisateur {row['id_utilisateur']} ------- ")
    print (f"nom utilisateur : ",row['nom_utilisateur'])
    print (f"email : ",row['email'])
    print (f"date inscription : ",row['date_inscription'])
    print (f"------------------------------- ")
    print ()
    
    

def affiche_utilisateur(id) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
                cur.execute("select * from utilisateurs where id_utilisateur = %s ",(id,))
                row = cur.fetchone()
                affiche_row(row)
                
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)

# OK -> affiche_utilisateur(7)

# * Utilisateurs : rechercher par `nom_utilisateur`.

def utilisateur_par_nom(nom) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
                cur.execute("select * from utilisateurs where nom_utilisateur = %s ",(nom,))
                row = cur.fetchone()
                affiche_utilisateur(row['id_utilisateur'])
                
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)

# OK -> utilisateur_par_nom("Jean Marais")


# ### 3. Mise à jour d’un enregistrement

# * **Utilisateurs** : modification de `nom_utilisateur` et `email`.

def modifier_nom_utilisateur(id_utilisateur,nom) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("update utilisateurs set nom_utilisateur = %s where id_utilisateur = %s ",(nom,id_utilisateur))
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)

# OK -> modifier_nom_utilisateur(7,'Louis de funes')    


def modifier_email_utilisateur(id_utilisateur,email) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("update utilisateurs set email = %s where id_utilisateur = %s ",(email,id_utilisateur))

    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)

# OK -> modifier_email_utilisateur(7,"louis@defunes.fr")

def supprimer_utilisateur(id_utilisateur) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("delete from utilisateurs where id_utilisateur = %s ",(id_utilisateur,))
                
    except psycopg.errors.SyntaxError as e: 
        print ("Erreur SQL : ", e)
    except psycopg.errors.UniqueViolation as e:
        print ("Violation Unique : ", e)
    except psycopg.OperationalError as e:
        print ("Problème de connection :" , e)
    except Exception as e:
        print ("Autre erreurs : ", e)
        
# OK -> supprimer_utilisateur(7)        
