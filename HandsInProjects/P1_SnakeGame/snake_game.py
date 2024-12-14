import pygame
import time
import random

# Intialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Snake
BLOCK_SIZE = 20

# Controlling the speed of the game through clock
clock = pygame.time.Clock()

# font styling
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def display_score(score):
    value = score_font.render(f"Your Score:{score}", True, BLACK)
    # display at top-corner
    screen.blit(value, [0, 0])


# function to draw snake on screen
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])


# function to display message on screen
def display_message(msg, color):
    message = font_style.render(msg, True, color)
    screen.blit(message, [WIDTH / 6, HEIGHT / 3])


# main function for game
def game_loop():
    game_over = False
    game_close = False

    # Initial position of snake
    # start at the center of screen
    x, y = WIDTH / 2, HEIGHT / 2
    # change in position, intially no movement
    x_change, y_change = 0, 0

    snake_list = []
    length_of_snake = 1

    # Initial position of food
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    # while game is running
    while not game_over:
        # while game over
        while game_close:
            # sets the screen background to black
            screen.fill(BLACK)
            # display the message then
            display_message("You Lost! Press Q-Quit or C-Play Again", RED)
            # final score display
            display_score(length_of_snake - 1)
            # update the display
            pygame.display.update()

            # Event handling
            # 1.for game over states
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # if q is pressed, quit the game
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    # if c is pressed, restart the game
                    if event.key == pygame.K_c:
                        game_loop()

            # 2. for player inputs
            for event in pygame.event.get():
                # if player quits the game
                if event.type == pygame.QUIT:
                    game_over = True
                # on user presses the key
                if event.type == pygame.KEYDOWN:
                    # it the key is left arrow key, move left
                    if event.key == pygame.K_LEFT:
                        x_change = -BLOCK_SIZE
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = BLOCK_SIZE
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -BLOCK_SIZE
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = BLOCK_SIZE
                        x_change = 0

            # Check if snake hits the boundary(wall) represented by width and height attribute
            if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
                game_close = True

            # update the snake position
            x += x_change
            y += y_change
            # clear the screen
            screen.fill(BLACK)
            # draw(render) the food
            pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

            # update the snake list(snake's body)
            snake_head = [x, y]
            snake_list.append(snake_head)
            # remove the last segement if the snake hasn't eaten the food(grown)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            # if snake collides with itself
            for block in snake_list[:-1]:
                if block == snake_head:
                    game_close = True

            # draw the snake and update the score
            draw_snake(BLOCK_SIZE, snake_list)
            display_score(length_of_snake - 1)

            # update the screen
            pygame.display.update()

            # check if the snake eats the food
            if x == food_x and y == food_y:
                # generate new food position
                food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20) * 20
                food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20) * 20
                # increase the length of snake
                length_of_snake += 1

            # controlling the game speed
            clock.tick(15)

        # # Quit pygame when the game ends
    pygame.quit()
    quit()


# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the Game
pygame.display.set_caption("Snake Game")


# Run the game by calling main function
game_loop()
