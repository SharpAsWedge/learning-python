from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.up()
        self.go_to_start()
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    
    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

# By the first video, initialization and move method were almost same as mine