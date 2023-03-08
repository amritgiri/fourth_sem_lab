# Process 
### The code of computer graphics is written and compiled in python programming language
------
# For graphics
- make sure the file 'graphics.py' is in the same directory 
["https://github.com/amritgiri/fourth_sem_lab/blob/main/computer_grahics/graphics.py"] 
this file can be obtain from google also
["https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjX3oHc5MP9AhWw-TgGHcfdCjIQFnoECAkQAQ&url=https%3A%2F%2Fmcsp.wartburg.edu%2Fzelle%2Fpython%2Fgraphics.py&usg=AOvVaw0BK1u3K7Zlz11wKnnaJKPS"]
- After downloading the file copy it to the project folder
- Now, import the file as:
```py
    from graphics import *
```
- Now you are ready to perform graphics as in C/C++ programming language
--------
# For OpenGL
- Make sure you install pyopengl in your system
```
$ suo apt update
$ sudo pip3 install pyopengl
$ pip install PyOpenGL PyOpenGL_accelerate
$ sudo apt-get install python-pygame
```

--------
--------
# Questions
### 1) To be familiar with DDA Line drawing algorithm.

WAP to implement DDA algorithm to draw the following AB Lines:
a) A (100,100) and B (200,250)
b) A (300,100) and B (100,250)
c) A (300,400) and B (100,250)

---

### 2) To be familiar with Bresenham’s Line drawing algorithm.

WAP to implement Bresenham’s algorithm to draw the following AB Lines:
a) A (150,100) and B (250,250)
b) A (300,150) and B (150,250)
c) A (300,200) and B (100,50)

---

### 3) To be familiar with Mid-point Circle drawing algorithm.

WAP to implement Mid-point Circle drawing algorithm to draw circle and Make
a Cone form the combination of circles.
a) Radius=100 and Center (200,125)

---

### 4) To be familiar with Mid-point Ellipse drawing algorithm.

WAP to implement Mid-point Ellipse drawing algorithm to draw ellipse:
a) Radius-x=100, Radius-y=75 and Center (200,125)
b) Radius-x=160, Radius-y=250 and Center (300,300)

---

### 5) WAP to implement Basic transformation of a triangle ABC with coordinates A

(60,60), B (110,60) and (70,100):

1. Translation with translation vector tx=40 and ty=-20.
2. Scaling with scaling factor sx=2 and sy=2.
3. Rotation about y-axis by 45 degree in CC-direction.

--------------------

### 6) To be familiar with Fixed point scaling and Pivot point rotation.WAP to implement Fixed point scaling and Pivot point rotation of a triangle ABC with coordinates A (60,60), B (110,60) and (70,100):
1) Scale about the centroid with scaling factor sx=2 and sy=2.
2) Scale about the centroid with scaling factor sx=1/2 and sy=1/2.
3) Rotation about the centroid by 90 degree in CC-direction.
4) Rotation about the centroid by 180 degree in clockwise-direction.

-----------------
### 7) To be familiar with Shear. WAP to implement Shear of a square ABCD whose coordinates are A (0,0), B (0,100), C (100,100) and D (100,0).
1) Shear the square relative to the Xref =-10 and Shy = 2. Calculate the final
coordinates and draw it.
2) Shear the square relative to the Yref =-10 and Shx = 1. Calculate the final
coordinates and draw it.
-----
### 8) Draw letter B using Opengl