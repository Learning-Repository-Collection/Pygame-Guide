#importing pygame
import pygame

# starting up pygame
pygame.init()

# loading the image
image = pygame.image.load("painting_marloes.jpg")

# .convert() creates a new copy of the image in pygame's format
# used for file formats .jpg or .bmp
# image = image.convert()

# used for images with transparency
# image = image.convert_alpha()

# viewing a larger portion of the image
view_rect = pygame.Rect(100, 50, 900, 900)

# check if image has loaded
if not image:
    print("Image not loaded!")
    quit()
else:
    print("Image has loaded!")


# loading images using blitting
# blit takes two arguments, source & destination
# source is the image surface you want to draw
# destination is the surface where you want to draw your image

# retrieving the screen surface
# setting the size of the screen
screen = pygame.display.set_mode((1000, 1000))

# blit the image onto the screen at specific coordinates
# a third parameter is the destination area
screen.blit(image, (0, 0), view_rect)

# update the display to reflect the images
pygame.display.flip()

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# stopping pygame
pygame.quit()