from sfml import sf
import time
from typing import TypedDict
WIDTH = 1000
HEIGHT = 600
G = sf.Vector2(0,1.3)

def draw_cube( win , r):  # win: la window / r: votre rectangle 
    x = r.position.x
    y = r.position.y

    w = r.size.x
    h = r.size.y

    #print(x,y,w,h,WIDTH,x+w)

    if x < WIDTH and x + w > WIDTH:     # il faut connaitre la largeur de votre fenêtre
        newR = sf.RectangleShape()
        newR.size = (w-(WIDTH-x),h)
        newR.position = (0,y)
        newR.fill_color = r.fill_color

        win.draw(newR)
    win.draw(r)

def moveXModulo(vin,x,mod):
    xin = vin.x
    yin = vin.y

    newX = abs( (xin + x)%mod )

    return sf.Vector2(newX,yin)


vit = sf.Vector2(0,0)

window = sf.RenderWindow(sf.VideoMode(WIDTH, HEIGHT), 'Basic Window Tutorial', sf.Style.DEFAULT)
window.framerate_limit = 60
window.key_repeat_enabled = False

rect = sf.RectangleShape()
rect.size = (50,50)
rect.position = (475,25)
rect.fill_color = sf.Color.GREEN


while window.is_open:
# fetch events (explained in next tutorial function)
    for event in window.events:
        if event == sf.Event.CLOSED:
            window.close()
        if event == sf.Event.KEY_PRESSED:
        #    if event["code"] == sf.Keyboard.UP:
        #        rect.move((0,-5))
        #    if event["code"] == sf.Keyboard.DOWN:
        #        rect.move((0,5))
        #    if event["code"] == sf.Keyboard.LEFT:
        #        rect.move((-5,0))
        #    if event["code"] == sf.Keyboard.RIGHT:
        #        rect.move((5,0))
            if event["code"] == sf.Keyboard.SPACE:
                vit.y = -25
    
    #if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
    #    rect.move((0,-5))
    #if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
    #    rect.move((0,5))
    if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT) or sf.Keyboard.is_key_pressed(sf.Keyboard.A):
        rect.position = moveXModulo(rect.position,-8,WIDTH)
        #rect.move((-10,0))
    if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT) or sf.Keyboard.is_key_pressed(sf.Keyboard.D):
        #rect.move((10,0))
        rect.position = moveXModulo(rect.position,8,WIDTH)

    rect.position = rect.position + vit
    #print(rect.position.y,HEIGHT-20-rect.size.y)

    if rect.position.y < HEIGHT-20-rect.size.y:
        vit = vit + G
    else:
        vit = sf.Vector2(0,0)
        rect.position = (rect.position.x,HEIGHT-20-rect.size.y)

    # clear window with a color (optional), by default, window is cleared with BLACK
    window.clear(sf.Color.BLACK)
    #window.draw(rect)
    draw_cube(window,rect)
    # finally display the window
    window.display()



