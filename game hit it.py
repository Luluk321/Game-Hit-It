from turtle import *
from random import randint

tsize = 20
s_lebar = 200
s_tinggi = 180

class Sprite(Turtle):
    def __init__(self, x, y, step=10, shape='circle', color='black'):
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
        self.poin = 0

    def ke_atas(self):
        self.goto(self.xcor(), self.ycor() + self.step)

    def ke_bawah(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def ke_kiri(self):
        self.goto(self.xcor() - self.step, self.ycor())

    def ke_kanan(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True
        else:
            return False

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start      
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end)) 

    def make_step(self):
        self.forward(self.step)

        if self.distance(self.x_end, self.y_end) < self.step: # if distance less than half step
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start) # change direction


pemain = Sprite(0, -100, 10, 'circle', 'orange')
musuh1 = Sprite(-s_lebar, 0, 15, 'square', 'red')
musuh1.set_move(-s_lebar, 0, s_lebar, 0)
musuh2 = Sprite(s_lebar, 70, 15, 'square', 'red')
musuh2.set_move(s_lebar, 70, -s_lebar, 70)
gol = Sprite(0, 120, 20, 'triangle', 'green')

total_score = 0

scr = pemain.getscreen()
scr.listen()
scr.onkey(pemain.ke_atas, 'Up')
scr.onkey(pemain.ke_kiri, 'Left')
scr.onkey(pemain.ke_kanan, 'Right')
scr.onkey(pemain.ke_bawah, 'Down')

while total_score < 3:
    musuh1.make_step()
    musuh2.make_step()
    # gol.make_step()
    if pemain.is_collide(gol):
        total_score += 1
        pemain.goto(0, -100)
    if pemain.is_collide(musuh1) or pemain.is_collide(musuh2):
        gol.hideturtle()
        break

if total_score == 3:
    musuh1.hideturtle()
    musuh2.hideturtle()





