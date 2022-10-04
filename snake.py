from turtle import Turtle
STARTING_POS = [(0,0), (-20,0), (-40,0)]  #tuples to the start position (3 squares)
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        # Create Snake
        for position in STARTING_POS:
            new_segment = Turtle("square")  # create x squares to make our "snake"
            new_segment.color("white")
            new_segment.penup()  # no traces when moving the squares
            new_segment.goto(position)  # declare the positions of the squares, so it look like a snake
            self.segments.append(new_segment)  # adds every cuadrito to a list/array to move all the pieces at the same time


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # para cada segmento de la culebrita en el rango de
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        self.segments[0].left(90)

