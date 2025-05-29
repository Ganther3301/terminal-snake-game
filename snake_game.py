#!/usr/bin/env python3
import curses
import random
import time

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    stdscr.timeout(100)  # Set input timeout for snake speed
    
    # Get terminal dimensions
    sh, sw = stdscr.getmaxyx()
    
    # Create a new window for the game
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(1)  # Enable keypad input
    win.timeout(100)  # Refresh every 100ms
    
    # Initialize snake position (middle of screen)
    snake_x = sw // 4
    snake_y = sh // 2
    
    # Initialize snake body
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]
    
    # Initialize food position
    food = [sh // 2, sw // 2]
    win.addch(food[0], food[1], curses.ACS_PI)
    
    # Initial direction is right
    key = curses.KEY_RIGHT
    
    # Initialize score
    score = 0
    
    # Create a new window for the score
    score_win = curses.newwin(1, sw, 0, 0)
    
    # Game loop
    while True:
        # Display score
        score_win.clear()
        score_win.addstr(0, 0, f"Score: {score}")
        score_win.refresh()
        
        # Get next key press
        next_key = win.getch()
        
        # If no key is pressed, use the previous key
        key = key if next_key == -1 else next_key
        
        # Calculate next position
        if key == curses.KEY_DOWN:
            new_head = [snake[0][0] + 1, snake[0][1]]
        elif key == curses.KEY_UP:
            new_head = [snake[0][0] - 1, snake[0][1]]
        elif key == curses.KEY_LEFT:
            new_head = [snake[0][0], snake[0][1] - 1]
        elif key == curses.KEY_RIGHT:
            new_head = [snake[0][0], snake[0][1] + 1]
        
        # Insert new head
        snake.insert(0, new_head)
        
        # Check if snake hits the border
        if (
            snake[0][0] in [0, sh - 1] or 
            snake[0][1] in [0, sw - 1] or 
            snake[0] in snake[1:]
        ):
            game_over(win, sh, sw, score)
            break
        
        # Check if snake eats the food
        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                new_food = [
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                ]
                food = new_food if new_food not in snake else None
            win.addch(food[0], food[1], curses.ACS_PI)
        else:
            # Move snake by removing the tail
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')
        
        # Draw snake head
        win.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
        
        # Refresh window
        win.refresh()

def game_over(win, sh, sw, score):
    win.clear()
    message = "GAME OVER!"
    score_msg = f"Final Score: {score}"
    restart_msg = "Press any key to exit..."
    
    win.addstr(sh // 2 - 1, (sw - len(message)) // 2, message)
    win.addstr(sh // 2, (sw - len(score_msg)) // 2, score_msg)
    win.addstr(sh // 2 + 1, (sw - len(restart_msg)) // 2, restart_msg)
    
    win.refresh()
    win.getch()  # Wait for key press

if __name__ == "__main__":
    try:
        # Initialize curses
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("Game terminated by user")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Thanks for playing Snake!")

