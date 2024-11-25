import turtle
import random
import time

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
score = 0

#print(turtle_screen.getshapes())   ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']
turtle_score = turtle.Turtle()
turtle_cat = turtle.Turtle()
turtle_cat.shape("turtle")
timer_text = turtle.Turtle()


def set_turtle_score():
    turtle_score.color("purple")
    turtle_score.hideturtle()
    turtle_score.penup()
    top_height = turtle_screen.window_height() / 2
    y = top_height - top_height / 10
    turtle_score.setposition(0, y)
    turtle_score.write("Score: ", False, "center", ("Arial", 25, "normal"))

def set_turtle():

    turtle_cat.hideturtle()
    turtle_cat.teleport(random.randrange(0, 100), random.randrange(0, 100))
    turtle.listen()
    turtle_screen.onscreenclick(click_turtle)
    turtle_cat.showturtle()





def click_turtle(x, y):
    global score
    coordinates = turtle_cat.pos()
    x_turtle, y_turtle = coordinates
    if float((x + 10)) >= x_turtle >= float((x - 10)) and float((y + 10)) >= y_turtle >= float((y - 10)):
        score += +1
        turtle_score.clear()
        turtle_score.write("Score: {}".format(score), False, "center", ("Arial", 25, "normal"))
        print("score arttırıldı", score)
        print((x, y))


def countdown(t):
    top_height = turtle_screen.window_height() / 2
    y = top_height - top_height / 4
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    timer_text.hideturtle()
    timer_text.penup()
    timer_text.setposition(0,y)
    timer_text.clear()

    if t > 0:
        timer_text.clear()
        timer_text.write("Count: {:02d}:{:02d}".format(mins, secs), False, "center", ("Arial", 25, "normal"))
        turtle_cat.hideturtle()
        turtle_cat.speed(0)
        turtle_cat.teleport(random.randrange(0, 280), random.randrange(0, 280))
        turtle.listen()
        turtle_screen.onscreenclick(click_turtle)
        turtle_cat.showturtle()
        turtle_screen.ontimer(lambda: countdown(t - 1), 500)


    else:
        timer_text.clear()
        turtle_cat.hideturtle()
        timer_text.write("Game Over!!", False, "center", ("Arial", 25, "normal"))



def start_game():
    turtle.tracer(0)
    set_turtle_score()
    turtle.tracer(1)
    turtle_screen.ontimer(lambda: countdown(10),10)

start_game()
turtle.mainloop()
