from turtle import Turtle, Screen
oyna = Screen()
oyna.title("Koptok o'yini")

chiziq = Turtle()
chiziq.color('green')
chiziq.pensize(5)
chiziq.speed(0)
chiziq.hideturtle()
chiziq.up()
chiziq.goto(300, 300)
chiziq.down()
chiziq.goto(300, -300)
chiziq.goto(-300, -300)
chiziq.goto(-300, 300)
chiziq.goto(300, 300)

varata_tepa = Turtle()
varata_tepa.color('green')
varata_tepa.pensize(5)
varata_tepa.speed(0)
varata_tepa.hideturtle()
varata_tepa.up()
varata_tepa.goto(-100, 300)
varata_tepa.down()
varata_tepa.goto(-100, 230)
varata_tepa.goto(100, 230)
varata_tepa.goto(100, 300)
varata_tepa.goto(-100, 300)

varata_past = Turtle()
varata_past.color('green')
varata_past.pensize(5)
varata_past.speed(0)
varata_past.hideturtle()
varata_past.up()
varata_past.goto(100, -300)
varata_past.down()
varata_past.goto(100, -230)
varata_past.goto(-100, -230)
varata_past.goto(-100, -300)
varata_past.goto(100, -300)


koptok = Turtle()
koptok.shape('circle')
koptok.color('blue')
koptok.up()
koptok.goto(0, 0)

step_x = 3
step_y = 2
while True:
    x, y = koptok.position()
    
    if x + step_x >= 300 or x + step_x <= -300:
        step_x = -step_x
    if y + step_y >= 300 or y + step_y <= -300:
        step_y = -step_y
    if x <= -10 and y <= 290:
        break


    koptok.goto(x+step_x, y+step_y)
    
oyna.mainloop()
        


