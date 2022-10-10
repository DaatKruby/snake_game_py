import turtle
from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600) #screen size ps si
screen.bgcolor("grey")
screen.tracer(0)               #avoid drawing
screen.title("Culebrita game") #title mamalón

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")

#Move
game_is_on = True
while game_is_on:
    screen.update()  #avoid running it from the start
    time.sleep(.08)   #avoid running it by "fps" of user computer

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh();



screen.exitonclick()