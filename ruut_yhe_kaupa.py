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

# Täidame seest
mina.begin_fill()

# 1. külg
# Muudame värvi
mina.color('red')
# Muudame pliiatsi paksust
mina.pensize(3)
# Liigume
mina.forward(100)

# 2. külg
# Keerame paremale
mina.right(90)
# Muudame värvi
mina.color("blue")
# Muudame pliiatsi paksust
mina.pensize(5)
# Liigume
mina.forward(100)

# 3. külg
# Keerame paremale
mina.right(90)
# Muudame värvi
mina.color("green")
# Muudame pliiatsi paksust
mina.pensize(7)
# Liigume
mina.forward(100)

# 4. külg
# Keerame paremale
mina.right(90)
# Muudame värvi ja anname ka täitevärvi
mina.color("yellow", "purple")
# Muudame pliiatsi paksust
mina.pensize(9)
# Liigume
mina.forward(100)

mina.end_fill()

# Käivitame programmi
