from classes.body import body
from classes.vector import vector2
from classes.camera import camera

import pygame as pg

#initialize variables
bodies = [body(100,100, 50), body(200,200,50)]

#initialize pg
pg.init()

#gets screen resolution
info_object = pg.display.Info()

#sets up camera
camera = camera(0,0)
camera_offset = [info_object.current_w/2, info_object.current_h/2]
camera.offset = vector2(camera_offset[0], camera_offset[1])
move_camera = False

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

            #mmb
            if event.button == 2:
                move_camera = True
                start_pos = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONUP:
            #rmb
            if event.button == 2:
                move_camera = False

        if move_camera == True:
            
            end_pos = pg.mouse.get_pos()

            moved = [end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]]

            camera.position.x -= moved[0]
            camera.position.y -= moved[1]

            start_pos = pg.mouse.get_pos()


    screen.fill((0,0,0))

    for active_body in bodies:
        pg.draw.circle(screen, (0,0,255), (active_body.position.x - camera.position.x, active_body.position.y-camera.position.y), active_body.radius)
        
    pg.display.flip()
