import pygame
import time
import random

# Initialize Pygame to use its functions and libraries
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600  # Set the width and height of the game window

# Colors in RGB format
WHITE = (255, 255, 255)  # Color for text and background
BLACK = (0, 0, 0)  # Color for game background
RED = (213, 50, 80)  # Color for game messages and food
GREEN = (0, 255, 0)  # Color for the snake
BLUE = (50, 153, 213)  # Color for the score

# Snake block size
BLOCK_SIZE = 20  # The size of each block in the snake's body

# Clock for controlling the game speed
clock = pygame.time.Clock()

# Font styles for text
font_style = pygame.font.SysFont("bahnschrift", 25)  # Font for messages
score_font = pygame.font.SysFont("comicsansms", 35)  # Font for the score


# Function to display the score on the screen
def display_score(score):
    value = score_font.render(f"Your Score: {score}", True, BLUE)
    screen.blit(value, [0, 0])  # Render score at the top-left corner


# Function to draw the snake on the screen
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])

        # Draw each segment of the snake as a green rectangle.
        # Parameters:
        # - `screen`: The surface to draw on.
        # - `GREEN`: The color of the rectangle.
        # - `[block[0], block[1], block_size, block_size]`: A list specifying the rectangle's position (top-left corner at `block[0]`, `block[1]`) and size (`block_size` width and height).


# Function to display messages in the center of the screen
def display_message(msg, color):
    message = font_style.render(msg, True, color)
    screen.blit(message, [WIDTH / 6, HEIGHT / 3])


# Main game loop
def game_loop():
    game_over = False  # Flag to control the main game loop
    game_close = False  # Flag to indicate game over state

    # Initial position of the snake
    x, y = WIDTH / 2, HEIGHT / 2  # Start at the center of the screen
    x_change, y_change = 0, 0  # No movement initially

    # Snake body setup
    snake_list = []  # List to keep track of the snake's body segments
    length_of_snake = 1  # Initial length of the snake

    # Random position for the food
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    # Main game loop
    while not game_over:

        # Handle game over screen
        while game_close:
            screen.fill(BLACK)  # Clear the screen
            display_message(
                "You Lost! Press Q-Quit or C-Play Again", RED
            )  # Show game over message
            display_score(length_of_snake - 1)  # Display the final score
            pygame.display.update()  # Update the display

            # Event handling for game over state
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Quit the game
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Restart the game
                        game_loop()

        # Event handling for player inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit the game
                game_over = True
            if event.type == pygame.KEYDOWN:  # Detect key presses
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE  # Move left
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE  # Move right
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE  # Move up
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE  # Move down
                    x_change = 0

        # Check if the snake hits the wall
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Update the snake's position
        x += x_change
        y += y_change
        screen.fill(BLACK)  # Clear the screen
        pygame.draw.rect(
            screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE]
        )  # Draw the food

        # Update the snake's body
        snake_head = [x, y]  # Add the new head position
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]  # Remove the last segment if the snake hasn't grown

        # Check if the snake collides with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Draw the snake and update the score
        draw_snake(BLOCK_SIZE, snake_list)
        display_score(length_of_snake - 1)

        # Update the screen
        pygame.display.update()

        # Check if the snake eats the food
        if x == food_x and y == food_y:
            food_x = (
                round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            )  # Generate new food position
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            length_of_snake += 1  # Increase the snake's length

        # Control the game speed
        clock.tick(15)

    # Quit Pygame when the game ends
    pygame.quit()
    quit()


# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the game window
pygame.display.set_caption("Snake Game")  # Set the window title

# Run the game
game_loop()
