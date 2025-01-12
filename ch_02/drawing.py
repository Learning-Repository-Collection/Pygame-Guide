
# importing pygame
import pygame

# starting up pygame
pygame.init()

# creating window
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Drawing Shapes Example")

# defining the color
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# defining center and radius
center = (200, 200)
radius = 50

# defining a rectangle
# parameters: x, y, width & height
rectangle = pygame.Rect(100, 100, 100, 100)


# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False
    
    # setting the background as black
    screen.fill((0, 0, 0))

    # draw a filled rectangle
    pygame.draw.rect(screen, green, rectangle)
    
    # drawing a circle
    pygame.draw.circle(screen, red, center, radius)

    # upading the display
    pygame.display.flip()

# stopping pygame
pygame.quit()