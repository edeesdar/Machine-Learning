from turtle import Turtle,Screen
import random

#from udemy.tim import new_turtle

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make you bet",prompt="Which turtle will win the race? Enter your color:")
print(user_bet)
colors=["red","orange","yellow","green","purple"]
y_positions=[-70,-48,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto( x=-230 ,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! The {winning_color} turtle is the winner")
            else:
                print(f"you've lost The{winning_color} turtle is the winner!")    


        rand_distance = random.radint(0, 10)   
        Turtle.forward(rand_distance)

screen.exitonclick()