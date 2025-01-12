
# importing pygame
import pygame

# setting up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First PyGame Game")

running = True
while running:

    # handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # updating game state

    # clearing the display
    # filling the screen in black
    screen.fill((0, 0, 0))

    # rendering graphics

    # updating the display
    pygame.display.flip()

# quitting pygame
pygame.quit()
    
