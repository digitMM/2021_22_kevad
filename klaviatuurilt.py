import turtle
               
aken = turtle.Screen()
aken.setup(600,600)            
aken.title("Proovime ise suunata!")     
aken.bgcolor("#404040")             
mina = turtle.Turtle() 
mina.shape("turtle")    
mina.color("#4db8ff")
mina.pensize(5)    

def edasi():
  mina.forward(30)

def vasakpööre():
  mina.left(45)

def parempööre():
  mina.right(45)

def lahku():
  aken.bye()                       

# Siin käivitatakse funktsioone
aken.onkey(edasi, "Up")
aken.onkey(vasakpööre, "Left")
aken.onkey(parempööre, "Right")
aken.onkey(lahku, "q")
# Siin "kuulatakse" klahvivajutusi
aken.listen()
# Lõputu tsükkel
aken.mainloop()
# Kui programm käivitada, siis enne klahvi vajutusi kliki aknal, muidu reageerin konsool.