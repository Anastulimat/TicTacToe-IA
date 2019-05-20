import tkinter
import random
import pprint

#################################################################################
#
#  Parametres du jeu

canvas = None   # zone de dessin


#Grille[0][0] désigne la case en haut à gauche
#Donc Grille[2][0] on a [2] représente le nombre du colonne et [0] le nombre de la ligne
#Grille[2][0] désigne la case en haut à droite
#Grille[0][2] désigne la case en bas à gauche


Grille = [ [0,0,1], 
           [2,0,0], 
           [0,0,0] ]  # attention les lignes représentent les colonnes de la grille
           
Scores = [0,0]   # score du joueur 1 (Humain) et 2 (IA)

window = tkinter.Tk()

#################################################################################
#
# gestion du joueur humain et de l'IA
# VOTRE CODE ICI 

def Play(x,y):
    global Grille             
    Grille[x][y] = 1

    positionsList = possiblePositions(Grille)
    
    if(len(positionsList) == 0):
        print("PASS len(positionsList) == 0")
        Grille = [ [0,0,1], 
            [2,0,0], 
            [0,0,0] ]
        Affiche(True)
        return

    randomPosition = pickRandomPosition(positionsList)
    Grille[randomPosition[0]][randomPosition[1]] = 2

    
    if(winTestOnLinesForPlayer(y) or winTestOnColomnsForPlayer(x) or winTestOnDiagonalForPlayer()):
        Scores[0] += 1
        Grille = [ [0,0,1], 
            [2,0,0], 
            [0,0,0] ]
        Affiche(True)
        return

    if(winTestOnLinesForIA(randomPosition[1]) or winTestOnColomnsForIA(randomPosition[0]) or winTestOnDiagonalForIA()):
        Scores[1] += 1
        Grille = [ [0,0,1], 
            [2,0,0], 
            [0,0,0] ]
        Affiche(True)
        return
    

    print(positionsList)
    print("==== Choix du IA ==== " + str(randomPosition))
    pprint.pprint(Grille)

    

def initGame():
    global Grille
    Grille = [ [0,0,1], 
            [2,0,0], 
            [0,0,0] ]
    Affiche(True)
    return
    

        
        
##### TEST SUR LES LIGNES FOR PLAYER #####
##########################################
def winTestOnLinesForPlayer(y):
    # On est sur la première ligne
    if(y == 0):
        if(Grille[0][y] == 1 and Grille[1][y] == 1 and Grille[2][y] == 1):
            print("Joueur 1 gange sur la première ligne")
            return True
    
    # On est sur la deuxième ligne
    if(y == 1):
        if(Grille[0][y] == 1 and Grille[1][y] == 1 and Grille[2][y] == 1):
            print("Joueur 1 gange sur la deuxième ligne")
            return True

    # On est sur la troisième ligne
    if(y == 2):
        if(Grille[0][y] == 1 and Grille[1][y] == 1 and Grille[2][y] == 1):
            print("Joueur 1 gange sur la troisième ligne")
            return True
        
    return False


##### TEST SUR LES LIGNES FOR IA #####
######################################
def winTestOnLinesForIA(y):
    # On est sur la première ligne
    if(y == 0):
        if(Grille[0][y] == 2 and Grille[1][y] == 2 and Grille[2][y] == 2):
            print("Joueur 2 gange sur la première ligne")
            return True
    
    # On est sur la deuxième ligne
    if(y == 1):
        if(Grille[0][y] == 2 and Grille[1][y] == 2 and Grille[2][y] == 2):
            print("Joueur 2 gange sur la deuxième ligne")
            return True

    # On est sur la troisième ligne
    if(y == 2):
        if(Grille[0][y] == 2 and Grille[1][y] == 2 and Grille[2][y] == 2):
            print("Joueur 2 gange sur la troisième ligne")
            return True
        
    return False










##### TEST SUR LES COLONNES FOR PLAYER #####
############################################
def winTestOnColomnsForPlayer(x):
    # On est sur la première colonne
    if(x == 0):
        
        if(Grille[x][0] == 1 and Grille[x][1] == 1 and Grille[x][2] == 1):
            print("Joueur 1 gagne ur la première colonne")
            return True
    
    # On est sur la deuxième colonne
    if(x == 1):
        if(Grille[x][0] == 1 and Grille[x][1] == 1 and Grille[x][2] == 1):
            print("Joueur 1 gagne sur la deuxième colonne")
            return True

    # On est sur la troisième colonne
    if(x == 2):
        if(Grille[x][0] == 1 and Grille[x][1] == 1 and Grille[x][2] == 1):
            print("Joueur 1 gagne sur la troisième colonne")
            return True

    return False



##### TEST SUR LES COLONNES FOR IA #####
########################################
def winTestOnColomnsForIA(x):
    # On est sur la première colonne
    if(x == 0):
        print("X == 0 FOR IA")
        if(Grille[x][0] == 2 and Grille[x][1] == 2 and Grille[x][2] == 2):
            print("Joueur 2 gagne ur la première colonne")
            return True
    
    # On est sur la deuxième colonne
    if(x == 1):
        print("X == 1 FOR IA")
        if(Grille[x][0] == 2 and Grille[x][1] == 2 and Grille[x][2] == 2):
            print("Joueur 2 gagne sur la deuxième colonne")
            return True

    # On est sur la troisième colonne
    if(x == 2):
        print("X == 2 FOR IA")
        if(Grille[x][0] == 2 and Grille[x][1] == 2 and Grille[x][2] == 2):
            print("Joueur 2 gange sur la troisième colonne")
            return True

    return False




##### TEST SUR LES DIGONALES FOR PLAYER #####
#############################################
def winTestOnDiagonalForPlayer():
    # On est sur le digonale du gauche vers la droite
    if(Grille[0][0] == 1 and Grille[1][1] == 1 and Grille[2][2] == 1):
        print("Joueur 1 gagne sur le digonale du gauche vers la droite")
        return True

    # On est sur le digonale du droite vers le gauche
    if(Grille[2][0] == 1 and Grille[1][1] == 1 and Grille[0][2] == 1):
        print("Joueur 1 gagne sur le digonale du gauche vers la droite")
        return True

    return False




##### TEST SUR LES DIGONALES FOR IA #####
#########################################
def winTestOnDiagonalForIA():
    # On est sur le digonale du gauche vers la droite
    if(Grille[0][0] == 2 and Grille[1][1] == 2 and Grille[2][2] == 2):
        print("Joueur 2 gagne sur le digonale du gauche vers la droite")
        return True

    # On est sur le digonale du droite vers le gauche
    if(Grille[2][0] == 2 and Grille[1][1] == 2 and Grille[0][2] == 2):
        print("Joueur 2 gagne sur le digonale du gauche vers la droite")
        return True
    
    return False
    

##### LIST POSSIBLE POSITIONS #####
###################################
def possiblePositions(Grille):
    positions = list()

    for x in range(len(Grille[0])):
        for y in range(len(Grille[1])):
            if(Grille[x][y] == 0):
                positions.append((x, y))
    
    return positions


def pickRandomPosition(positionsList):
    if positionsList is not None:
        return positionsList[random.randint(0, len(positionsList)-1)]


def IAPlay(positionsList):
    position = pickRandomPosition(positionsList)
    Grille[position[0]][position[1]]






################################################################################
#    
# Dessine la grille de jeu

def Affiche(PartieGagnee = False):
        ## DOC canvas : http://tkinter.fdex.eu/doc/caw.html
        canvas.delete("all")
        
        for i in range(4):
            canvas.create_line(i*100,0,i*100,300,fill="blue", width="4" )
            canvas.create_line(0,i*100,300,i*100,fill="blue", width="4" )
            
        for x in range(3):
            for y in range(3):
                xc = x * 100 
                yc = y * 100 
                if ( Grille[x][y] == 1):
                    canvas.create_line(xc+10,yc+10,xc+90,yc+90,fill="red", width="4" )
                    canvas.create_line(xc+90,yc+10,xc+10,yc+90,fill="red", width="4" )
                if ( Grille[x][y] == 2):
                    canvas.create_oval(xc+10,yc+10,xc+90,yc+90,outline="yellow", width="4" )
        
        msg = 'SCORES : ' + str(Scores[0]) + '-' + str(Scores[1])
        fillcoul = 'gray'
        if (PartieGagnee) : fillcoul = 'red'
        canvas.create_text(150,400, font=('Helvetica', 30), text = msg, fill=fillcoul)  
        
    
        canvas.update()   #force la mise a jour de la zone de dessin
        
  
####################################################################################
#
#  fnt appelée par un clic souris sur la zone de dessin

def MouseClick(event):
   
    window.focus_set()
    x = event.x // 100  # convertit une coordonée pixel écran en coord grille de jeu
    y = event.y // 100
    if ( (x<0) or (x>2) or (y<0) or (y>2) ) : return
     
    
    print("clicked at", x,y)
    
    Play(x,y)  # gestion du joueur humain et de l'IA
    
    Affiche()

#####################################################################################
#
#  Mise en place de l'interface - ne pas toucher

# fenetre

window.geometry("300x500") 
window.title('Mon Super Jeu')
window.protocol("WM_DELETE_WINDOW", lambda : window.destroy())
window.bind("<Button-1>", MouseClick)

#zone de dessin
WIDTH = 300
HEIGHT = 500
canvas = tkinter.Canvas(window, width=WIDTH , height=HEIGHT, bg="#000000")
canvas.place(x=0,y=0)
Affiche()
 
# active la fenetre 
window.mainloop()


  


    
        

      
 

