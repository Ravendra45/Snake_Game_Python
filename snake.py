import pygame
import random
import time

# Snake game run karne ka function
def run_snake_game():
    # Pygame init
    pygame.init()

    # Screen setup (badi screen)
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("my cool Snake Game")

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)

    # Snake settings
    snake_block = 20
    snake_speed = 0.15  # jitna zyada number, utni slow speed
    snake_body = [[100, 50], [90, 50], [80, 50]]
    snake_direction = "RIGHT"

    # Food position
    food_pos = [random.randrange(1, (screen_width // snake_block)) * snake_block,
                random.randrange(1, (screen_height // snake_block)) * snake_block]

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != "DOWN":
                    snake_direction = "UP"
                elif event.key == pygame.K_DOWN and snake_direction != "UP":
                    snake_direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                    snake_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                    snake_direction = "RIGHT"

        # Snake move
        head = list(snake_body[0])
        if snake_direction == "UP":
            head[1] -= snake_block
        elif snake_direction == "DOWN":
            head[1] += snake_block
        elif snake_direction == "LEFT":
            head[0] -= snake_block
        elif snake_direction == "RIGHT":
            head[0] += snake_block

        snake_body.insert(0, head)

        # Snake eat food
        if head == food_pos:
            food_pos = [random.randrange(1, (screen_width // snake_block)) * snake_block,
                        random.randrange(1, (screen_height // snake_block)) * snake_block]
        else:
            snake_body.pop()

        # Collision check
        if head[0] < 0 or head[0] >= screen_width or head[1] < 0 or head[1] >= screen_height:
            running = False
        if head in snake_body[1:]:
            running = False

        # Draw
        screen.fill(black)
        for block in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], snake_block, snake_block))
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], snake_block, snake_block))

        pygame.display.flip()
        time.sleep(snake_speed)  # Speed control

    pygame.quit()

# Function call jab script run ho
if __name__ == "__main__":
    run_snake_game()