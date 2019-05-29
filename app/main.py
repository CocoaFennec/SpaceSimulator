from classes.body import body
from classes.vector import vector2
from classes.camera import camera

import pygame as pg
import math

#initialize variables
bodies = [body(100,100, 50), body(200,200,50)]
G = 0.0000000000667408

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
        #end the game if the user closes it
        if event.type == pg.QUIT:
            done = True

        #check to see if the mouse has been pressed
        if event.type == pg.MOUSEBUTTONDOWN:
            #lmb
            if event.button == 1:
                pos = pg.mouse.get_pos()
                bodies.append(body(int((pos[0] + camera.position.x)/camera.zoom), int((pos[1] + camera.position.y)/camera.zoom)))

            #mmb
            if event.button == 2:
                move_camera = True
                start_pos = pg.mouse.get_pos()

            if event.button == 4:
                camera.zoom *= 1.1

            if event.button == 5:
                camera.zoom *= 0.9

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

    for subject in bodies:

        attraction = vector2(0,0)

        for attractor in bodies:

            if attractor != subject:
                distance = int(math.sqrt((attractor.position.x - subject.position.x)**2 + (attractor.position.y - subject.position.y)**2))
                attraction += (attractor.mass/((distance)**3)) * (attractor.position + (-1 * subject.position))




    screen.fill((0,0,0))

    for active_body in bodies:
        pg.draw.circle(screen, (0,0,255),
         (int(active_body.position.x*camera.zoom - camera.position.x),
          int(active_body.position.y*camera.zoom - camera.position.y)),
           int(active_body.radius*camera.zoom))
        
    pg.display.flip()
