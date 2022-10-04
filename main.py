from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=1920, height=1080) #screen size ps si
screen.bgcolor("black")
screen.tracer(0)               #avoid drawing
screen.title("Culebrita game") #title mamalón

starting_pos = [(0,0), (-20,0), (-40,0)]  #tuples to the start position (3 squares)

segments = []

for position in starting_pos:
    new_segment = Turtle("square") #create x squares to make our "snake"
    new_segment.color("white")
    new_segment.penup()            #no traces when moving the squares
    new_segment.goto(position)     #declare the positions of the squares, so it look like a snake
    segments.append(new_segment)   #adds every cuadrito to a list/array to move all the pieces at the same time


game_is_on = True
while game_is_on:
    screen.update()  #avoid running it from the start
    time.sleep(.5)   #avoid running it by "fps" of user computer

    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)








screen.exitonclick()