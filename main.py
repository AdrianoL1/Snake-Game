import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.setup(width=600, height=600)
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect collision with food
        if snake.segments[0].distance(food) < 15:
            food.refresh()
            snake.extend()
            score.update_score()
            score.draw_score()

        # Detect collision with wall
        if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
            score.reset()
            snake.reset()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.segments[0].distance(segment) < 10:
                score.reset()
                snake.reset()

    screen.exitonclick()

if __name__ == "__main__":
    main()
