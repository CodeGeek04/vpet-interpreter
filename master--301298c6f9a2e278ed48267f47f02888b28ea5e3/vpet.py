from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


def load_model(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    vertices = []
    faces = []
    
    for line in lines:
        if line.startswith('v '):
            vertex = line.split()[1:]
            vertex = [float(coord) for coord in vertex]
            vertices.append(vertex)
        elif line.startswith('f '):
            face = line.split()[1:]
            face = [int(index.split('/')[0]) for index in face]
            faces.append(face)
    
    return vertices, faces


def render_model(vertices, faces):
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex_index in face:
            vertex = vertices[vertex_index - 1]
            glVertex3fv(vertex)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Set up the camera position and orientation
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
    
    # Render the Ironman model
    render_model(vertices, faces)
    
    glFlush()
    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"VPet")
    
    # Load the Ironman model
    vertices, faces = load_model("/path/to/ironman.obj")
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    
    glEnable(GL_DEPTH_TEST)
    
    glutMainLoop()


if __name__ == "__main__":
    main()
