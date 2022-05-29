from turtle import Turtle, Screen
import time
from food import Food
from snake import Snake
from score import Score

screen = Screen()
snake = Snake()
food = Food()
scoreboard = Score()
screen.listen()
wait = 0.25
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake 2.0")
screen.tracer(0)

game_over = False

while not game_over:
    screen.update()
    time.sleep(wait)
    snake.move()
    if snake.head.distance(food)< 10:
        print("hit")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        wait =scoreboard.speeder()


    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<=10:
            #game_over = True
            scoreboard.reset()
            snake.reset()

    if snake.head.xcor() >=380 or snake.head.xcor() <=-380 or snake.head.ycor() >=360 or snake.head.ycor() <=-360:
        #game_over = True
        scoreboard.reset()
        snake.reset()

t1 = Turtle()
t1.color("white")
t1.write(f"Game over. Score:{scoreboard.score}", align="center", font=("Arial", 20, "bold"))
screen.exitonclick()
