## Impordime turtle
import turtle

# Teeme akna
aken = turtle.Screen() 
# Muudame akna laiust ja kõrgust
aken.setup(500, 300) 
# Muudame akna taustavärvi      
aken.bgcolor("pink")
# Muudame akna teksti   
aken.title("Tere, Mina!") 

# Teeme kilpkonna
mina = turtle.Turtle()
# Muudame kuju
mina.shape("turtle") 
# Muudame kiirust, valime aeglase kiiruse, et oleks hea jälgida
mina.speed(1)
# Muudame algset asukohta
mina.up()
mina.goto(-100,100)
mina.down()

mina.begin_fill()

# Sama asi tsükliga

varvid = ["red", "blue", "green", "yellow"]
nurk = 0
pliiatsi_suurus = 3

for varv in varvid:
  # Külg
  # Keerame paremale
  mina.right(nurk)
  # Muudame järgmiseks korraks nurga suuruse ära
  nurk = 90
  # Muudame värvi
  mina.color(varv)
  # Muudame pliiatsi paksust
  mina.pensize(pliiatsi_suurus)
  # Muudame pliiatsi suurust
  pliiatsi_suurus += 2
  # Liigume
  mina.forward(100)

mina.fillcolor("violet")
mina.end_fill()