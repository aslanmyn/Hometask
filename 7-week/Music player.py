import pygame

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((640, 480))

# Load a music file
pygame.mixer.music.load("🎷 СЕКТОР ГАЗА «Туман» СИМФОНИЧЕСКИЙ ОРКЕСТР  г.Воронеж 🎸 (256  kbps).mp3")

# Set the default volume
pygame.mixer.music.set_volume(0.5)

# Start playing the music
pygame.mixer.music.play()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.KEYUP:
                # Play music
                pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                # Stop music
                pygame.mixer.music.stop()
            elif event.key == pygame.K_LEFT:
                # Play next song
                pass  # TODO: Implement next song functionality
            elif event.key == pygame.K_b:
                # Play previous song
                pass  # TODO: Implement previous song functionality


    
    pygame.display.flip()

