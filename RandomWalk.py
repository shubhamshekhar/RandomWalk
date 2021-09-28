from turtle import Turtle, Screen
import random


class RandomWalk:
    def __init__(self, shape, colour, speed, width):
        self.shape = shape
        self.colour = colour
        self.screen_width = 640
        self.screen_height = 640
        self.turtle = Turtle()
        self.turtle.speed(speed)
        self.turtle.width(width)
        self.my_screen = Screen()
        self.my_screen.setup(self.screen_width, self.screen_height)
        self.my_screen.title("Random Walk Painting")

    def check_boundary(self):
        """
        Checks if the turtle is going to cross the window pane or not
        :return:
        """
        turtle_position = self.turtle.position()
        if turtle_position[0] > self.screen_width/2 - 40 and int(self.turtle.heading()) == 0:
            return False
        if turtle_position[0] < -self.screen_width/2 + 40 and int(self.turtle.heading()) == 180:
            return False
        if turtle_position[1] > self.screen_height/2 - 40 and int(self.turtle.heading()) == 90:
            return False
        if turtle_position[1] < -self.screen_height/2 + 40 and int(self.turtle.heading()) == 270:
            return False
        return True

    def get_direction(self):
        """
        resets the direction of the turtle
        :return:
        """
        is_direction_correct = False
        while not is_direction_correct:
            direction = random.randint(0, 2)
            if direction == 0:
                self.turtle.left(90)
            elif direction == 1:
                self.turtle.right(90)
            else:
                self.turtle.right(0)
            is_direction_correct = self.check_boundary()

    def set_random_colour(self):
        """
        reset turtle colour
        :return:
        """
        r = random.randrange(255)
        g = random.randrange(255)
        b = random.randrange(255)
        self.turtle.color((r, g, b))

    def random_walk(self):
        """
        performs the walk
        :return:
        """
        self.my_screen.colormode(255)
        for _ in range(2000):
            self.get_direction()
            self.set_random_colour()
            self.turtle.forward(20)
        self.my_screen.exitonclick()
