# games
Classic Snake Game with Python Turtle
This Python script is a modified version of the classic arcade game "Snake", developed using the Turtle graphics library. It features the basic gameplay of Snake, where the player controls a snake to eat food while avoiding collisions with itself or the edges of the game area.

Features
Wrap-around Movement: The snake can move across the boundaries of the game area and appear on the opposite side.
Mouse Control: Instead of keyboard inputs, this version of the game uses mouse clicks to change the direction of the snake.
Speed Adjustment: The speed of the snake can be adjusted by changing the timer settings.
Score Display: The game displays the length of the snake (score) each time it eats food.

How to Play
Starting the Game: Run the Python script to start the game.
Controlling the Snake: Click on the game window in the direction you want the snake to move. The snake will move towards the clicked point, choosing the shortest path (horizontal or vertical).
Objective: Guide the snake to eat the green squares (food) that appear randomly on the screen.
Scoring: Each piece of food eaten increases the length of the snake by one segment and increases your score.
Game Over: The game ends if the snake collides with itself.

Requirements
Python 3.x
Turtle Graphics Library
Freegames Library
Installation
Installation
Ensure you have Python 3 installed on your system. You can download it from Python's official website.

To install the required freegames library, use pip:

``` Python pip install freegames ```

Running the Game
To play the game, simply run the script in your Python environment:



``` python
python snake_game.py 
```

Replace snake_game.py with the path to the script file if necessary.

Customization
Speed Adjustment: To change the speed of the snake, modify the value in the ontimer(move, 100) call in the script. Lower values make the snake move faster, higher values make it slower.
License
This project is open source and available under the MIT License

