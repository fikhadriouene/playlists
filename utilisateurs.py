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


def affiche_utilisateur(id) :
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

# * Utilisateurs : rechercher par `nom_utilisateur`.

def utilisateur_par_nom(nom) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from nom where nom = %s ",(nom,))
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

#modifier_nom_utilisateur(1,'robert')    


def email_nom_utilisateur(id_utilisateur,email) :
    try :
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("update utilisateur set email = %s where id_utilisateur = %s ",(email,id_utilisateur))
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