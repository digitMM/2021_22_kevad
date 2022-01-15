import turtle
import random

aken = turtle.Screen()
aken.setup(600,600)            
aken.title("Proovime värve ja asukoha vahetamist!")     
aken.bgcolor("#404040")             
mina = turtle.Turtle() 
mina.shape("turtle")    
mina.color("#4db8ff")
mina.pensize(5)    

# Värviskeemi muutus. Siin öeldakse, mitu väärtust saab kanali kohta olla ehk paneme paika värvi sügavuse
aken.colormode(255)

def värviline_jälg(x, y):
    mina.up()
    mina.goto(x, y)
    mina.down()
    # Värvikanali väärtused valitakse juhuslikult vahemikust 0-255.
    mina.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    mina.stamp()

aken.onclick(värviline_jälg, 1) # 1 - vasak klahv, 3 - parem 
aken.mainloop()