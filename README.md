# Terminal Snake Game

A classic Snake game implemented in Python that runs directly in your terminal.

## Description

This is a simple implementation of the classic Snake game that runs in your terminal. The game uses Python's curses library to create an interactive terminal-based interface where you control a snake, collect food, and try to achieve the highest score possible without hitting the walls or your own snake body.

## Requirements

- Python 3.x
- curses library (built into Python's standard library on Linux/MacOS)
  - Windows users may need to install the `windows-curses` package

## Installation

No installation required beyond Python itself. The game uses the standard curses library which comes with Python on Unix-based systems (Linux/MacOS).

## How to Run

1. Clone this repository to your local machine
2. Make the game script executable (if needed):
   ```
   chmod +x snake_game.py
   ```
3. Run the game:
   ```
   ./snake_game.py
   ```
   
   Or alternatively:
   ```
   python3 snake_game.py
   ```

## Controls

- **↑ (Up Arrow)**: Move the snake up
- **↓ (Down Arrow)**: Move the snake down
- **← (Left Arrow)**: Move the snake left
- **→ (Right Arrow)**: Move the snake right
- **Ctrl+C**: Quit the game at any time

## Game Rules

1. Control the snake to eat the food (π symbol)
2. Each time the snake eats food, it grows longer and your score increases
3. The game ends if the snake hits the wall or collides with its own body
4. Try to achieve the highest score possible!

## Features

- Real-time snake movement using arrow keys
- Random food generation
- Score tracking
- Game over screen with final score
- Simple and clean terminal-based UI

## License

This project is open source and available under the MIT License.

