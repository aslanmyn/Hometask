import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Load images
car_image = pygame.image.load("Player.png")
coin_image = pygame.image.load("coin_gold_racer.png")

# Set up the clock
clock = pygame.time.Clock()

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up game variables
car_x = WIDTH // 2
car_y = HEIGHT - 100
car_speed = 5
coin_x = random.randint(0, WIDTH - coin_image.get_width())
coin_y = -coin_image.get_height()
coin_speed = 2
coins_collected = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # Update coin position
    coin_y += coin_speed

    # Check collision between car and coin
    car_rect = pygame.Rect(car_x, car_y, car_image.get_width(), car_image.get_height())
    coin_rect = pygame.Rect(coin_x, coin_y, coin_image.get_width(), coin_image.get_height())
    if car_rect.colliderect(coin_rect):
        coins_collected += 1
        coin_x = random.randint(0, WIDTH - coin_image.get_width())
        coin_y = -coin_image.get_height()

    # Draw background
    screen.fill(WHITE)

    # Draw car
    screen.blit(car_image, (car_x, car_y))

    # Draw coin
    screen.blit(coin_image, (coin_x, coin_y))

    # Draw collected coins count
    coins_text = font.render("Coins: {}".format(coins_collected), True, BLACK)
    screen.blit(coins_text, (WIDTH - coins_text.get_width() - 10, 10))

    # Update the screen
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()
