from turtle import Turtle, Screen
import random

# Creating the prompt screen.

screen = Screen()
screen.setup(width=600,height=400) # screen size
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ") # starting prmpt

colors = ["red","orange","blue","yellow","green","purple"]
y_cor = [-70,-40,-10,20,50,80] # Starting y-coordinates of turtles
all_turtle = []

# Random step size for tutles
def turtle_step():
    move = random.randint(5,25)
    return move

# Creating tutles and setting them up at starting positions
for i in range(0,6):
    new_turtle = Turtle(shape="turtle") # Creates a tutle instance. Turtle is created at the center of the screen.
    new_turtle.penup() # Pen is taken up so that turtle does not draw a line when going to starting line
    new_turtle.color(colors[i]) 
    
    new_turtle.goto(x=-250,y=y_cor[i]) # Moving turtle from center to starting position.
    new_turtle.pendown() # Pen down now turtle will draw line when it moves.
    new_turtle.speed(1) # movement speed of turtle.
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on :
    for i in range(0,6):
        all_turtle[i].forward(turtle_step())
        if all_turtle[i].xcor()>250: # x coordinate = 250 is the finish line of race.
            if user_bet==colors[i]: # checks if the winning turtle is same as the user entered.
                print(f"You win. The {colors[i]} turtle is the winner. ")
                is_race_on=False                
            else:
                print(f"You lose. The {colors[i]} turtle is the winner.")
                is_race_on=False
            
screen.exitonclick()