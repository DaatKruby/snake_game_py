from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=1920, height=1080) #screen size ps si
screen.bgcolor("black")
screen.tracer(0)               #avoid drawing
screen.title("Culebrita game") #title mamalón

snake = Snake()

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")

#Move
game_is_on = True
while game_is_on:
    screen.update()  #avoid running it from the start
    time.sleep(.1)   #avoid running it by "fps" of user computer

    snake.move()



screen.exitonclick()