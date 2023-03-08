import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def Cube(_w,_h,_d,i,j):
    glBegin(GL_QUADS)
# front
    glColor3f(1,0,0)
    glVertex3f(_w,_h+j,_d)
    glVertex3f(_w,_h,_d)
    glVertex3f(_w+i,_h,_d)
    glVertex3f(_w+i,_h+j,_d)
    #back
    glColor3f(0,1,0)
    glVertex3f(_w+i,_h,0)
    glVertex3f(_w,_h,0)
    glVertex3f(_w,_h+j,0)
    glVertex3f(_w+i,_h+j,0)
    #top
    glColor3f(0,0,1)
    glVertex3f(_w,_h+j,0)
    glVertex3f(_w,_h+j,_d)
    glVertex3f(_w+i,_h+j,_d)
    glVertex3f(_w+i,_h+j,0)
    #bottom
    glColor3f(1,1,0)
    glVertex3f(_w,_h,0)
    glVertex3f(_w+i,_h,0)
    glVertex3f(_w+i,_h,_d)
    glVertex3f(_w,_h,_d)
    #left
    glColor3f(0,1,1)
    glVertex3f(_w,_h+j,0)
    glVertex3f(_w,_h,0)
    glVertex3f(_w,_h,_d)
    glVertex3f(_w,_h+j,_d)
    #right
    glColor3f(1,0,1)
    glVertex3f(_w+i,_h+j,_d)
    glVertex3f(_w+i,_h,_d)
    glVertex3f(_w+i,_h,0)
    glVertex3f(_w+i,_h+j,0)
    glEnd()

def main():
    pygame.init()
    display = (1000,1000)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glRotatef(25,1,0,0)
        glRotatef(25,0,1,0)
        glRotatef(25,0,0,1)
        
        glEnable(GL_DEPTH_TEST)
        #right side straight line
        Cube(0,0,.1,.2,1.2)
        #bottom
        Cube(0,0,.1,.7,.2)
        #top
        Cube(0,1.1,.1,.7,.2)
        #from up
        Cube(.5,.1,.1,.2,.55)
        # from down
        Cube(.5,.75,.1,.2,.5)
        #from mid
        Cube(.22,.53,.1,.44,.3)
        pygame.display.flip()
        pygame.time.wait(500)


main()