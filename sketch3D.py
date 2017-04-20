from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import texture
import rock
from random import randint
from random import uniform
import tkFileDialog


name = 'texture'

texture_size = 500

new_radius = [randint(10,90), randint(10,90), randint(10,90)]
new_color = [uniform(0,1),uniform(0,1),uniform(0,1),1.]
move_mode = 0
new_center = [0., 0., 0.]
new_rotation = [randint(0,360), randint(0,360), randint(0,360)]

new_rock_mode = False

last_x = 0
last_y = 0

x_rot = 0
y_rot = 0

mTexture = texture.Texture3D(texture_size)
originalTexture = mTexture

def sketch(pTexture=None, t_size=500, window_size =1000, random_texture_size=None):
    global texture_size
    global mTexture
    global originalTexture
    
    if pTexture != None:
        mTexture = pTexture
    else: 
        originalTexture = mTexture = texture.Texture3D(t_size)

    if random_texture_size != None:
        originalTexture = mTexture = texture.createRandomTexture(t_size, random_texture_size)

    rock.setTextureSize(t_size)
    texture_size = t_size

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_size,window_size)
    glutCreateWindow(name)

    glClearColor(1.,1.,1.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_NORMALIZE)
    glEnable(GL_CLIP_PLANE0)
    glEnable(GL_CLIP_PLANE1)
    glEnable(GL_CLIP_PLANE2)
    glEnable(GL_CLIP_PLANE3)
    glEnable(GL_CLIP_PLANE4)
    glEnable(GL_CLIP_PLANE5)
    lightZeroPosition = [t_size/5,t_size/10,t_size/5,1.]
    lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.5/t_size)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.5/t_size)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display)
    if pTexture == None:
        glutKeyboardFunc(keypressed)
    glutMotionFunc(mouseMotion)
    glutMouseFunc(click)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40.,1.,1.,t_size*4)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(t_size*2,t_size,t_size*2,
              0,0,0,
              0,1,0)
    glPushMatrix()
    glutMainLoop()

    return mTexture

def display():

    global texture_size
    global new_rock_mode
    global new_rotation

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glClipPlane(GL_CLIP_PLANE0, [ 1., 0., 0., texture_size/2.+1]);
    glClipPlane(GL_CLIP_PLANE1, [-1., 0., 0., texture_size/2.+1]);
    glClipPlane(GL_CLIP_PLANE2, [ 0., 1., 0., texture_size/2.+1]);
    glClipPlane(GL_CLIP_PLANE3, [ 0.,-1., 0., texture_size/2.+1]);
    glClipPlane(GL_CLIP_PLANE4, [ 0., 0., 1., texture_size/2.+1]);
    glClipPlane(GL_CLIP_PLANE5, [ 0., 0.,-1., texture_size/2.+1]);

    glPushMatrix()
    color = [1.,1.,1.,1]
    glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
    glLineWidth(5)
    glutWireCube(texture_size)
    glPopMatrix()

    if new_rock_mode:
        glPushMatrix()
        glMaterialfv(GL_FRONT,GL_DIFFUSE, new_color)
        glTranslatef(new_center[0], new_center[1], new_center[2])
        glRotatef( new_rotation[0], 1.0, 0.0, 0.0 )
        glRotatef( new_rotation[1], 0.0, 1.0, 0.0 )
        glRotatef( new_rotation[2], 0.0, 0.0, 1.0 )
        glScalef(new_radius[0],new_radius[1], new_radius[2])
        glutSolidSphere(1,50,50)
        glPopMatrix()

    for rock in mTexture.rocks:
        glPushMatrix()
        glMaterialfv(GL_FRONT,GL_DIFFUSE, rock.color.tolist() + [1.])
        glTranslatef(rock.center[0],rock.center[1], rock.center[2])
        glRotatef( rock.rotation[0], 1.0, 0.0, 0.0 )
        glRotatef( rock.rotation[1], 0.0, 1.0, 0.0 )
        glRotatef( rock.rotation[2], 0.0, 0.0, 1.0 )
        glScalef(rock.radius[0],rock.radius[1], rock.radius[2])
        glutSolidSphere(1,50,50)
        glPopMatrix()

    glutSwapBuffers()
    return

def keypressed(*args):
    global new_radius
    global new_color
    global new_center
    global new_rotation
    global move_mode
    global new_rock_mode
    global mTexture
    global originalTexture

    if new_rock_mode:
        if args[0] == '1':
            new_radius[move_mode] = 10
        elif args[0] == '2':
            new_radius[move_mode] = 20
        elif args[0] == '3':
            new_radius[move_mode] = 30
        elif args[0] == '4':
            new_radius[move_mode] = 40
        elif args[0] == '5':
            new_radius[move_mode] = 50
        elif args[0] == '6':
            new_radius[move_mode] = 60
        elif args[0] == '7':
            new_radius[move_mode] = 70
        elif args[0] == '8':
            new_radius[move_mode] = 80
        elif args[0] == '9':
            new_radius[move_mode] = 90

        elif args[0] == 'r':
            new_color = [1.,0.,0.,1.]
        elif args[0] == 'g':
            new_color = [0.,1.,0.,1.]
        elif args[0] == 'b':
            new_color = [0.,0.,1.,1.]

        elif args[0] == 'x':
            move_mode = 0
        elif args[0] == 'y':
            move_mode = 1
        elif args[0] == 'z':
            move_mode = 2

        elif args[0] == 'l':
            if (-texture_size / 2.) < new_center[move_mode]:
                new_center[move_mode] -= 1
        elif args[0] == 'o':
            if (texture_size / 2.) > new_center[move_mode]:
                new_center[move_mode] += 1
        elif args[0] == 'k':
            new_rotation[move_mode] -= 1
        elif args[0] == 'i':
            new_rotation[move_mode] += 1

        elif args[0] == 'a':
            if mTexture.add(rock.Rock3D(new_center, new_radius, new_color, new_rotation)):
                new_radius = [randint(10,90), randint(10,90), randint(10,90)]
                new_color = [uniform(0,1),uniform(0,1),uniform(0,1),1.]
                move_mode = 0
                new_center = [0., 0., 0.]
                new_rotation = [randint(0,360), randint(0,360), randint(0,360)]
                new_rock_mode = False
                originalTexture = mTexture

        glutPostRedisplay()

    else:
        if args[0] == 'n':
            new_rock_mode = True
        elif args[0] == 'S':
            file_save(originalTexture)
        elif args[0] == 'P':
            originalTexture.learn()
            mTexture = originalTexture.sample()

        glutPostRedisplay()

        

def click( button, state, x, y ):
    global last_x
    global last_y

    if state == GLUT_DOWN:
        last_x  = x
        last_y  = y

def mouseMotion (x, y):
    global last_x
    global last_y
    global x_rot
    global y_rot


    x_rot = ((x - last_x)) % 360
    y_rot = ((y - last_y)) % 360

    last_x = x
    last_y = y

    glRotatef( x_rot, 0.0, 1.0, 0.0 )
    
    glutPostRedisplay()

def file_save(texture):
    f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".te", initialdir='textures')
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = texture.toString()
    f.write(text2save)
    f.close()