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
mina.speed(5) 

# Värviskeemi muutus. Siin öeldakse, mitu väärtust saab kanali kohta olla ehk paneme paika värvi sügavuse
aken.colormode(255)

def värv(x, y):
  mina.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def uus_asukoht(x, y):
    mina.up()
    mina.goto(x, y)
    mina.down()

# Jälgib kursoriga erkaani mööda vedamist
def joonista(x, y):
    mina.speed(10)
    mina.ondrag(None)
    # Häälestab nurga
    mina.setheading(mina.towards(x, y))
    mina.goto(x, y)
    # On rekursiivne
    mina.ondrag(joonista)
    mina.speed(5)

# Asukoha muutmine
aken.onclick(uus_asukoht, 1) # 1 - vasak klahv
# Värvi muutmine
aken.onclick(värv, 3) # 3 - parem klahv
# Joonistamise alustamine
mina.ondrag(joonista)

aken.mainloop()