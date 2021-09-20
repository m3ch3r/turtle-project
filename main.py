from turtle import *

from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import messagebox


turtle = Turtle()
turtle.speed(100)
"""
Turtle Project

Author: Braden Franklin
Date: 09/10/21
Course: Intro to computer Programming 1, Tri 1 2021

Description: WIP

"""
#allows the user to chose the color of the background
def createBackground():
    colorPicker = colorchooser.askcolor(title = "Choose your background color")
    turtle.color(colorPicker[1])
    turtle.pensize(10000)
    turtle.forward(1)
    turtle.pensize(1)

#creates an outline of the pumpkin
def createPumpkinOutline(x, y):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.circle(80, 180)
    turtle.forward(100)
    turtle.circle(80, 180)
    turtle.forward(100)

#creates the pumpkin
def createPumpkin():
    colorPicker = colorchooser.askcolor(title = "Choose your color for the pumpkin")
    print(colorPicker[1])
    turtle.color(colorPicker[1])
    x = simpledialog.askfloat("Input", "What x coordinate should the pumpkin be at on the screen?")
    y = simpledialog.askfloat("Input", "What y coordinate should the pumpkin be at on the screen?")
    turtle.begin_fill()
    createPumpkinOutline(x, y)
    turtle.end_fill()
    turtle.left(90)
    turtle.penup()
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.pendown()
    turtle.color("brown")
    turtle.pensize(30)
    turtle.circle(30, 60)
    turtle.left(210)
    turtle.pensize(5)
    createPumpkinOutline(x, y)
    turtle.penup()
    turtle.left(180)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(100)
    
#Carves the eyes for the pumpkin based on a tkinter input value
def createEyes(): 

    while True:
        p = simpledialog.askinteger("Input", """
        Input the number coresponding to the set of eyes you'd like to carve
        Type "1" for the "> <" eyes
        Type "2" for the "^ ^" eyes
        Type "3" for the "o o" eyes""")
        if p == 1: #Create the "> <" eye type
           print(p)
           turtle.right(90)
           turtle.forward(35)
           turtle.pendown()
           turtle.left(22.5)
           turtle.forward(25)
           turtle.back(25)
           turtle.right(45)
           turtle.forward(25)
           turtle.back(25)
           turtle.left(22.5)
           turtle.penup()
           turtle.back(70)
           turtle.left(180)
           turtle.pendown()
           turtle.right(22.5)
           turtle.forward(25)
           turtle.back(25)
           turtle.left(45)
           turtle.forward(25)
           turtle.back(25)
           turtle.penup()
           turtle.right(22.5)
           turtle.back(35)
           turtle.right(90)
           break
        elif p == 2: #Create the "^ ^" eye type
            print(p)
            turtle.right(90)
            turtle.forward(35)
            turtle.pendown()
            turtle.left(45)
            turtle.forward(25)
            turtle.right(90)
            turtle.forward(25)

            turtle.back(25)
            turtle.left(90)
            turtle.back(25)
            turtle.right(45)
            turtle.penup()
            turtle.back(70)
            turtle.right(180)

            turtle.right(45)
            turtle.pendown()
            turtle.forward(25)
            turtle.left(90)
            turtle.forward(25)

            turtle.penup()
            turtle.back(25)
            turtle.right(90)
            turtle.back(25)
            turtle.left(45)
            turtle.back(35)
            turtle.right(90)


            break
        elif p == 3: #Create the "o o" eye type
            print(p)
            turtle.right(90)
            turtle.forward(35)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(20)
            turtle.end_fill()
            turtle.penup()
            turtle.right(180)
            turtle.forward(80)
            turtle.pendown()
            turtle.right(180)
            turtle.begin_fill()
            turtle.circle(20)
            turtle.end_fill()
            turtle.penup()
            turtle.forward(40)
            turtle.left(90)
            break
        else:
            messagebox.showerror("Error", "Invalid Type entered.")

#Carves the mouth for the pumpkin based on a tkinter input value
def createMouth(): 
    while True: 
        p = simpledialog.askinteger("Input", """
        Input the number coresponding to the type of mouth you'd like to carve
        Type "1" for the "o" mouth
        Type "2" for the "w" mouth
        Type "3" for the "__" mouth
        """)
        if p == 1: #Creates the "o" mouth
            print(p)
            turtle.penup()
            turtle.back(60)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(15)
            turtle.end_fill()
            break
        elif p == 2: #Creates the "w" mouth
            print(p)
            turtle.penup()
            turtle.back(60)
            turtle.left(90)
            turtle.forward(20)
            turtle.pendown()
            turtle.write("w", font=("Verdana", 45, "normal"))
            break
        elif p == 3: #Creates the "__" mouth
            print(p)
            turtle.penup()
            turtle.back(60)
            turtle.pendown()
            turtle.pensize(5)
            turtle.right(90)
            turtle.forward(25)
            turtle.back(50)
            turtle.pensize(1)
            break
        else: 
            messagebox.showerror("Error", "Invalid Type entered.")
            
#main
def main():
    createBackground()
    createPumpkin()
    createEyes()
    createMouth()
    turtle.hideturtle()
    turtle.getscreen()._root.mainloop()
main()

