import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up brush sizes
SMALL_BRUSH = 5
MEDIUM_BRUSH = 10
LARGE_BRUSH = 20

# Set up shapes
RECTANGLE = 'rectangle'
CIRCLE = 'circle'

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up game variables
drawing = False
eraser = False
current_color = BLACK
current_brush_size = SMALL_BRUSH
current_shape = None
start_x, start_y = 0, 0
end_x, end_y = 0, 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Start drawing
            if not drawing:
                drawing = True
                start_x, start_y = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            # Stop drawing
            if drawing:
                drawing = False
                end_x, end_y = event.pos
                if current_shape == RECTANGLE:
                    pygame.draw.rect(screen, current_color, (start_x, start_y, end_x - start_x, end_y - start_y))
                elif current_shape == CIRCLE:
                    radius = int(((end_x - start_x) ** 2 + (end_y - start_y) ** 2) ** 0.5)
                    pygame.draw.circle(screen, current_color, (start_x, start_y), radius)
        elif event.type == pygame.KEYDOWN:
            # Select brush size
            if event.key == pygame.K_1:
                current_brush_size = SMALL_BRUSH
            elif event.key == pygame.K_2:
                current_brush_size = MEDIUM_BRUSH
            elif event.key == pygame.K_3:
                current_brush_size = LARGE_BRUSH
            # Select colors
            elif event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_e:
                # Toggle eraser mode
                eraser = not eraser
                current_color = WHITE if eraser else BLACK
            elif event.key == pygame.K_u:
                # Clear the screen
                screen.fill(WHITE)
            elif event.key == pygame.K_s:
                # Select rectangle shape
                current_shape = RECTANGLE
            elif event.key == pygame.K_c:
                # Select circle shape
                current_shape = CIRCLE

    if drawing:
        # Draw with selected brush size and color
        if eraser:
            pygame.draw.circle(screen, current_color, pygame.mouse.get_pos(), current_brush_size)
        else:
            pygame.draw.circle(screen, current_color, pygame.mouse.get_pos(), current_brush_size // 2)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()

