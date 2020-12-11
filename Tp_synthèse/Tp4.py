# Fenetre
import tkinter
from sqlite3 import*

"""
StringVar(): chaine de caractère
IntVar() : nombre entier
DoubleVar(): nombre à virgule
BooleanVar() : booléen
"""
connection = connect("tt_user.db")
cursor= connection.cursor()
#Création de la fenetre globale
root = tkinter.Tk()
#Paramétrer la fenetre globale
root.geometry("400x400")
root.title("TP4")

def popup():
    popup = tkinter.Tk()
    popup.geometry("200x200")
    popup.title("TP4")
    label = tkinter.Label(popup, text="Connexion imppossible")
    label.pack()
    popup.mainloop()
# Initialiser les widgets à afficher (ex Label)
#Label
w = tkinter.Label(root, text = "Login")
w2=tkinter.Label(root, text = "Password")
#Zone de Saisie
var_entry = tkinter.StringVar()
var_entry2 = tkinter.StringVar()
entry = tkinter.Entry(root,textvariable=var_entry)
entry2 = tkinter.Entry(root,textvariable=var_entry2)

var_gender = tkinter.IntVar()
button1 = tkinter.Button(root, text="Connexion",command = popup)
    

# appliquer le mode d'affichage
w.pack()
entry.pack()
w2.pack()
entry2.pack()
button1.pack()
# Affichage de la fenetre Globle
root.mainloop()                  
                
