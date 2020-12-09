from sqlite3 import*

#connection
connection = connect("GestionFormation.db")
cursor= connection.cursor()

def ajouterMatiere():
    new_matiere=(cursor.lastrowid, "JAVA")
    cursor.execute('INSERT INTO Matiere VALUES(?,?)',new_matiere)
    connection.commit()
    print("Une nouvelle matière a été ajouté")

def ajouterCursus():
    new_cursus=(cursor.lastrowid, "DevOps")
    cursor.execute('INSERT INTO Cursus VALUES(?,?)',new_cursus)
    connection.commit()
    print("Un nouveau cursus a été ajouté")

def ajouterEtudiant():
    new_etudiant=(cursor.lastrowid, "Tsubasa","Natureza",20)
    cursor.execute('INSERT INTO Etudiant VALUES(?,?,?,?)',new_etudiant)
    connection.commit()
    print("Un nouveau etudiant a été ajouté")

def listerMatiere():
    cursor.execute('SELECT * FROM Matiere')
    print(cursor.fetchone())

def listerCursus():
    cursor.execute('SELECT * FROM Cursus')
    print(cursor.fetchone())

def listerEtudiant():
    cursor.execute('SELECT * FROM Etudiant')
    print(cursor.fetchone())

def modifierMatiere():
    modif_matiere=('SQL',1)
    cursor.execute('UPDATE Matiere SET nomMatiere=? WHERE idMatiere=?', modif_matiere)
    connection.commit()
    print("La nouvelle matiere qui a été ajouté est mis à jour")

def modifierCursus():
    modif_cursus=('WebMaster',1)
    cursor.execute('UPDATE Cursus SET nomCursus=? WHERE idCursus=?', modif_cursus)
    connection.commit()
    print("Le nouv cursus qui a été ajouté est mis à jour")

def modifierEtudiant():
    modif_etudiant=('Yusuke','Battousai',22,1)
    cursor.execute('UPDATE Etudiant SET nomEtudiant=?, prenomEtudiant=?, age=? WHERE idEtudiant=?', modif_etudiant)
    connection.commit()
    print("Le nouv utilisateur qui a été ajouté est mis à jour")

def supprimerMatiere():
    del_matiere=(1,)
    cursor.execute('DELETE from Matiere WHERE idMatiere=?', del_matiere)
    connection.commit()
    print("La bdd a été mise à jour")
    

def supprimerCursus():
    del_cursus=(1,)
    cursor.execute('DELETE from Cursus WHERE idCursus=?', del_cursus)
    connection.commit()
    print("La bdd a été mise à jour")

def supprimerEtudiant():
    del_etudiant=(1,)
    cursor.execute('DELETE from Etudiant WHERE idEtudiant=?', del_etudiant)
    connection.commit()
    print("La bdd a été mise à jour")
    
#ajouterMatiere()
#ajouterCursus()
#ajouterEtudiant()
#listerMatiere()
#listerCursus()
#listerEtudiant()
#modifierMatiere()
#modifierCursus()
#modifierEtudiant()
supprimerMatiere()
supprimerCursus()
supprimerEtudiant()
cursor.close()
connection.close()
