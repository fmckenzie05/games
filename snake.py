from random import randrange
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
score = 0  # Initialize score

def wrap(value, min, max):
    """Wrap value around min and max."""
    if value > max:
        return min
    if value < min:
        return max
    return value

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Wrap snake head around edges if it goes out of boundaries."""
    head.x = wrap(head.x, -200, 190)
    head.y = wrap(head.y, -200, 190)
    return True

def move():
    """Move snake forward one segment and move food randomly."""
    global score
    head = snake[-1].copy()
    head.move(aim)

    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        score += 1  # Increase score
        display_score()  # Update score display
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

def change_direction(x, y):
    """Change direction based on mouse click position relative to snake's head."""
    head = snake[-1]
    dx = x - head.x
    dy = y - head.y

    if abs(dx) > abs(dy):
        # Horizontal movement takes precedence if the click is more horizontal than vertical
        if dx > 0:
            change(10, 0)  # Move right
        else:
            change(-10, 0)  # Move left
    else:
        # Vertical movement otherwise
        if dy > 0:
            change(0, 10)  # Move up
        else:
            change(0, -10)  # Move down

def display_score():
    """Display the current score on the screen."""
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=("Arial", 14, "normal"))

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onscreenclick(change_direction)  # Change to mouse click

# Score display setup
score_turtle = Turtle(visible=False)
score_turtle.penup()
score_turtle.goto(0, 160)
score_turtle.color("black")
display_score()  # Initial score display

move()
done()
