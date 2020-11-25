# Utilisation de Tkinter
from tkinter import Tk, Label, Button
mw = Tk() # Création Fenêtre Graphique
labelHello = Label(mw, text = "Hello World ! ", fg = 'blue')
labelHello.pack() # Positionnement
buttonQuitt = Button (mw, text = "QUITTER", fg = "red", command = mw.destroy)
buttonQuitt.pack() # Positionnement
mw.mainloop()