'''
AUTHOR: TIGIST WONDIMNEH
SECTION: 1
ID: UGR/2538/12
'''
from tkinter import *
import pygame
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

class functionGraphs:

    def __init__(self):

        self.root = Tk()
        self.root.configure(bg="white")
        self.root.title("My Graph")
        self.root.geometry('600x600')

        #Create the gui
        self.label_one = Label(self.root, text="Welcome!",
                               bg="white", font=("Calibri", 30, "bold"))
        self.label_two = Label(self.root, text="Select functions to draw their graphs!",
                               bg="white", fg="black", font=("Calibri", 15,"bold"))

        self.label_three = Label(self.root, text="Graph one", bg="grey", font=("Calibri", 15, "bold"))
        self.label_four = Label(self.root, text="Graph two", bg="grey", font=("Calibri", 15, "bold"))

        #Display the label gui's
        self.label_one.grid(row=0, column=0, padx=150, pady=15, columnspan=2)
        self.label_two.grid(row=1, column=0, padx=150, columnspan=2)

        self.label_three.grid(row=2, column=0, padx=30, pady=10)
        self.label_four.grid(row=2, column=1, padx=30, pady=10)

        # Radiobutton Variables
        self.rad_one = IntVar()
        self.rad_two = IntVar()

        #  Dictionary of radiobuttons of group one
        self.radiobuttons = {
            "Linear Function      " : 1,
            "Modulus Function     " : 2,
            "Square Root Function" : 3,
            "Constant Function    " : 4,
            "Cubic Root Function  " : 5,
            "Heart Function       " : 6,
        }
        for text,value in self.radiobuttons.items():
            Radiobutton(self.root, text=text, width = 20, fg="black", bg = "cyan", font=(
                "Calibri", 12), variable=self.rad_one, value=value, indicatoron = 0).grid(row=value + 2, column=0, pady = 7)

        #  Dictionary of radiobuttons of group two
        self.radiobuttons_two = {
            "Quadratic Function  ": 1,
            "Cubic Function        ": 2,
            "Cosine Function      ": 3,
            "Sine Function         ": 4,
            "Logarithmic Function": 5,
            "Exponential Function": 6,
        }
        
        for text, value in self.radiobuttons_two.items():
            Radiobutton(self.root, text=text, width = 20, fg="black", bg="orchid", font=(
                "Calibri", 12), variable=self.rad_two, value=value, indicatoron = 0).grid(row=value + 2, column=1, pady = 7)

        # The plot button 
        self.graph_btn = Button(self.root,text="Plot",width = 14, font = ("Calibri", 14, "bold"), fg = "black", bg = "lime", command = self.graph)
        self.graph_btn.grid(row = 10, column = 0, columnspan =2, pady = 5)

        # The close button
        self.graph_btn = Button(self.root, text="Close", width=14, font=("Calibri", 14, "bold"), fg="black", bg="grey", command=self.close)
        self.graph_btn.grid(row = 11, column = 0, columnspan  = 2, pady = 5)
        
        self.root.mainloop()
    #  the function that initiates the pygame window and draws the graphs
    def graph(self):
        self.lable_invalid = Label(self.root, text="You did not select any function, Please choose a function to plot!", fg="red", font=("Calibri", 12, "bold"))
        if self.rad_one.get() == 0 and self.rad_two.get() == 0:
            self.lable_invalid.grid(row = 12, column = 0, columnspan = 2)
        else:
            self.lable_invalid.destroy()
            def init():
                pygame.init()
                display = (900, 500)
                pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
                glClearColor(0.0, 0.0, 0.0, 1.0)
                gluOrtho2D(-5.0, 5.0, -5.0, 5.0)

            def draw():
                glClear(GL_COLOR_BUFFER_BIT)
                glColor3f(1.0, 0.0, 0.0)
                glBegin(GL_LINES)
                glVertex2f(40.0, 0.0)
                glVertex2f(-40.0, 0.0)
                glVertex2f(0.0, 40.0)
                glVertex2f(0.0, -40.0)
                glEnd() 

                x = np.linspace(-10, 10, 100)

                # conditionals for graphing group two

                if self.rad_two.get() == 1:
                    y = np.power(x, 2)
                    glPointSize(10)
                    glColor3f(0.0, 0.0, 1.0)
                    glBegin(GL_LINE_STRIP)
                    for a, b in zip(x, y):
                        glVertex2f(a, b)
                    glEnd()
                    glFlush()

                elif self.rad_two.get() == 2:
                    y = np.power(x,3)
                    glColor3f(0.0, 0.0, 1.0)
                    glPointSize(10)
                    glBegin(GL_LINE_STRIP)
                    for a, b in zip(x, y):
                        glVertex2f(a, b)
                    glEnd()
                    glFlush()

                elif self.rad_two.get() == 3:
                    z = np.linspace(-(360 * np.pi),360 * np.pi,10000)
                    y = np.cos(z)
                    glColor3f(0.0, 0.0, 1.0)
                    glPointSize(10)
                    glBegin(GL_LINE_STRIP)
                    for a, b in zip(z,y):
                        glVertex2f(a, b)
                    glEnd()
                    glFlush()
                    
                elif self.rad_two.get() == 4:
                    z = np.linspace(-(360 * np.pi), 360 * np.pi, 10000)
                    y = np.sin(z)
                    glPointSize(10)
                    glColor3f(0.0, 0.0, 1.0)
                    glBegin(GL_LINE_STRIP)
                    for a, b in zip(z,y):
                        glVertex2f(a, b)
                    glEnd()
                    glFlush()

                elif self.rad_two.get() == 5:
                    z = np.linspace(0,5,10000)
                    y = np.log10(z)
                    glColor3f(0.0, 0.0, 1.0)
                    glPointSize(10)
                    glBegin(GL_LINE_STRIP)
                    for a, b in zip(z,y):
                        glVertex2f(a, b)
                    glEnd()
                    glFlush()

                elif self.rad_two.get() == 6:
                    z = np.linspace(-5,5,1000)
                    y = np.power(2,z)
                    glColor3f(0.0, 0.0, 1.0)
                    glPointSize(10)
                    glBegin(GL_LINE_STRIP)
                    for a, b in zip(z,y):
                        glVertex2f(a, b)
                    glEnd()
                    glFlush()
                else:
                    pass
                # conditionals for graphing group one
                if self.rad_one.get() == 1:
                    z = np.linspace(-5,5,1000)
                    y = z
                    glPointSize(10)
                    glColor3f(0.0, 1.0, 0.0)
                    glBegin(GL_LINE_STRIP)
                    for a, b in zip(z,y):
                        glVertex2f(a, b)
                    glEnd()
                    glFlush()

                elif self.rad_one.get() == 2:
                    z = np.linspace(-4,4,1000)
                    y = np.abs(z)
                    glColor3f(0.0, 1.0, 0.0)
                    glPointSize(10)
                    glBegin(GL_LINE_STRIP)
                    for a, b in zip(z,y):
                        glVertex2f(a, b)
                    glEnd()
                    glFlush()

                elif self.rad_one.get() == 3:
                    z = np.linspace(0,5,4000)
                    y = np.sqrt(z)
                    glColor3f(0.0, 1.0, 0.0)
                    glPointSize(10)
                    glBegin(GL_LINE_STRIP)
                    for a, b in zip(z, y):
                        glVertex2f(a, b)
                        
                    glEnd()
                    glFlush()

                elif self.rad_one.get() == 4:
                    glPointSize(10)
                    glColor3f(0.0, 1.0, 0.0)
                    glBegin(GL_LINE_STRIP)
                    glVertex2f(-5,3)
                    glVertex2f(5,3)
                    glEnd()
                    glFlush()

                elif self.rad_one.get() == 5:
                    z = np.linspace(-5, 5, 4000)
                    y = np.cbrt(z)
                    glColor3f(0.0, 1.0, 0.0)
                    glPointSize(10)
                    glBegin(GL_LINE_STRIP)
                    for a, b in zip(z, y):
                        glVertex2f(a, b)
                    glEnd()
                    glFlush()

                elif self.rad_one.get() == 6:
                    z = np.linspace(-2, 2, 10000)
                    y = np.sqrt(1- (np.power(z,2))) + np.cbrt(np.power(z,2))
                    g = - np.sqrt(1- (np.power(z,2))) + np.cbrt(np.power(z,2))
                    glColor3f(0.0, 1.0, 0.0)
                    glPointSize(10)
                    glBegin(GL_LINE_STRIP)
                    for a, b in zip(z, y):
                        glVertex2f(a, b)

                    for a, b in zip(z, g):
                        glVertex2f(a, b)
                    glEnd()
                    glFlush()
                else:
                    pass

            def main():
                init()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            # quit()
                    draw()
                    pygame.display.flip()
                    pygame.time.wait(10)
            main()

    def close(self):
        self.root.destroy()

display = functionGraphs()
