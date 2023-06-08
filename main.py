import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(key="Up", fun=player.move)

scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if player.distance(car) <= 20:
            scoreboard.game_over()
            game_is_on = False
            break
    if player.has_won():
        scoreboard.next_level()
        player.go_to_start()
        car_manager.level_up()


screen.exitonclick()
