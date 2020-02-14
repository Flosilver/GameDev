from sfml import sf
import time
from typing import TypedDict

class Perso(sf.Shape):
    '''Un perso est la représentation du personnage dans le jeu'''

    # constructeur
    def __init__(self,form,nom):
        self.shape = form
        self.name = nom

    # méthodes
    def _set_color(self,color):
        self.shape.fill_color

    def _get_shape(self):
        print ("Récupération de la forme")
        return self.shape

    def drawPerso(self,window):
        w = self.size.x
        h = self.size.y

        x = self.shape.position.x
        y = self.shape.position.y

        winW = window.mode.width
        if x < winW and x + w > winW:
            newS = self.shape()
            newS.position = (x - winW,y)
            newS.fill_color = self.fill_color

            window.draw(newS)
        window.draw(self)



        