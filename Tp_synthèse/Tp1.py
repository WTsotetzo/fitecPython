from sqlite3 import*

#connection
connection = connect("Tp.db")
cursor= connection.cursor()

def ajouterAgence():
    new_agence=(cursor.lastrowid, "CIC")
    cursor.execute('INSERT INTO Agence VALUES(?,?)',new_agence)
    connection.commit()
    print("Une nouvelle agence a été ajouté")

def ajouterCb():
    new_cb=(cursor.lastrowid, 500, 200)
    cursor.execute('INSERT INTO Cb VALUES(?,?,?)',new_cb)
    connection.commit()
    print("Un nouveau Compte Bancaire a été ajouté")

def ajouterClient():
    new_etudiant=(cursor.lastrowid,"Monsieur", "Tsubasa","Natureza","20 rue de tp")
    cursor.execute('INSERT INTO Client VALUES(?,?,?,?,?)',new_etudiant)
    connection.commit()
    print("Un nouveau client a été ajouté")

def listerAgence():
    cursor.execute('SELECT * FROM Agence')
    print(cursor.fetchone())

def listerCb():
    cursor.execute('SELECT * FROM Cb')
    print(cursor.fetchone())

def listerClient():
    cursor.execute('SELECT * FROM Client')
    print(cursor.fetchone())

def modifierAgence():
    modif_agence=('BNP Paribas',1)
    cursor.execute('UPDATE Agence SET nomAgence=? WHERE idAgence=?', modif_agence)
    connection.commit()
    print("La nouvelle agence qui a été ajouté est mis à jour")

def modifierCb():
    modif_cb=(30,100,1)
    cursor.execute('UPDATE Cb SET solde=?, decouvert=? WHERE idCompte=?', modif_cb)
    connection.commit()
    print("Le nouv compte qui a été ajouté est mis à jour")

def modifierClient():
    modif_client=('Madame','Butern','Nami','3 rue de One Piece',1)
    cursor.execute('UPDATE Client SET Civilité=?, nom=?, prenom=?, adresse=? WHERE idClient=?', modif_client)
    connection.commit()
    print("Le nouv client qui a été ajouté est mis à jour")

def supprimerAgence():
    del_agence=(1,)
    cursor.execute('DELETE from Agence WHERE idAgence=?', del_agence)
    connection.commit()
    print("La bdd a été mise à jour")
    

def supprimerCb():
    del_cb=(1,)
    cursor.execute('DELETE from Cb WHERE idCompte=?', del_cb)
    connection.commit()
    print("La bdd a été mise à jour")

def supprimerClient():
    del_client=(1,)
    cursor.execute('DELETE from Client WHERE idClient=?', del_client)
    connection.commit()
    print("La bdd a été mise à jour")

def ajouter(client,compte):
    cursor


###Main
#ajouterAgence()
#ajouterCb()
#ajouterClient()
#listerAgence()
#listerCb()
#listerClient()
#modifierAgence()
#modifierCb()
#modifierClient()
#supprimerAgence()
#supprimerCb()
#supprimerClient()
cursor.close()
connection.close()




