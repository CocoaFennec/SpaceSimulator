from classes.body import body
from classes.vector import vector2

import pygame as pg

#initialize variables
bodies = [body(100,100, 50), body(200,200,50)]

#initialize pg
pg.init()

#gets screen resolution
info_object = pg.display.Info()

print(info_object.current_h)
print(info_object.current_w)

#sets up the screen to display the game
#screen = pg.display.set_mode((info_object.current_w, info_object.current_h), pg.FULLSCREEN)
screen = pg.display.set_mode((1920, 1080), pg.NOFRAME)
pg.display.set_caption("Space Simulation")

done = False

while not done:
    for event in pg.event.get():
        #if end the game if the user closes it
        if event.type == pg.QUIT:
            done = True

        #check to see if the mouse has been pressed
        if event.type == pg.MOUSEBUTTONDOWN:
            #lmb
            if event.button == 1:
                pos = pg.mouse.get_pos()
                bodies.append(body(pos[0], pos[1]))

    screen.fill((0,0,0))

    for active_body in bodies:
        pg.draw.circle(screen, (0,0,255), (active_body.position.x, active_body.position.y), active_body.radius)
        
        
    pg.display.flip()
