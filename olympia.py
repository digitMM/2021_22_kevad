## Impordime turtle
import turtle

# Teeme akna
aken = turtle.Screen() 
# Muudame akna laiust ja kõrgust
aken.setup(500, 300) 
# Muudame akna taustavärvi      
aken.bgcolor("white")
# Muudame akna teksti   
aken.title("Tere, Mina!") 

# Teeme kilpkonna
mina = turtle.Turtle()
# Muudame kuju
mina.shape("turtle") 
# Muudame kiirust, valime aeglase kiiruse, et oleks hea jälgida
mina.speed(4)
# Muudame algset asukohta
mina.up()
mina.goto(-200,100)
mina.down()

# 1. rõngas
# Muudame värvi
mina.color('#0081C8') # Internetist leiab värvikoodid
# Muudame pliiatsi paksust
mina.pensize(7)
# Liigume
mina.forward(100)
mina.right(90)
mina.forward(100)
mina.right(90)
mina.forward(100)
mina.right(90)
mina.forward(100)

# Muudame  asukohta
mina.up()
mina.goto(-80,0)
mina.down()

# 2. rõngas
mina.color('black') # Internetist leiab värvikoodid
# Muudame pliiatsi paksust
mina.pensize(7)
# Liigume
mina.forward(100)
mina.right(90)
mina.forward(100)
mina.right(90)
mina.forward(100)
mina.right(90)
mina.forward(100)

# Muudame  asukohta
mina.up()
mina.goto(140,0)
mina.down()

# 3. rõngas
mina.color('#EE334E') # Internetist leiab värvikoodid
# Muudame pliiatsi paksust
mina.pensize(7)
# Liigume
mina.forward(100)
mina.right(90)
mina.forward(100)
mina.right(90)
mina.forward(100)
mina.right(90)
mina.forward(100)

# Muudame  asukohta
mina.up()
mina.goto(-40,20)
mina.down()

# 4. rõngas
mina.color('#FCB131') # Internetist leiab värvikoodid
# Muudame pliiatsi paksust
mina.pensize(7)
# Liigume
mina.forward(100)
mina.right(90)
mina.forward(100)
mina.right(90)
mina.forward(100)
mina.right(90)
mina.forward(100)

# Muudame  asukohta
mina.up()
mina.goto(-20,20)
mina.down()

# 5. rõngas
mina.color('#00A651') # Internetist leiab värvikoodid
# Muudame pliiatsi paksust
mina.pensize(7)
# Liigume
mina.forward(100)
mina.right(90)
mina.forward(100)
mina.right(90)
mina.forward(100)
mina.right(90)
mina.forward(100)


# Käivitame programmi