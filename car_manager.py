from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        r = random.randint(1, 5)
        if r == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            y = random.randint(-250, 250)
            car.goto(380, y)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



